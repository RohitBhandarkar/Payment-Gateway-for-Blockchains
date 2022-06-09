from web3 import Web3
import time
ganache_url = "HTTP://127.0.0.1:7545" #Local port in which Ganache is running or any URL to connect to blockchains
web3 = Web3(Web3.HTTPProvider(ganache_url))
#accepts information
SenderAccount = input("Enter your Account Number: ")
ReceiverAccount = input("Enter the receivers Account Number: ")
SenderPrivateKey = input("Enter your private key: ")
amount = float(input("Enter the amount to be transferred: "))
time.sleep(5)
#transaction
nonce = web3.eth.getTransactionCount(SenderAccount)
tx = {                                   #Transaction Details
    'nonce': nonce,
    'to': ReceiverAccount,
    'value': web3.toWei(amount, 'ether'),
    'gas': 200000,
    'gasPrice': web3.toWei(50, 'gwei')
}
signed_tx = web3.eth.account.signTransaction(tx, SenderPrivateKey) #Signing the transaction
tx_hash = web3.toHex(web3.eth.sendRawTransaction(signed_tx.rawTransaction)) #Transaction
print("succesfully transfered {} ether.\nHash: {}".format(amount, tx_hash))

#block information
bkNumber = web3.eth.blockNumber
block = web3.eth.getBlock(bkNumber)
#print(block)
parentHash = web3.toHex(block['parentHash'])
miner = block['miner']
diff = block['difficulty']
size = web3.fromWei(block['size'], 'ether')
gasLim = web3.fromWei(block['gasLimit'], 'ether')
gasUse = web3.fromWei(block['gasUsed'], 'ether')
balance = web3.eth.getBalance(SenderAccount)
print("Block Number: {}".format(bkNumber))
print("Amount: {}".format(amount))
print("Parent Hash: {}".format(parentHash))
print("Miner: {}".format(miner))
print("Difficulty: {}".format(diff))
print("Gas Limit: {}".format(gasLim))
print("Gas Used: {}".format(gasUse))
print("Account Balance: {}".format(web3.fromWei(balance, 'ether')))
