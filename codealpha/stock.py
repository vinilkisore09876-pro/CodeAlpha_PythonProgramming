# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300
}

total_investment = 0

n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock_name = input("\nEnter stock name (AAPL, TSLA, GOOGL, MSFT): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        print(f"Investment in {stock_name}: ${investment}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_investment)

# Optional: Save result to a text file
save = input("Do you want to save the result? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write(f"Total Investment Value: ${total_investment}")
    print("Result saved in portfolio.txt")