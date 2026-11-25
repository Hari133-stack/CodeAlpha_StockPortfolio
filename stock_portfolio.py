stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300
}

total_investment = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if name in stocks:
        investment = stocks[name] * quantity
        total_investment += investment

        print("Stock:", name)
        print("Price:", stocks[name])
        print("Investment:", investment)
    else:
        print("Stock not available!")

print("----------------------")
print("Total Investment:", total_investment)