import pandas as pd
import yfinance as yf

# download Truist stock info for 2021
df = yf.download("TFC",
                 start = "2021-01-01",
                 end = "2021-12-31")

df = df.loc[:, ["Adj Close"]]

# calculate simple return
df["simple_rtn"] = df["Adj Close"].pct_change()

df