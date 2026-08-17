import pandas as pd

# Load CSV
df = pd.read_csv("india_exchange_rates.csv")

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

print("=== INDIA CURRENCY EXCHANGE RATE ANALYSIS ===")

# Basic statistics
print("\nTotal currencies:", df["currency"].nunique())

print("\nHighest exchange rate:")
print(df.loc[df["rate"].idxmax()])

print("\nLowest exchange rate:")
print(df.loc[df["rate"].idxmin()])

# Selected currencies
selected = df[df["currency"].isin(["USD", "EUR", "GBP", "JPY"])]

print("\nSelected Currency Rates:")
print(selected[["currency", "rate"]])

# Sort currencies by rate
print("\nTop 10 currencies by rate:")
print(df.sort_values("rate", ascending=False).head(10))

# Save sorted results
df.sort_values("rate", ascending=False).to_csv(
    "exchange_rates_sorted.csv",
    index=False
)

print("\nAnalysis completed!")
print("Created: exchange_rates_sorted.csv")