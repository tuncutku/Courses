import pandas_datareader as web
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import math

us_etf_list = [
    "ARKW",
    "CLOU",
    "ONLN",
    "EMQQ",
    "IBUY",
    "EBIZ",
    "BOTZ",
    "IYK",
    "JETS",
    "PBW",
]

canadian_bond_list = [
    "ZAG.TO",
    "BXF",
]

start = datetime.datetime(2019, 7, 1)


def create_etf_db(startDate, etfList):

    etfs = pd.concat(
        [web.DataReader(etf, "yahoo", start)["Adj Close"] for etf in etfList], axis=1
    )
    etfs.columns = etfList

    return np.log(etfs / etfs.shift(1))


log_ret = create_etf_db(start, us_etf_list)

frontier_volatility = []
optWeights = []
frontier_y = np.linspace(0, 0.7, 100)
n_etfs = len(log_ret.columns)
bounds = ((0, 1),) * n_etfs
init_guess = np.repeat((1 / n_etfs), n_etfs)


def minimize_volatility(weights):
    return get_ret_vol_sr(weights)[1]


# Contraints
def check_sum(weights):
    """
    Returns 0 if sum of weights is 1.0
    """
    return np.sum(weights) - 1


def get_ret_vol_sr(weights):
    """
    Takes in weights, returns array or return,volatility, sharpe ratio
    """
    weights = np.array(weights)
    ret = np.sum(log_ret.mean() * weights) * 252
    vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov() * 252, weights)))
    sr = ret / vol
    return np.array([ret, vol, sr])


for possible_return in frontier_y:
    # function for return
    cons = (
        {"type": "eq", "fun": check_sum},
        {"type": "eq", "fun": lambda w: get_ret_vol_sr(w)[0] - possible_return},
    )

    result = minimize(
        minimize_volatility, init_guess, method="SLSQP", bounds=bounds, constraints=cons
    )
    optWeights.append(np.round(result["x"], 2))
    frontier_volatility.append(result["fun"])

plt.figure(figsize=(12, 8))
# Add frontier line
plt.plot(frontier_volatility, frontier_y, "g--", linewidth=3)
plt.xlabel("Volatility")
plt.ylabel("Return")

plt.show()
