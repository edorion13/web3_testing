from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = "0x101D3F89a7698bF2a9aaD418387d91A05cE2A0d9"
account_2 = "0x7ADcd38A968e263027014758F637D05f321e0f24"

private_key = '0xad891d30c011d52c2f9af0da44c2ce6abbc699aba7cdf9e7590f219d959bacbd'

nonce = web3.eth.get_transaction_count(account_1)
#build transaction
tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.to_wei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.to_wei('50', 'gwei')
}
# sign trasaction
signed_tx = web3.eth.account.sign_transaction(tx, private_key)
# send transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx)
# get trransaction has
print(tx_hash)

