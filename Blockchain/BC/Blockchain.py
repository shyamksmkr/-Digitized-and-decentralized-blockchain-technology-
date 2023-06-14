from hashlib import sha256
import json
import time
#import Block
#from BC import Block
#from Block import *
import pickle
from datetime import datetime

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

class Blockchain:
    # difficulty of our PoW algorithm
    difficulty = 2

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()
        self.peer = []
        self.translist = []

    def create_genesis_block(self):
        """
        A function to generate genesis block and appends it to
        the chain. The block has index 0, previous_hash as 0, and
        a valid hash.
        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        """
        A function that adds the block to the chain after verification.
        Verification includes:
        * Checking if the proof is valid.
        * The previous_hash referred in the block and the hash of latest block
          in the chain match.
        """
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        #print("main "+str(block.hash))
        self.chain.append(block)
        return True

    def is_valid_proof(self, block, block_hash):
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        #print("compare "+str(block_hash == block.compute_hash())+" "+block.compute_hash()+" "+str(block_hash.startswith('0' * Blockchain.difficulty)))
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    def proof_of_work(self, block):
        """
        Function that tries different values of nonce to get a hash
        that satisfies our difficulty criteria.
        """
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def addPeer(self, peer_details):
        self.peer.append(peer_details)   
	
    def addTransaction(self,trans_details):
        self.translist.append(trans_details)

    def mine(self):
        """
        This function serves as an interface to add the pending
        transactions to the blockchain by adding them to the block
        and figuring out Proof Of Work.
        """
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)

        self.unconfirmed_transactions = []
        return new_block.index
    
    def save_object(obj, filename):
        with open(filename, 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

if __name__== "__main__":
    blockchain = Blockchain()
    #count = 'kaleem.mmd@gmail.com'
    #x = count+',3000'
    #blockchain.addPeer(x)
    #count = 'saleem.mmd@gmail.com'
    #x = count+',3000'
    #blockchain.addPeer(x)
    
    #for i in range(len(blockchain.peer)):
    #    blockchain.add_new_transaction(blockchain.peer[i])
    #    blockchain.mine()
    #blockchain.peer.clear()    
    #blockchain.peer.remove(x)
    #print(blockchain.peer)
    #blockchain.save_object(blockchain,'BC_DB.txt')
    with open('BC_DB.txt', 'wb') as output:
        pickle.dump(blockchain, output, pickle.HIGHEST_PROTOCOL)
        

    with open('BC_DB.txt', 'rb') as input:
         blockchain = pickle.load(input)
    for i in range(len(blockchain.chain)):
        b = blockchain.chain[i]
        print(str(b.transactions)+" "+str(b.previous_hash)+" "+str(b.index)+" "+str(b.hash)+" "+str(datetime.fromtimestamp(b.timestamp)))


    
