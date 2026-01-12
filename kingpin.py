import networkx as nx

def get_kingpin_scores(G):
    pagerank = nx.pagerank(G)
    betweenness = nx.betweenness_centrality(G)

    scores = {}
    for node in G.nodes():
        scores[node] = round(0.6 * pagerank[node] + 0.4 * betweenness[node], 4)

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)
