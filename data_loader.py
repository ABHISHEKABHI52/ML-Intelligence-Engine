import pandas as pd

def load_data():
    suspects = pd.read_csv("data/suspects.csv")
    calls = pd.read_csv("data/call_logs.csv")
    transactions = pd.read_csv("data/transactions.csv")
    return suspects, calls, transactions
