import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# print(help(minimize))

# Download and get Daily Returns
aapl = pd.read_csv("AAPL_CLOSE", index_col="Date", parse_dates=True)
cisco = pd.read_csv("CISCO_CLOSE", index_col="Date", parse_dates=True)
ibm = pd.read_csv("IBM_CLOSE", index_col="Date", parse_dates=True)
amzn = pd.read_csv("AMZN_CLOSE", index_col="Date", parse_dates=True)

stocks = pd.concat([aapl, cisco, ibm, amzn], axis=1)
stocks.columns = ["aapl", "cisco", "ibm", "amzn"]

log_ret = np.log(stocks / stocks.shift(1))


def get_ret_vol_sr(weights):
    """
    Takes in weights, returns array or return,volatility, sharpe ratio
    """
    weights = np.array(weights)
    ret = np.sum(log_ret.mean() * weights) * 252
    vol = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov() * 252, weights)))
    sr = ret / vol
    return np.array([ret, vol, sr])


def neg_sharpe(weights):
    return get_ret_vol_sr(weights)[2] * -1


# Contraints
def check_sum(weights):
    """
    Returns 0 if sum of weights is 1.0
    """
    return np.sum(weights) - 1


# By convention of minimize function it should be a function that returns zero for conditions
cons = {"type": "eq", "fun": check_sum}

# 0-1 bounds for each weight
bounds = ((0, 1), (0, 1), (0, 1), (0, 1))

# Initial Guess (equal distribution)
init_guess = [0.25, 0.25, 0.25, 0.25]

# Sequential Least SQuares Programming (SLSQP).
opt_results = minimize(
    neg_sharpe, init_guess, method="SLSQP", bounds=bounds, constraints=cons
)
print(opt_results)

####### All Optimal Portfolios (Efficient Frontier) #######

# Our returns go from 0 to somewhere along 0.3
# Create a linspace number of points to calculate x on
frontier_y = np.linspace(
    0, 0.3, 100
)  # Change 100 to a lower number for slower computers!


def minimize_volatility(weights):
    return get_ret_vol_sr(weights)[1]


frontier_volatility = []

for possible_return in frontier_y:
    # function for return
    cons = (
        {"type": "eq", "fun": check_sum},
        {"type": "eq", "fun": lambda w: get_ret_vol_sr(w)[0] - possible_return},
    )

    result = minimize(
        minimize_volatility, init_guess, method="SLSQP", bounds=bounds, constraints=cons
    )

    frontier_volatility.append(result["fun"])

plt.figure(figsize=(12, 8))
# Add frontier line
plt.plot(frontier_volatility, frontier_y, "g--", linewidth=3)
plt.xlabel("Volatility")
plt.ylabel("Return")

plt.show()
