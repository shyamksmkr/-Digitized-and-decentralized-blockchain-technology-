from Block import *
from Blockchain import *
import pickle
blockchain = Blockchain()

with open('BC_DB.txt', 'wb') as output:
    pickle.dump(blockchain, output, pickle.HIGHEST_PROTOCOL)
        

with open('BC_DB.txt', 'rb') as input:
    blockchain = pickle.load(input)
for i in range(len(blockchain.chain)):
    b = blockchain.chain[i]
    print(str(b.transactions)+" "+str(b.previous_hash)+" "+str(b.index)+" "+str(b.hash)+" "+str(datetime.fromtimestamp(b.timestamp)))

