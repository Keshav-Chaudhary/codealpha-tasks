import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data
def plot_stock_data(stock_data, ticker):
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label=ticker)
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Stock Price (USD)')
    plt.legend()
    plt.show()
def calculate_portfolio_value(portfolio):
    total_value = 0
    for stock, quantity in portfolio.items():
        stock_data = get_stock_data(stock, start_date, end_date)
        latest_price = stock_data['Close'].iloc[-1]
        total_value += latest_price * quantity
    return total_value
portfolio = {'AAPL': 5, 'GOOGL': 3, 'MSFT': 4}
start_date = '2023-01-01'
end_date = datetime.today().strftime('%Y-%m-%d')

# Plot individual stocks
for stock, quantity in portfolio.items():
    stock_data = get_stock_data(stock, start_date, end_date)
    plot_stock_data(stock_data, stock)

# Plot overall portfolio value
portfolio_value = calculate_portfolio_value(portfolio)
print(f'Portfolio Value: ${portfolio_value:.2f}')
