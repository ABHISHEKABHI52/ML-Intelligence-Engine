from fastapi import FastAPI
from data_loader import load_data
from graph_builder import build_graph
from kingpin import get_kingpin_scores
from fraud_rings import detect_rings
from risk_model import train_and_score
from intelligence import generate_brief

app = FastAPI(title="Cybercrime Intelligence System")

@app.get("/")
def home():
    return {"status": "CIS AI Engine Running"}

@app.get("/analyze")
def analyze():
    suspects, calls, transactions = load_data()
    G = build_graph(calls, transactions)

    kingpins = get_kingpin_scores(G)
    rings = detect_rings(G)
    risks = train_and_score(G)

    results = []

    for _, row in suspects.iterrows():
        sid = row["suspect_id"]
        name = row["name"]

        ring = "None"
        for k, v in rings.items():
            if sid in v:
                ring = f"Ring-{k}"

        connections = list(G.neighbors(sid)) if sid in G else []

        try:
            brief = generate_brief(name, risks.get(sid,0), ring, connections)
        except:
            brief = "Gemini AI unavailable"

        results.append({
            "suspect": sid,
            "name": name,
            "risk": risks.get(sid,0),
            "ring": ring,
            "connections": connections,
            "ai_brief": brief
        })

    return {
        "kingpins": kingpins[:5],
        "rings": rings,
        "analysis": results
    }
