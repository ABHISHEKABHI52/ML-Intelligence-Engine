import requests
from config import GEMINI_API_KEY, GEMINI_URL

def generate_brief(name, risk, ring, connections):
    prompt = f"""
    Suspect: {name}
    Risk Score: {risk}
    Ring: {ring}
    Connections: {connections}

    Write a police intelligence briefing for prosecution.
    """

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    r = requests.post(GEMINI_URL + "?key=" + GEMINI_API_KEY, json=payload)

    return r.json()["candidates"][0]["content"]["parts"][0]["text"]
