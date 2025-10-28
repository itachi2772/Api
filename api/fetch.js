export default async function handler(req, res) {
  const { aadhaar, key } = req.query;

  // 🟢 If no Aadhaar given → show usage info
  if (!aadhaar) {
    return res.status(200).json({
      message: "🟢 Aadhaar Family Info API by @Mr_Itachi007",
      usage: "/fetch?aadhaar=YOUR_AADHAAR_NUMBER&key=itachi007"
    });
  }

  // 🛡️ Key check
  if (key !== "itachi007") {
    return res.status(403).json({
      error: "❌ Invalid API key",
      note: "Use key=itachi007 to access this API"
    });
  }

  try {
    // 🔹 Your main source API (with real working key)
    const sourceApi = `https://family-members-n5um.vercel.app/fetch?aadhaar=${aadhaar}&key=paidchx`;

    // 🔹 Fetch from original API
    const response = await fetch(sourceApi);
    const data = await response.json();

    // 🔹 Send response with credit
    return res.status(200).json({
      developer: "@Mr_Itachi007",
      source: "family-members-n5um.vercel.app",
      result: data,
      credit: "by @Mr_Itachi007"
    });

  } catch (error) {
    return res.status(500).json({
      error: "⚠️ Failed to fetch data",
      details: error.message
    });
  }
}
