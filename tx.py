import requests
import json
hash = input("Enter Txid: ")

def func():
    req = requests.get("https://chain.so/api/v2/tx/BTC/"+str(hash))
    hex = req.json()['data']['tx_hex']
    print(hex)
    #print("\n"str(hex))
if hash == "":
    print("Oops You may Not Enter TXiD")
else:
    func()
