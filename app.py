from flask import Flask, request
import requests
import os

app = Flask(__name__)

API_KEY = "PUT_API_KEY_HERE"
SERVER_ID = "PUT_SERVER_ID_HERE"
PANEL_URL = "https://your-panel-url.com"
SECRET = "start123"

@app.route("/")
def home():
    return """
    <h2>Bot Control</h2>
    <button onclick="fetch('/start?key=start123')">
        Start Bot
    </button>
    """

@app.route("/start")
def start():
    if request.args.get("key") != SECRET:
        return "No access", 403

    url = f"{PANEL_URL}/api/client/servers/{SERVER_ID}/power"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "Application/vnd.pterodactyl.v1+json",
        "Content-Type": "application/json"
    }

    r = requests.post(url, json={"signal": "start"}, headers=headers)

    return f"STATUS: {r.status_code} RESPONSE: {r.text}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
