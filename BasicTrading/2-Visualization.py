import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

x = np.linspace(0, 5, 11)

y = x ** 2

## Functional Method

plt.plot(x, y, "r-")
plt.xlabel("numbers")
plt.ylabel("squared")
plt.show()

plt.subplot(1, 2, 1)
plt.plot(x, y, "r")
plt.subplot(1, 2, 2)
plt.plot(y, x, "b")
plt.show()

## Object Oriented Method

fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.set_title("My Title")
axes.set_xlabel("Hello")
axes.plot(x, y)
plt.show()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.5, 0.2, 0.6, 0.8])
plt.show()

## Multiple Figures

fig, axes = plt.subplots(nrows=1, ncols=2)
plt.tight_layout()
for current_ax in axes:
    current_ax.plot(x, y)
plt.show()

## Figure Size and DPI

fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 2))
axes[0].plot(x, y)
axes[1].plot(y, x)
plt.tight_layout()
plt.show()

## Plot formatting
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.plot(x, x ** 2, label="x squared", color="purple", lw=2)  # color RGB Hex code
ax.plot(x, x ** 3, label="x cube", alpha=0.8)  # alpha is transparency
ax.plot(x, x ** 4, label="x quad", linestyle="-.")
ax.plot(x, x ** 0.5, label="x sqrt", marker="o", markersize=4)
ax.legend(loc=0)
ax.set_xlim([0, 1])
plt.show()

## Pandas visualiation

df = pd.DataFrame(np.random.randn(1000, 3), columns=["a", "b", "c"])
df["a"].hist(bins=30)
df["a"].plot(kind="hist", bins=30)
df["a"].plot.hist(bins=30)

df["a"].plot.area(alpha=0.4)

df.plot.bar()

df.plot.scatter("a", "b")

# Time Series Visualization
from datetime import datetime

date_list = pd.date_range(end=datetime.today(), periods=100).to_pydatetime().tolist()
df_2 = pd.DataFrame(np.random.randn(100, 3), columns=["a", "b", "c"], index=date_list)
df_2["a"].plot(figsize=(12, 4), xlim=["2020-04-01", "2020-06-01"])

