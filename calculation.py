

#Commission on purchase
MAKER_FEES=0.001

#Commission on sale
TAKER_FEES=0.001

#The commission for transfer in the network is None, because CCXT does not provide the corresponding data
transfer_fee_by_network = None

#Calculate a spread
def spread_calculation(buy_price, sell_price):
    if buy_price < sell_price:
        spread = ((sell_price - buy_price)/sell_price)*100
    else:
        spread = ((buy_price - sell_price) / sell_price) * 100

    if spread > MAKER_FEES:
        return spread-MAKER_FEES