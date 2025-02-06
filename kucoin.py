import requests
#from kucoin import *

#client = Market(url='https://api.kucoin.com')

response = requests.get("https://api.kucoin.com/api/v3/currencies/USDT")
res = response.json()
#pprint.pprint(res)
chains = res['data']['chains']
#pprint.pprint(chains[0])
#print(chains[0]['chainName'])
#print(chains[0]['withdrawalMinFee'])
#print(chains[0]['isWithdrawEnabled'])

for i in chains:
    if i['isWithdrawEnabled']:
        print('chainName: ', i['chainName'])
        print('withdrawalMinFee: ',i['withdrawalMinFee'])
        print('isWithdrawEnabled: ',i['isWithdrawEnabled'])
        print()