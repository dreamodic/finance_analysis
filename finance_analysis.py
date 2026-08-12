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
print(price.head(10))

max_dd = price["Drawdown"].min()
max_dd_date = price["Drawdown"].idxmin()

print("最大回撤 %.3f" % max_dd,"最大回撤对应时间：",price.loc[max_dd_date])

plt.plot(price["Date"],price["Drawdown"], label = "Drawdown")

plt.title("Drawdown of BYD")
plt.xlabel("Date")
plt.ylabel("Drawdown")
plt.legend()
plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0))

plt.show() #test git