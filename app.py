import pprint

import ccxt
import pandas as pd
import pybit
from pybit.unified_trading import HTTP

#Necessary exchanges

bingx = ccxt.bingx()
bitbank = ccxt.bitbank()
bitfinex = ccxt.bitfinex()
bitget = ccxt.bitget()
bithumb = ccxt.bithumb()
bitmart = ccxt.bitmart()
bitmex = ccxt.bitmex()
bitstamp = ccxt.bitstamp()
kucoin = ccxt.kucoin()
binance = ccxt.binance()

needed_exchanges = [bingx, bitbank, bitfinex, bitget, bithumb, bitmart, bitmex, bitstamp, kucoin, binance]

#List for exchanges where we will buy
market_data_list_buy = []

#List for exchanges where we will sell
market_data_list_sell = []

#Commission on purchase
maker_fees = 0.001

#Commission on sale
take_fees = 0.001

#The commission for transfer in the network is None, because CCXT does not provide the corresponding data
transfer_fee_by_network = None

