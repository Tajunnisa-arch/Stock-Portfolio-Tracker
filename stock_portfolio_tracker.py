
# Task 2: Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 170,
    "AMZN": 200
}

portfolio = []
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

# Display available stocks
print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

# Get stock details from the user
while True:
    stock_name = input(
        "\nEnter stock name (or DONE to finish): "
    ).strip().upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock name. Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity

    total_investment += investment

    portfolio.append({
        "stock": stock_name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

    print("Investment:", "$", investment)

# Display portfolio summary
print("\n===== PORTFOLIO SUMMARY =====")

for item in portfolio:
    print(
        item["stock"],
        "| Quantity:", item["quantity"],
        "| Price: $", item["price"],
        "| Investment: $", item["investment"]
    )

print("\nTotal Investment: $", total_investment)

# Optional: Save the result to a text file
save = input("\nSave result to a text file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("STOCK PORTFOLIO SUMMARY\n")

        for item in portfolio:
            file.write(
                f"{item['stock']} | Quantity: {item['quantity']} "
                f"| Price: ${item['price']} "
                f"| Investment: ${item['investment']}\n"
            )

        file.write(f"\nTotal Investment: ${total_investment}\n")

    print("Results saved to portfolio.txt")

print("\nThank you!")
