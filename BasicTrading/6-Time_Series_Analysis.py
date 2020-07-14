import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

airline = pd.read_csv("airline_passengers.csv", index_col="Month")
airline.dropna(inplace=True)
airline.index = pd.to_datetime(airline.index)

#### SMA (Simple Moving Average) ####

airline["6-month-SMA"] = airline["Thousands of Passengers"].rolling(window=6).mean()
airline["12-month-SMA"] = airline["Thousands of Passengers"].rolling(window=12).mean()
airline.plot()
plt.show()

#### EWMA (Exponentially Weighted Moving Average) ####

airline["EWMA12"] = airline["Thousands of Passengers"].ewm(span=12).mean()
airline[["Thousands of Passengers", "EWMA12"]].plot()
plt.show()

#### ETS (Error Trend Seasonality) ####

from statsmodels.tsa.seasonal import seasonal_decompose

result = seasonal_decompose(airline["Thousands of Passengers"], model="additive")
result.plot()
plt.show()

#### ARIMA (Autoregressive Integrated Moving Average) ####

df = pd.read_csv("monthly-milk-production-pounds-p.csv")
df.columns = ["Month", "Milk in pounds per cow"]

# Weird last value at bottom causing issues
df.drop(168, axis=0, inplace=True)
df["Month"] = pd.to_datetime(df["Month"])
df.set_index("Month", inplace=True)

print(df.describe().transpose())

from statsmodels.tsa.seasonal import seasonal_decompose

decomposition = seasonal_decompose(df["Milk in pounds per cow"], freq=12)
fig = plt.figure()
fig = decomposition.plot()
fig.set_size_inches(15, 8)


def adf_check(time_series):
    """
    Pass in a time series, returns ADF report
    """
    result = adfuller(time_series)
    print("Augmented Dickey-Fuller Test:")
    labels = [
        "ADF Test Statistic",
        "p-value",
        "#Lags Used",
        "Number of Observations Used",
    ]

    for value, label in zip(result, labels):
        print(label + " : " + str(value))

    if result[1] <= 0.05:
        print(
            "strong evidence against the null hypothesis, reject the null hypothesis. Data has no unit root and is stationary"
        )
    else:
        print(
            "weak evidence against null hypothesis, time series has a unit root, indicating it is non-stationary "
        )


df["Milk First Difference"] = df["Milk in pounds per cow"] - df[
    "Milk in pounds per cow"
].shift(1)
adf_check(df["Milk First Difference"].dropna())

# Sometimes it would be necessary to do a second difference
# This is just for show, we didn't need to do a second difference in our case
df["Milk Second Difference"] = df["Milk First Difference"] - df[
    "Milk First Difference"
].shift(1)

adf_check(df["Milk Second Difference"].dropna())

df["Seasonal Difference"] = df["Milk in pounds per cow"] - df[
    "Milk in pounds per cow"
].shift(12)
# Seasonal Difference by itself was not enough!
adf_check(df["Seasonal Difference"].dropna())

# You can also do seasonal first difference
df["Seasonal First Difference"] = df["Milk First Difference"] - df[
    "Milk First Difference"
].shift(12)
df["Seasonal First Difference"].plot()

adf_check(df["Seasonal First Difference"].dropna())

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

fig_first = plot_acf(df["Milk First Difference"].dropna())
fig_seasonal_first = plot_acf(df["Seasonal First Difference"].dropna())

result = plot_pacf(df["Seasonal First Difference"].dropna())

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(
    df["Seasonal First Difference"].iloc[13:], lags=40, ax=ax1
)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(
    df["Seasonal First Difference"].iloc[13:], lags=40, ax=ax2
)
plt.show()

# We have seasonal data!
model = sm.tsa.statespace.SARIMAX(
    df["Milk in pounds per cow"], order=(0, 1, 0), seasonal_order=(1, 1, 1, 12)
)
results = model.fit()
print(results.summary())
results.resid.plot()
plt.show()
results.resid.plot(kind="kde")

df["forecast"] = results.predict(start=150, end=168, dynamic=True)
df[["Milk in pounds per cow", "forecast"]].plot(figsize=(12, 8))

from pandas.tseries.offsets import DateOffset

future_dates = [df.index[-1] + DateOffset(months=x) for x in range(0, 24)]
future_dates_df = pd.DataFrame(index=future_dates[1:], columns=df.columns)
future_df = pd.concat([df, future_dates_df])
future_df["forecast"] = results.predict(start=168, end=188, dynamic=True)
future_df[["Milk in pounds per cow", "forecast"]].plot(figsize=(12, 8))

