import csv

def main():
    # 1. Hardcoded stock prices (Mock Database)
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 370,
        "AMZN": 145
    }

    print("--- Simple Stock Portfolio Tracker ---")
    print(f"Available stocks: {', '.join(stock_prices.keys())}\n")

    portfolio = []
    total_investment = 0

    # 2. Collect user input
    while True:
        symbol = input("Enter stock symbol (or type 'done' to finish): ").upper()
        
        if symbol == 'DONE':
            break
        
        if symbol in stock_prices:
            try:
                quantity = int(input(f"How many shares of {symbol} do you own? "))
                
                # Calculation
                price = stock_prices[symbol]
                holding_value = price * quantity
                total_investment += holding_value
                
                # Store for summary and file saving
                portfolio.append({
                    "Symbol": symbol,
                    "Shares": quantity,
                    "Price": price,
                    "Value": holding_value
                })
            except ValueError:
                print("Invalid input. Please enter a whole number for shares.")
        else:
            print(f"Sorry, we don't have price data for {symbol}. Try AAPL, TSLA, etc.")

    # 3. Display Results
    print("\n" + "="*30)
    print("YOUR PORTFOLIO SUMMARY")
    print("="*30)
    
    for item in portfolio:
        print(f"{item['Symbol']}: {item['Shares']} shares @ ${item['Price']} = ${item['Value']}")
    
    print("-" * 30)
    print(f"TOTAL INVESTMENT: ${total_investment}")
    print("="*30)

    # 4. Optional: Save to CSV
    save_choice = input("\nWould you like to save this to a file? (y/n): ").lower()
    if save_choice == 'y' and portfolio:
        filename = "my_portfolio.csv"
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=["Symbol", "Shares", "Price", "Value"])
                writer.writeheader()
                writer.writerows(portfolio)
                # Adding a total row at the end
                file.write(f"\nTotal Investment,,,${total_investment}")
            
            print(f"Success! Portfolio saved to {filename}")
        except Exception as e:
            print(f"An error occurred while saving: {e}")

if __name__ == "__main__":
    main()