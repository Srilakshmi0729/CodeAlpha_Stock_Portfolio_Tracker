import csv

# Hardcoded stock prices (price per share)
stock_prices = {
    'TCS': 3540.50,
    'INFY': 1487.20,
    'RELIANCE': 2850.75,
    'HDFCBANK': 1723.40,
    'WIPRO': 458.60,
    'SBIN': 715.00,
    'AAPL':180.00,
    'TSLA':250.00
}

portfolio = []
total_investment = 0.0

print("📈 Stock Portfolio Tracker")
print("Available Stocks:", ', '.join(stock_prices.keys()))
print("Type 'q' to quit and view summary.\n")

while True:
    stock = input("Enter stock name: ").upper()
    if stock == 'Q':
        break
    if stock not in stock_prices:
        print("❌ Stock not found in price list. Try again.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
    except ValueError:
        print("❌ Invalid quantity. Must be an integer.\n")
        continue

    price = stock_prices[stock]
    total = quantity * price
    total_investment += total

    portfolio.append({
        'Stock': stock,
        'Quantity': quantity,
        'Price': price,
        'Total': total
    })

    print(f"✅ Added {quantity} shares of {stock} at ₹{price:.2f} each. Subtotal: ₹{total:.2f}\n")

# --- Display Summary ---
print("\n📊 Portfolio Summary")
print("-" * 50)
print(f"{'Stock':10} {'Qty':>6} {'Price':>10} {'Total':>12}")
print("-" * 50)
for entry in portfolio:
    print(f"{entry['Stock']:10} {entry['Quantity']:6} ₹{entry['Price']:9.2f} ₹{entry['Total']:11.2f}")
print("-" * 50)
print(f"{'Grand Total':>30}: ₹{total_investment:.2f}")

# --- Optional Save to File ---
choice = input("\n💾 Do you want to save the result? (y/n): ").lower()
if choice == 'y':
    file_type = input("Save as (1) TXT or (2) CSV? Enter 1 or 2: ")
    
    if file_type == '1':
        with open("portfolio_summary.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("-" * 50 + "\n")
            for entry in portfolio:
                f.write(f"{entry['Stock']:10} Qty: {entry['Quantity']:3} @ ₹{entry['Price']:.2f} = ₹{entry['Total']:.2f}\n")
            f.write("-" * 50 + "\n")
            f.write(f"Grand Total Investment: ₹{total_investment:.2f}\n")
        print("✅ Saved to portfolio_summary.txt")

    elif file_type == '2':
        with open("portfolio_summary.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Stock', 'Quantity', 'Price', 'Total'])
            for entry in portfolio:
                writer.writerow([entry['Stock'], entry['Quantity'], entry['Price'], entry['Total']])
            writer.writerow(['', '', 'Grand Total', total_investment])
        print("✅ Saved to portfolio_summary.csv")

    else:
        print("❌ Invalid choice. Not saved.")

else:
    print("⚠️ Not saved. Program finished.")
import csv

# Hardcoded stock prices (price per share)
stock_prices = {
    'TCS': 3540.50,
    'INFY': 1487.20,
    'RELIANCE': 2850.75,
    'HDFCBANK': 1723.40,
    'WIPRO': 458.60,
    'SBIN': 715.00
}

portfolio = []
total_investment = 0.0

print("📈 Stock Portfolio Tracker")
print("Available Stocks:", ', '.join(stock_prices.keys()))
print("Type 'q' to quit and view summary.\n")

while True:
    stock = input("Enter stock name: ").upper()
    if stock == 'Q':
        break
    if stock not in stock_prices:
        print("❌ Stock not found in price list. Try again.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
    except ValueError:
        print("❌ Invalid quantity. Must be an integer.\n")
        continue

    price = stock_prices[stock]
    total = quantity * price
    total_investment += total

    portfolio.append({
        'Stock': stock,
        'Quantity': quantity,
        'Price': price,
        'Total': total
    })

    print(f"✅ Added {quantity} shares of {stock} at ₹{price:.2f} each. Subtotal: ₹{total:.2f}\n")

# --- Display Summary ---
print("\n📊 Portfolio Summary")
print("-" * 50)
print(f"{'Stock':10} {'Qty':>6} {'Price':>10} {'Total':>12}")
print("-" * 50)
for entry in portfolio:
    print(f"{entry['Stock']:10} {entry['Quantity']:6} ₹{entry['Price']:9.2f} ₹{entry['Total']:11.2f}")
print("-" * 50)
print(f"{'Grand Total':>30}: ₹{total_investment:.2f}")

# --- Optional Save to File ---
choice = input("\n💾 Do you want to save the result? (y/n): ").lower()
if choice == 'y':
    file_type = input("Save as (1) TXT or (2) CSV? Enter 1 or 2: ")
    
    if file_type == '1':
        with open("portfolio_summary.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("-" * 50 + "\n")
            for entry in portfolio:
                f.write(f"{entry['Stock']:10} Qty: {entry['Quantity']:3} @ ₹{entry['Price']:.2f} = ₹{entry['Total']:.2f}\n")
            f.write("-" * 50 + "\n")
            f.write(f"Grand Total Investment: ₹{total_investment:.2f}\n")
        print("✅ Saved to portfolio_summary.txt")

    elif file_type == '2':
        with open("portfolio_summary.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Stock', 'Quantity', 'Price', 'Total'])
            for entry in portfolio:
                writer.writerow([entry['Stock'], entry['Quantity'], entry['Price'], entry['Total']])
            writer.writerow(['', '', 'Grand Total', total_investment])
        print("✅ Saved to portfolio_summary.csv")

    else:
        print("❌ Invalid choice. Not saved.")

else:
    print("⚠️ Not saved. Program finished.")
