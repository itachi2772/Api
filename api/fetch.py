import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

MY_API_KEY = "itachi007"
SOURCE_API = "https://family-members-n5um.vercel.app/fetch"
SOURCE_KEY = "paidchx"

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "🟢 Aadhaar Family Info API by @Mr_Itachi007",
        "usage": "/fetch?aadhaar=YOUR_AADHAAR_NUMBER&key=itachi007"
    })

@app.route("/fetch", methods=["GET"])
def fetch_info():
    aadhaar = request.args.get("aadhaar")
    key = request.args.get("key")

    if not aadhaar:
        return jsonify({"error": "❌ Aadhaar number required"}), 400

    if key != MY_API_KEY:
        return jsonify({"error": "❌ Invalid API key"}), 403

    try:
        url = f"{SOURCE_API}?aadhaar={aadhaar}&key={SOURCE_KEY}"
        response = requests.get(url, timeout=10)
        data = response.json()
        data["credit"] = "🟢 Powered by @Mr_Itachi007"
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()
