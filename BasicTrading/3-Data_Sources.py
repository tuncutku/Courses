import pandas_datareader as web
from pandas_datareader.data import Options
import datetime

import quandl

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2019, 1, 1)

########## Yahoo & Google ##########
# Equity Prices
facebook = web.DataReader("FB", "yahoo", start, end)
# Option Prices
fb_options = Options("FB", "yahoo")
fb_options.get_options_data(expiry=fb_optipns.expirt_dates[0])

########## Quandl ##########

mydata = quandl.get("EIA/PET_RWTC_D", returns="numpy")
realEstate_SF = quandl.get("ZILLOW/C13_ZRIFAH")
stockApple = quandl.get("WIKI/AAPL.1")  # .1 gives the first column

