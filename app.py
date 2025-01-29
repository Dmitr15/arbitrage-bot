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

