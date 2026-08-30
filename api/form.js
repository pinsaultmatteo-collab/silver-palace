/* ============================================================
   SILVER PALACE — réception des formulaires
   Fonction serverless Vercel, zéro dépendance (fetch natif).

   Les données partent directement chez Brevo (hébergeur français,
   serveurs en UE) : rien ne transite par un tiers hors Europe et
   aucune candidature ne dort dans un tableau de bord externe.

   Variables d'environnement à définir dans Vercel :
     BREVO_API_KEY          clé API v3 (Brevo → SMTP & API → Clés API)
     MAIL_FROM              expéditeur validé chez Brevo
     MAIL_TO_RESERVATION    boîte de l'accueil
     MAIL_TO_CANDIDATURE    boîte de la direction (confidentiel)
     MAIL_TO_CONTACT        boîte générale
     BREVO_LIST_ID          id de la liste newsletter
     BREVO_DOI_TEMPLATE_ID  (optionnel) active le double opt-in
     BREVO_DOI_REDIRECT     (optionnel) page de retour après confirmation
   ============================================================ */

const BREVO = "https://api.brevo.com/v3";

/* Un schéma par formulaire : libellé lisible + champs obligatoires.
   Tout champ absent d'ici est ignoré — un bot ne peut pas injecter
   de contenu arbitraire dans l'e-mail. */
const FORMS = {
  reservation: {
    sujet: "Nouvelle réservation",
    destinataire: () => process.env.MAIL_TO_RESERVATION,
    requis: ["prenom", "email", "tel", "date"],
    champs: {
      prenom: "Prénom",
      email: "E-mail",
      tel: "Téléphone",
      date: "Date souhaitée",
      heure: "Heure d'arrivée",
      personnes: "Nombre de personnes",
      occasion: "Occasion",
      message: "Message",
    },
  },
  candidature: {
    sujet: "Candidature danseuse",
    destinataire: () => process.env.MAIL_TO_CANDIDATURE,
    requis: ["nom", "age", "tel"],
    champs: {
      nom: "Prénom / nom de scène",
      age: "Âge",
      tel: "Téléphone",
      email: "E-mail",
      instagram: "Instagram",
      experience: "Expérience",
      message: "Message",
    },
  },
  contact: {
    sujet: "Message depuis le site",
    destinataire: () => process.env.MAIL_TO_CONTACT,
    requis: ["nom", "email", "message"],
    champs: {
      nom: "Nom",
      email: "E-mail",
      sujet: "Sujet",
      message: "Message",
    },
  },
};

const echappe = (v) =>
  String(v).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])
  );

const emailValide = (v) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(String(v || "").trim());

async function brevo(chemin, corps) {
  const r = await fetch(BREVO + chemin, {
    method: "POST",
    headers: {
      "api-key": process.env.BREVO_API_KEY,
      "content-type": "application/json",
      accept: "application/json",
    },
    body: JSON.stringify(corps),
  });
  if (!r.ok) {
    const detail = await r.text().catch(() => "");
    const err = new Error(`Brevo ${r.status} ${detail.slice(0, 300)}`);
    err.statut = r.status;
    throw err;
  }
  return r;
}

/* ---------- Newsletter : inscription à une liste, pas un e-mail ---------- */
async function newsletter(data) {
  const email = String(data.email || "").trim();
  if (!emailValide(email)) return { code: 400, erreur: "email" };

  const listId = Number(process.env.BREVO_LIST_ID);
  const doi = process.env.BREVO_DOI_TEMPLATE_ID;

  if (doi) {
    // Double opt-in : Brevo envoie le mail de confirmation et n'ajoute
    // le contact à la liste qu'une fois le lien cliqué.
    await brevo("/contacts/doubleOptinConfirmation", {
      email,
      includeListIds: [listId],
      templateId: Number(doi),
      redirectionUrl: process.env.BREVO_DOI_REDIRECT || "https://silver-palace.com/",
    });
  } else {
    await brevo("/contacts", { email, listIds: [listId], updateEnabled: true });
  }
  return { code: 200 };
}

/* ---------- Formulaires transactionnels ---------- */
async function transactionnel(type, data) {
  const schema = FORMS[type];

  const manquant = schema.requis.find((c) => !String(data[c] || "").trim());
  if (manquant) return { code: 400, erreur: manquant };
  if (data.email && !emailValide(data.email)) return { code: 400, erreur: "email" };

  const lignes = Object.entries(schema.champs)
    .filter(([cle]) => String(data[cle] || "").trim())
    .map(
      ([cle, libelle]) =>
        `<tr><td style="padding:6px 14px 6px 0;color:#888;white-space:nowrap;vertical-align:top">${libelle}</td>` +
        `<td style="padding:6px 0"><strong>${echappe(data[cle]).replace(/\n/g, "<br>")}</strong></td></tr>`
    )
    .join("");

  const destinataire = schema.destinataire();
  if (!destinataire) return { code: 500, erreur: "config" };

  await brevo("/smtp/email", {
    sender: { email: process.env.MAIL_FROM, name: "Site Silver Palace" },
    to: [{ email: destinataire }],
    // Répondre directement à la personne depuis la boîte du club.
    ...(data.email && emailValide(data.email)
      ? { replyTo: { email: String(data.email).trim() } }
      : {}),
    subject: `${schema.sujet} — ${echappe(data.prenom || data.nom || data.email || "")}`.trim(),
    htmlContent:
      `<div style="font-family:system-ui,sans-serif;font-size:15px;color:#222">` +
      `<h2 style="font-weight:600;margin:0 0 18px">${schema.sujet}</h2>` +
      `<table style="border-collapse:collapse">${lignes}</table>` +
      `<p style="margin-top:22px;color:#999;font-size:12px">Envoyé depuis silver-palace.com</p></div>`,
  });
  return { code: 200 };
}

module.exports = async (req, res) => {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    return res.status(405).json({ ok: false });
  }

  try {
    const data = typeof req.body === "string" ? JSON.parse(req.body) : req.body || {};

    // Piège à robots : le champ est masqué, un humain ne le remplit jamais.
    // On répond 200 pour ne pas renseigner le bot sur la raison du rejet.
    if (String(data.website || "").trim()) return res.status(200).json({ ok: true });

    const type = String(data.type || "");
    if (type !== "newsletter" && !FORMS[type]) {
      return res.status(400).json({ ok: false, erreur: "type" });
    }
    if (!process.env.BREVO_API_KEY) {
      return res.status(500).json({ ok: false, erreur: "config" });
    }

    const r = type === "newsletter" ? await newsletter(data) : await transactionnel(type, data);
    if (r.code !== 200) return res.status(r.code).json({ ok: false, erreur: r.erreur });
    return res.status(200).json({ ok: true });
  } catch (e) {
    // Le détail part dans les logs Vercel, jamais dans la réponse publique.
    console.error("[form]", e && e.message);
    return res.status(502).json({ ok: false, erreur: "envoi" });
  }
};
