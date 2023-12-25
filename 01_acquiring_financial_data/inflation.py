import pandas as pd
import nasdaqdatalink



# download Truist stock info for 2021
df = nasdaqdatalink.ApiConfig.api_key = ""

df = df.loc[:, ["Adj Close"]]

# calculate simple return
df["simple_rtn"] = df["Adj Close"].pct_change()

df["real_rtn"] = (
    (df["simple_rtn"] + 1) / (df["inflation_rate"])
)

df