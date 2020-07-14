import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

my_year = 2017
my_month = 1
my_day = 2
my_hour = 13
my_minute = 30
my_second = 15

my_date = datetime(my_year, my_month, my_day, my_hour, my_minute, my_second)
my_date.day  # gives 2

first_two = [datetime(2017, 1, 2), datetime(2017, 1, 3)]

# Create date time index
datetime_index = pd.DatetimeIndex(first_two)

data = np.random.randn(2, 2)
cols = ["a", "b"]

df = pd.DataFrame(data, datetime_index, cols)
df.index.argmax()  # last date
df.index.max()  # give final date

########### Time Resampling ###########

# Option 1
df_2 = pd.read_csv("Apple.csv")

df_2["Date"] = pd.to_datetime(df_2["Date"])
df_2.info()  # Show data types --- good for testing
df_2.set_index("Date", inplace=True)

# Option 2
df_3 = pd.read_csv("Apple.csv", index_col="Date", parse_dates=True)

# Resample
df_2.resample(rule="A").mean()  # check documentation for RULE
df_2.resample(rule="Q").mean()


def first_day(entry):
    return entry[0]


df_2.resample(rule="A").apply(first_day)

df_2["Close"].resample(rule="A").mean().plot(kind="bar", figsize=(16, 6))
plt.show()

########### Time Shifting ###########
df_2.shift(periods=1)  # shift every data one day
df_2.tshift(freq="M")  # shift every day to the enf of month

########### Pandas rolling and expanding ###########

df_2["Close 30 day MA"] = df_2["Close"].rolling(window=30).mean()
df_2[["Close", "Close 30 day MA"]].plot(figsize=(16, 6))

df_2["Close"].expanding().mean().plot(figsize=(16, 6))

# Bollinger Bands
df_2["Close 20 day MA"] = df_2["Close"].rolling(window=20).mean()
df_2["Upper"] = df_2["Close 20 day MA"] + 2 * (df_2["Close"].rolling(window=20).std())
df_2["Lower"] = df_2["Close 20 day MA"] - 2 * (df_2["Close"].rolling(window=20).std())
df_2[["Close 20 day MA", "Upper", "Lower", "Close"]].tail(150).plot(figsize=(16,6))
plt.show()
