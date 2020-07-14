import requests
import pandas as pd

etf_list = [
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


def create_url(ticker):
    return "https://etfdb.com/etf/{}/#holdings".format(ticker)


def create_holding_db(url):
    html = requests.get(url).content
    return pd.read_html(html)[2].head(15)


def create_holding_list(etf_list):
    etfHolding_List = []
    for etf in etf_list:
        etfHolding_List.append(create_holding_db(create_url(etf)))
    return etfHolding_List


etfs = create_holding_list(etf_list)

f = 1

