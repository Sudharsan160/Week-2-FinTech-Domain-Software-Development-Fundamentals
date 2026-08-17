import pandas as pd

data = {
    "date": "2026-08-17",
    "base_currency": "INR",
    "rates": {
        "AUD": 0.01468,
        "BRL": 0.05449,
        "CAD": 0.0145,
        "CHF": 0.00847,
        "CNY": 0.07049,
        "CZK": 0.21834,
        "DKK": 0.06745,
        "EUR": 0.00902,
        "GBP": 0.00771,
        "HKD": 0.08206,
        "HUF": 3.2653,
        "IDR": 186.34,
        "ILS": 0.03087,
        "ISK": 1.2829,
        "JPY": 1.6654,
        "KRW": 14.7675,
        "MXN": 0.1779,
        "MYR": 0.04249,
        "NOK": 0.09855,
        "NZD": 0.01768,
        "PHP": 0.64333,
        "PLN": 0.03885,
        "RON": 0.04727,
        "SEK": 0.09925,
        "SGD": 0.01335,
        "THB": 0.34542,
        "TRY": 0.50102,
        "USD": 0.01046,
        "ZAR": 0.1692
    }
}

rows = []

for currency, rate in data["rates"].items():
    rows.append({
        "date": data["date"],
        "base_currency": data["base_currency"],
        "currency": currency,
        "rate": rate
    })

df = pd.DataFrame(rows)

df.to_csv("india_exchange_rates.csv", index=False)

print("CSV created successfully!")
print(df)