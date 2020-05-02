stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

summary_prices = {}

for key, value in stock.items():
    summary_prices[key] = value * prices[key]

total_prices = 0.00

for value in summary_prices.values():
    total_prices += value

print(summary_prices)
print(f'Total prices: {total_prices}')