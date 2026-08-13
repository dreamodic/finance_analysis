import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df = pd.read_csv("./002594.csv")
price = df[["Date", "Close"]].copy()
price["Date"] = pd.to_datetime(price["Date"])

print(price["Date"].isna().sum())
print(price["Date"].duplicated().sum())
print(price["Date"].is_monotonic_increasing)

price["Peak"] = price["Close"].cummax()
price["Drawdown"] = (price["Close"] / price["Peak"] - 1)
price["Return"] = price["Close"].pct_change()
price["Rolling_vol"] = price["Return"].rolling(20).std()
price["annual_vol"] = (price["Rolling_vol"] * (252 ** 0.5))
subprice = price.loc[price["Drawdown"] <= -0.2]
print(subprice.head(10))

max_dd = price["Drawdown"].min()
max_dd_date = price.loc[price["Drawdown"] == max_dd]

print("最大回撤 %.3f" % max_dd,"最大回撤对应时间：",max_dd_date)

max_Rv_day = price["Rolling_vol"].idxmax()
print(price.loc[max_Rv_day])

plt.plot(price["Date"],price["annual_vol"], label = "Annual_Rv")

plt.title("Annual_Rv of BYD")
plt.xlabel("Date")
plt.ylabel("Annual_Rv")
plt.legend()
plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0))

plt.show() #test git

#vol analysis test