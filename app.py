import json
import random
from datetime import datetime
from flask import Flask, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory alert database for the SOC session
ALERT_LOGS = []

EVENT_TYPES = [
    {
        "event_id": 1,
        "name": "Encoded PowerShell Execution",
        "technique": "T1059.001",
        "severity": "HIGH",
        "desc": "powershell.exe executed -EncodedCommand payload",
    },
    {
        "event_id": 13,
        "name": "Registry Run Key Modification",
        "technique": "T1547.001",
        "severity": "CRITICAL",
        "desc": "HKCU\\...\\Run modified by SOC_Lab_Test_Process",
    },
    {
        "event_id": 3,
        "name": "Outbound Port Sweep Detected",
        "technique": "T1046",
        "severity": "MEDIUM",
        "desc": "Rapid TCP connections to ports 135, 445, 3389",
    },
    {
        "event_id": 10,
        "name": "Process Access (LSASS Read)",
        "technique": "T1003.001",
        "severity": "CRITICAL",
        "desc": "Suspicious handle opened to lsass.exe process",
    },
]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/alerts", methods=["GET"])
def get_alerts():
    return jsonify(ALERT_LOGS)


@app.route("/api/simulate-attack", methods=["POST"])
def trigger_attack():

    selected_event = random.choice(EVENT_TYPES)
    alert = {
        "id": len(ALERT_LOGS) + 1,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "host": "VICTIM-WIN11-VM",
        "event_id": selected_event["event_id"],
        "name": selected_event["name"],
        "technique": selected_event["technique"],
        "severity": selected_event["severity"],
        "description": selected_event["desc"],
    }
    ALERT_LOGS.insert(0, alert)
    return jsonify({"status": "success", "alert": alert})


if __name__ == "__main__":
    app.run(debug=True, port=5000)