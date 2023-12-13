import pandas as pd
import yfinance as yf
import numpy as np

# download data and keep adjusted close prices only
df = yf.download("AAPL",
                 start="2011-01-01",
                 end="2021-12-31",
                 progress=False)
df = df.loc[:, ["Adj Close"]]

# calculate the simple and log returns using adjusted close prices
df["simple_rtn"] = df["Adj Close"].pct_change()
df["log_rtn"] = np.log(df["Adj Close"]/df["Adj Close"].shift(1))

# inspect output
df.head(10)