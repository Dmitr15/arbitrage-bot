from pybit.unified_trading import HTTP
import pprint
session = HTTP(
    testnet=False,
    api_key="YOUR_API_KEY",
    api_secret="YOUR_API_SECRET",
)
dict_a = session.get_coin_info(coin="USDT",)
print(dict_a)
a=dict_a['result'].get('rows')

b = a[0]['chains']
pprint.pprint(b)

for i in b:
    if i['chainWithdraw'] != str(0):
        print('chainType: ', i['chainType'])
        print('withdrawFee: ', i['withdrawFee'])
        print()