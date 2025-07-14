import json

with open("D:/problem statement/user-wallet-transactions.json", "r") as f:
    data = json.load(f)

print("Total records:", len(data))
print("First transaction example:\n")
print(json.dumps(data[0], indent=2))

from collections import defaultdict

wallet_data = defaultdict(list)

for txn in data:
    wallet = txn.get("userWallet")
    if wallet:
        wallet_data[wallet].append(txn)

print(f"Total unique wallets: {len(wallet_data)}")

# Show sample transaction count for 1 wallet
sample_wallet = list(wallet_data.keys())[0]
print(f"\nSample wallet: {sample_wallet}")
print(f"Number of transactions: {len(wallet_data[sample_wallet])}")

import pandas as pd

wallet_features = []

for wallet, txns in wallet_data.items():
    deposit_amt = 0
    borrow_amt = 0
    repay_amt = 0
    liquidation_count = 0
    total_txns = len(txns)

    for txn in txns:
        action = txn.get("action", "").lower()
        action_data = txn.get("actionData", {})
        amount = float(action_data.get("amount", "0"))

        if action == "deposit":
            deposit_amt += amount
        elif action == "borrow":
            borrow_amt += amount
        elif action == "repay":
            repay_amt += amount
        elif action == "liquidationcall":
            liquidation_count += 1

    repay_ratio = (repay_amt / borrow_amt) if borrow_amt != 0 else 0

    wallet_features.append({
        "wallet": wallet,
        "total_deposit": deposit_amt,
        "total_borrow": borrow_amt,
        "total_repay": repay_amt,
        "repay_ratio": repay_ratio,
        "num_liquidations": liquidation_count,
        "num_txns": total_txns,
    })

df = pd.DataFrame(wallet_features)
print(df.head())

import pandas as pd

wallet_features = []

for wallet, txns in wallet_data.items():
    deposit_amt = 0
    borrow_amt = 0
    repay_amt = 0
    liquidation_count = 0
    total_txns = len(txns)

    for txn in txns:
        action = txn.get("action", "").lower()
        action_data = txn.get("actionData", {})
        amount = float(action_data.get("amount", "0"))

        if action == "deposit":
            deposit_amt += amount
        elif action == "borrow":
            borrow_amt += amount
        elif action == "repay":
            repay_amt += amount
        elif action == "liquidationcall":
            liquidation_count += 1

    repay_ratio = (repay_amt / borrow_amt) if borrow_amt != 0 else 0

    wallet_features.append({
        "wallet": wallet,
        "total_deposit": deposit_amt,
        "total_borrow": borrow_amt,
        "total_repay": repay_amt,
        "repay_ratio": repay_ratio,
        "num_liquidations": liquidation_count,
        "num_txns": total_txns,
    })

df = pd.DataFrame(wallet_features)
print(df.head())
df.to_csv("wallet_features.csv", index=False)
print("Saved as wallet_features.csv")

def calculate_risk_score(row):
    score = 0

    if row["repay_ratio"] < 0.5 and row["total_borrow"] > 0:
        score += 30

    if row["total_borrow"] > 0:
        score += 30

    if row["num_liquidations"] >= 1:
        score += 30

    if row["num_txns"] < 5:
        score += 10

    return score

df["risk_score"] = df.apply(calculate_risk_score, axis=1)

def assign_label(score):
    if score >= 70:
        return "High Risk"
    elif score >= 40:
        return "Medium Risk"
    else:
        return "Low Risk"

df["risk_label"] = df["risk_score"].apply(assign_label)

print(df[["wallet", "risk_score", "risk_label"]].head())

