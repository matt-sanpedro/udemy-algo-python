import yfinance as yf
import datetime

print("Downloading yfinance data...")
"""
period: defines the time block
"""
# define time for data
# data = yf.download("MSFT", period="6mo")
# today = datetime.date.today()
# data = yf.download("MSFT", start="2017-01-01", end=str(today))

# extract interval data (limited to few months of data - finer granularity)
# do NOT get more than 1 month of interval data
today = datetime.date.today()
data = yf.download("MSFT", period="1mo", interval="5m")

# summarize statistics
data.info()
print("\n### Statistics ###")
print(data.describe())
print("\n### Example Elements ###")
print(data)
print("\n### END DATA PREVIEW ###")
