import yfinance as yf
import datetime as dt
import pandas as pd

print("Downloading yfinance data...")
"""
period: defines the time block
"""
# stocks list
stocks = ["AMZN", "MSFT", "INTC", "GOOG", "INFY.NS", "3988.HK"]

# define time for data
# data = yf.download("MSFT", period="6mo")
# today = dt.date.today()
# data = yf.download("MSFT", start="2017-01-01", end=str(today))

# extract interval data (limited to few months of data - finer granularity)
# do NOT get more than 1 month of interval data
# today = dt.date.today()
# data = yf.download("MSFT", period="1mo", interval="5m")

# datetime automation implementation - timedelta expects unit in days
start = dt.datetime.today() - dt.timedelta(30)
end = dt.datetime.today()
# data = yf.download(stocks, period="1mo", interval="5m")

# store entire dataframe with stock data
ohlcv_data = {}

# initialize blank dataframe variable
cl_price = pd.DataFrame()
# loop through list to collect data and save adjusted close values
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker,start,end)["Adj Close"]
    ohlcv_data[ticker] = yf.download(ticker,start,end)

# summarize statistics
cl_price.info()
print("\n### Statistics ###")
print(cl_price.describe())
print("\n### Example Elements ###")
print(cl_price)
print("\n### Shape ###")
print(cl_price.shape)
print("\n### END DATA PREVIEW ###")

# stocks dataframe with all data
print(ohlcv_data["GOOG"])
