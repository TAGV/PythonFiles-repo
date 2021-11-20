import web3
from web3 import Web3

with open('/home/myubuntu/PycharmProjects/secretfile.txt','r') as sf:
    rd = sf.readline()      # This reads the url endpoint

    # Infura url for Ethereum endpoint
    w3 = Web3(Web3.HTTPProvider(rd))
    print(w3.isConnected())
    print(w3.eth.blockNumber)
    print(w3.eth.get_block('latest'))








