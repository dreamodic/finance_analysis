import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df = pd.read_csv("./002594.csv")
price = df[["Date","Close"]]
price["Date"] = pd.to_datetime(price["Date"])

monthly = price.set_index("Date")
print(monthly.head())
print(monthly.index)
monthly_close = monthly["Close"].resample("ME").last()
print(monthly_close.head())
monthly_return = monthly_close.pct_change()
print(monthly_return)
best_month = monthly_return.idxmax()
worst_month = monthly_return.idxmin()
print(best_month,monthly_return.loc[best_month],worst_month,monthly_return.loc[worst_month])

print(price["Date"].isna().sum())
print(price["Date"].duplicated().sum())
print(price["Date"].is_monotonic_increasing)

price["Return"] = price["Close"].pct_change()
returns = price["Return"].dropna()
skew = returns.skew()
kurt = returns.kurt()
max_return_index = price["Return"].idxmax()
min_return_index = price["Return"].idxmin()

print(price.loc[max_return_index],["Date","Close","Return"])
print(price.loc[min_return_index],["Date","Close","Return"])
print(price["Return"].max() * 100)
print(price["Return"].min() * 100)

print(skew)
print(kurt)

plt.plot(monthly_return.index, monthly_return.values, label = "monthly_return")
plt.title("Monthly_return of BYD")
plt.xlabel("Month")
plt.ylabel("Monthly_return")
plt.legend()

plt.show()

plt.hist(returns,bins = 100)
plt.title("Daily D")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")

plt.show()
