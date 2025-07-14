Aave V2 Wallet Risk Analysis

Overview:
This project analyzes over 100,000 DeFi transactions from the Aave V2 protocol on the Polygon network.  
It extracts wallet behavior features like deposits, borrows, repays, liquidations, and number of transactions.

Goal:
To assign a risk score and label (Low / Medium / High Risk) to each wallet based on their activity.

Files Included:
wallet_risk_analysis.py 
wallet_features.csv 
README.txt 

How to Run
1. Install required library: `pip install pandas`
2. Run the script: `python wallet_risk_analysis.py`
3. Output will be saved as `wallet_features.csv`

Features Used
total_deposit
total_borrow
total_repay
repay_ratio
num_liquidations
num_txns

Scoring Logic
Repay ratio < 0.5 → +30
Has borrow > 0 → +30
Liquidations >= 1 → +30
Fewer than 5 txns → +10

Lower score = safer wallet  
Higher score = riskier wallet
