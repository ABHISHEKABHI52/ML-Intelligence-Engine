# 🛡️ Cybercrime Intelligence System (CIS)  
**AI + Machine Learning Powered Criminal Network Intelligence Engine 🚔🤖**

---

## 🔍 Project Overview

This project contains the complete **ML + Intelligence Engine** for our Cybercrime Intelligence System.  
It converts raw police data (calls, transactions, suspects) into **actionable cybercrime intelligence** using:

- Graph Analysis 🕸️  
- Machine Learning 🤖  
- Google Gemini AI 🧠  

The engine automatically identifies:
- **Kingpins** 👑  
- **Fraud Rings** 🕵️  
- **Risk Levels** ⚠️  
- **AI-generated Police Briefings** 📄  

---

## 📁 Project Structure

```text
ml_engine/
│
├── app.py                 # FastAPI backend 🚀
├── config.py              # Gemini API configuration 🔐
├── data_loader.py         # Reads CSV crime data 📊
├── graph_builder.py       # Builds criminal relationship graph 🕸️
├── kingpin.py             # Finds network leaders 👑
├── fraud_rings.py         # Detects gangs using ML 🤖
├── risk_model.py          # Calculates suspect risk ⚠️
├── intelligence.py        # Generates Gemini AI briefs 🧠
├── requirements.txt      # Required Python libraries 📦
│
└── data/
    ├── suspects.csv       # Suspect details 👤
    ├── call_logs.csv      # Call connections 📞
    └── transactions.csv  # Money flow 💰
```


---

```text

🧠 How the ML + Intelligence Engine Works

Our Cybercrime Intelligence System follows a file-based AI pipeline,
where each module performs a specific role in converting raw crime
data into actionable intelligence 🚔.


data_loader.py — Data Ingestion 📊  
The system starts by loading three CSV files:
suspects.csv – list of suspects  
call_logs.csv – call connections between suspects  
transactions.csv – money flow between suspects  

These files provide the raw cybercrime data for analysis.

🕸️ graph_builder.py — Criminal Network Creation  
This module converts calls and transactions into a NetworkX graph:
- Each suspect becomes a node
- Each call or transaction becomes an edge

This builds a complete criminal relationship network used by all ML and AI modules.

---

👑 kingpin.py — Kingpin Detection  
Using PageRank and Betweenness Centrality, this file identifies the most powerful
and influential criminals in the network.These suspects are ranked as Kingpins.

---

🤖 fraud_rings.py — Fraud Ring Detection  
This module uses  KMeans clustering (Machine Learning) to group suspects into organized
gangs based on their connections.Each cluster represents a fraud ring.

---

⚠️ risk_model.py — Risk Scoring  
A Random Forest ML model calculates the probability of each suspect being high-risk.  
This allows law enforcement to prioritize arrests and investigations.

---

🧠 intelligence.py — AI Intelligence Briefing  
This module sends suspect details (risk score, fraud ring, connections) to Google Gemini AI, which generates:
- Police-style investigation reports  
- Prosecution-ready intelligence briefs  

---

🚀 app.py — API for Frontend  
This file connects all modules and exposes the main API using FastAPI.  
The frontend dashboard calls:

```

## 📊 Data Used

The engine works with three CSV files:

- **suspects.csv** → list of suspects 👤  
- **call_logs.csv** → who called whom 📞  
- **transactions.csv** → who sent money to whom 💰  

These files are loaded by `data_loader.py`.

---

## 🕸️ Criminal Network Creation

`graph_builder.py` builds a **NetworkX graph** where:
- Each suspect is a **node**
- Each call or money transfer is an **edge**

This creates the full **criminal network graph** used by all ML and AI modules.

---

## 👑 Kingpin Detection (Graph Intelligence)

`kingpin.py` applies:
- **PageRank**
- **Betweenness Centrality**

to identify criminals who control the network.  
The highest scoring suspects are marked as **Kingpins** 👑.

---

## 🕵️ Fraud Ring Detection (Machine Learning)

`fraud_rings.py` uses **KMeans clustering** 🤖 to group suspects into gangs based on their connections.  
Each cluster represents an **organized fraud ring**.

---

## ⚠️ Risk Scoring (Machine Learning)

`risk_model.py` uses **RandomForest ML** to assign a **risk probability** to every suspect based on their activity in the graph.

Example:
- `0.90` → Critical 🔴  
- `0.50` → Medium 🟠  
- `0.10` → Low 🟢  

---

## 🧠 AI Intelligence Briefing

`intelligence.py` sends suspect details to **Google Gemini API** and generates:

- Police-style investigation summaries  
- Prosecution-ready intelligence briefs 📄  

These are shown in the dashboard for each suspect.

---

## 🌐 FastAPI Backend

`app.py` connects all modules and exposes the main API:

http://127.0.0.1:8000

This endpoint returns:
- Kingpins 👑  
- Fraud rings 🕵️  
- Risk scores ⚠️  
- Gemini AI reports 🧠  

The frontend team uses this API to display:
- Network graph  
- Leaderboard  
- Fraud rings  
- AI briefing panels  

---

## 🔐 Gemini API Setup

1. Go to 👉 https://aistudio.google.com  
2. Click **Get API Key**  
3. Copy your key  
4. Paste it into `config.py`:

GEMINI_API_KEY = "YOUR_API_KEY"

---

## 🚀 How to Run

Install dependencies:
pip install -r requirements.txt

powershell

Start the engine:
uvicorn app:app --reload

Open in browser:
http://127.0.0.1:8000/analyze

---

## 🏆 Final Result

This ML + Intelligence Engine transforms raw cybercrime data into:

> **AI-powered, prosecution-ready cybercrime intelligence 🚔🔥**

It combines:
- Graph Intelligence 🕸️  
- Machine Learning 🤖  
- Generative AI 🧠  

to give law-enforcement a **powerful cybercrime investigation tool**.

---
