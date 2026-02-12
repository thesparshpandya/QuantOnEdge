import yfinance as yf

def get_financial_summary(ticker):
    """Fetches basic fundamentals."""
    # Append .NS for NSE stocks
    stock = yf.Ticker(ticker + ".NS")
    info = stock.info
    return {
        "Current Price": info.get('currentPrice'),
        "Market Cap": info.get('marketCap'),
        "PE Ratio": info.get('trailingPE'),
        "Sector": info.get('sector')
    }

if __name__ == "__main__":
    # Test with Tata Elxsi
    print(get_financial_summary("TATAELXSI"))