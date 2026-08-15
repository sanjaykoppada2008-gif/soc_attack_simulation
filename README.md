# 🛡️ SOC Attack Simulation & Telemetry Monitoring Console

A lightweight, full-stack Security Operations Center (SOC) attack simulation environment and threat monitoring dashboard. This project simulates adversary tactics mapped to the **MITRE ATT&CK** framework and visualizes security telemetry in real time via a custom Flask API and HTML/JS dashboard.

---

## 📌 Project Overview

This project provides hands-on exposure to both offensive adversary simulation and defensive SOC telemetry pipelines:
* **Adversary Simulation:** Emulates real-world threat techniques including obfuscated execution, persistence creation, process memory access, and network sweeps.
* **Defensive Monitoring:** Ingests live threat events, calculates critical metrics, and presents real-time alerts on a dark-themed SOC analyst dashboard.
* **In-Browser Testing:** Features an integrated test console to inject custom security telemetry directly from the web browser without external agent requirements.

---

## 🚀 Key Features

* 📊 **Real-Time SOC Dashboard:** Auto-refreshing event log console built with HTML5/CSS3 and JavaScript polling (`/api/alerts`).
* ⚡ **MITRE ATT&CK Mapping:** Pre-configured telemetry rules mapping simulated events to standard MITRE techniques (T1059.001, T1547.001, T1003.001, T1046).
* 🧪 **Interactive Test Suite:** In-browser preset buttons, custom telemetry form injector, and an automated background stress-testing toggle.
* 🔌 **REST API Endpoint:** Flask backend accepting structured JSON telemetry from host systems, virtual machines, or PowerShell execution scripts.

---

## 🛠️ Tech Stack & Tools

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend API** | Python 3, Flask, Flask-CORS | REST API handling event storage, alert metrics, and routing |
| **Frontend UI** | HTML5, CSS3, Vanilla JavaScript | Responsive dark-mode SOC dashboard |
| **Telemetry Generator** | PowerShell / REST API | Scripting payload for Windows endpoint attack simulation |
| **Telemetry Format** | JSON / Sysmon Event Schema | Sysmon Event IDs (1, 3, 10, 13) |

---

## 📁 Repository Structure

```text
soc_attack_simulation/
│
├── app.py                  # Flask API server & telemetry ingestion engine
├── requirements.txt        # Python dependencies
├── .gitignore              # Git ignore configuration
└── templates/
    └── index.html          # HTML/JS SOC Dashboard & Test Console
