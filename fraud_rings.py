import networkx as nx
from sklearn.cluster import KMeans

def detect_rings(G):
    nodes = list(G.nodes())

    if len(nodes) < 3:
        return {}

    X = nx.to_numpy_array(G)

    kmeans = KMeans(n_clusters=3, random_state=42)
    labels = kmeans.fit_predict(X)

    rings = {}
    for i, node in enumerate(nodes):
        rings.setdefault(int(labels[i]), []).append(node)

    return rings
