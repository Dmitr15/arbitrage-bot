import requests

response = requests.get("https://api.bitget.com/api/spot/v1/public/currencies")

result = response.json()
#res = response.json()
#print(result)

data = result['data']

#data['coinDisplayName']
print(data[0]['coinDisplayName'])
print()
print(data[1]['chains'])
chainName = data[1]['chains'][0]['chain']

isWithdrawable = data[1]['chains'][0]['withdrawable']
print(isWithdrawable)

withdrawFee = data[1]['chains'][0]['withdrawFee']
print(withdrawFee)
print()

for d in data:
   print(d['coinDisplayName'])
  #continue
   for i in d:
       print(d[i]['chains'][0]['chain'])


test = result['data'][1]['chains'][0]['chain']

print(test)