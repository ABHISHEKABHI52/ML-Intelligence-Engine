from sklearn.ensemble import RandomForestClassifier
import numpy as np

def train_and_score(G):
    nodes = list(G.nodes())
    X = []

    for n in nodes:
        degree = G.degree(n)
        X.append([degree])

    X = np.array(X)

    y = [1 if d[0] > 2 else 0 for d in X]

    model = RandomForestClassifier()
    model.fit(X, y)

    probs = model.predict_proba(X)

    risk = {}
    for i, n in enumerate(nodes):
        risk[n] = round(float(probs[i][1]), 3)

    return risk
