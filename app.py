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
MAKER_FEES=0.001

#Commission on sale
TAKER_FEES=0.001

#The commission for transfer in the network is None, because CCXT does not provide the corresponding data
transfer_fee_by_network = None
#BreakLoops = False

#Arbitrage opportunity function
def arb_oppotunities():
    BreakLoops = False
    for i in range(len(needed_exchanges)):
        for j in range(i+1, len(needed_exchanges)):
            try:
                buy_exchange = needed_exchanges[i]
                sell_exchange = needed_exchanges[j]
                market_data_list_buy = list(buy_exchange.load_markets().keys())
                market_data_list_sell = list(sell_exchange.load_markets().keys())
                market_data_list_buy.sort()
                market_data_list_sell.sort()
            except Exception:
                continue
            for buy_para in range(len(market_data_list_buy)):
                buy_a = market_data_list_buy[buy_para]
                if ':' in buy_a:
                    continue
                if BreakLoops == True:
                    BreakLoops = False
                    break
                for sell_para in range(len(market_data_list_sell)):
                    if BreakLoops:
                        break
                    sell_a = market_data_list_sell[sell_para]
                    str_a = str(sell_a)
                    if ':' in str_a:
                        continue
                    try:
                        if sell_a in market_data_list_buy:
                            index_buy = market_data_list_buy.index(str_a)
                            if buy_a != sell_a:

                                print(buy_exchange, sell_exchange, market_data_list_buy[index_buy], market_data_list_sell[sell_para], buy_exchange.fetch_ticker(market_data_list_buy[index_buy])['last'],
                                    sell_exchange.fetch_ticker(market_data_list_sell[sell_para])['last'])
                                BreakLoops = True
                    except Exception:
                        continue

#Prompt function
def prompt(buy_exchange, sell_exchange, buy_para, sell_para, buy_price, sell_price):
    spread = str(spread_calculation(buy_price, sell_price))+'%'
    if buy_price < sell_price:
        print(f'---{buy_para}---\nBuy at: {buy_exchange}\nSell at: {sell_exchange}\nPurchase price in tokens: {buy_price}\nSelling price: {sell_price}\n--Spread: {spread}--\n')


def spread_calculation(buy_price, sell_price):
    if buy_price < sell_price:
        spread = (sell_price/(buy_price-1))*100
    else:
        spread = (buy_price / (sell_price - 1)) * 100

    if spread > MAKER_FEES:
        return spread-MAKER_FEES

if __name__ == '__main__':
    arb_oppotunities()
