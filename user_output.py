from calculation import spread_calculation
from calculation import MAKER_FEES, TAKER_FEES
def prompt(buy_exchange, sell_exchange, buy_para, sell_para, buy_price, sell_price):
    spread = str(spread_calculation(buy_price, sell_price))+'%'
    if buy_price < sell_price:
        print(f'---{buy_para}---\nBuy at: {buy_exchange}\nSell at: {sell_exchange}\nPurchase price in tokens: {buy_price}\nSelling price in tokens: {sell_price}\nMaker fees: {MAKER_FEES}\nTaker fees: {TAKER_FEES}\n--Spread: {spread}--\n')
    else:
        print(f'---{buy_para}---\nBuy at: {sell_exchange}\nSell at: {buy_exchange}\nPurchase price in tokens: {sell_price}\nSelling price: {buy_price}\nMaker fees: {MAKER_FEES}\nTaker fees: {TAKER_FEES}\n--Spread: {spread}--\n')
