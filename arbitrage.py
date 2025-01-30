from exchanges import needed_exchanges

#List for exchanges where we will buy
market_data_list_buy = []

#List for exchanges where we will sell
market_data_list_sell = []

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
                                prompt(buy_exchange, sell_exchange, market_data_list_buy[index_buy], market_data_list_sell[sell_para], buy_exchange.fetch_ticker(market_data_list_buy[index_buy])['last'], sell_exchange.fetch_ticker(market_data_list_sell[sell_para])['last'])
                                BreakLoops = True
                    except Exception:
                        continue