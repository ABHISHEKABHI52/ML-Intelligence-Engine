import networkx as nx

def build_graph(calls, transactions):
    G = nx.Graph()

    for _, row in calls.iterrows():
        G.add_edge(row["from"], row["to"], weight=row["duration"], type="call")

    for _, row in transactions.iterrows():
        G.add_edge(row["from"], row["to"], weight=row["amount"], type="money")

    return G
