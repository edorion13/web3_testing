from web3 import Web3
import json
from pathlib import Path

infura_url = "https://mainnet.infura.io/v3/af3e721adaf346bba5be451ac34d24e9"
web3 = Web3(Web3.HTTPProvider(infura_url))

#def getCoinLenderABI():
    #with open(Path('coinLenderABI.json')) as c:
        #coinLenderABI = json.load(c)
        #return coinLenderABI
    


#coinLenderAddress = "0xd9145CCE52D386f254917e481eB44e9943F39138"
usdcAddress = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
#coinLenderABI = getCoinLenderABI
usdcABI = '[{"constant":false,"inputs":[{"name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"newImplementation","type":"address"},{"name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[],"name":"implementation","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newAdmin","type":"address"}],"name":"changeAdmin","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"admin","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_implementation","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":false,"name":"previousAdmin","type":"address"},{"indexed":false,"name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"implementation","type":"address"}],"name":"Upgraded","type":"event"}]'

#coinLendercontract = web3.eth.contract(address=coinLenderAddress, abi=coinLenderABI)
usdcContract = web3.eth.contract(address=usdcAddress, abi=usdcABI)

print(usdcContract.functions.symbol().call())
