// A blockchain comprises of several blocks that are joined to each other.
// The chaining of blocks takes place such that if one block is tampered with, the rest of the chain becomes invalid.

import hashlib
import time

class Block:

    def __init__(self, index, proof_no, prev_hash, data, timestamp=None):
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp or time.time()

#property
#Calculate_hash, will generate the hash of the blocks using the above values.
#The SHA-256 module is imported into the project to assist in obtaining the hashes of the blocks.

    def calculate_hash(self):
        block_of_string = "{}{}{}{}{}".format(self.index, self.proof_no, self.prev_hash, self.data,self.timestamp)

        return hashlib.sha256(block_of_string.encode()).hexdigest()

    
    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof_no, self.prev_hash, self.data,self.timestamp)

"""self—this refers to the instance of the Block class, making it possible to access the methods and attributes associated with the class;

index—this keeps track of the position of the block within the blockchain;

proof_no—this is the number produced during the creation of a new block (called mining);

prev_hash—this refers to the hash of the previous block within the chain;

data—this gives a record of all transactions completed, such as the quantity bought;

timestamp—this places a timestamp for the transactions.
"""               

class BlockChain:

    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.construct_genesis()
"""
self.chain—this variable keeps all blocks;
self.current_data—this variable keeps all the completed transactions in the block;
self.construct_genesis()—this method will take care of constructing the initial block.
"""

def construct_genesis(self):
        self.construct_block(proof_no=0, prev_hash=0)

"""
The blockchain requires a construct_genesis method to build the initial block in the chain. In the blockchain convention, this block is special because it symbolizes the start of the blockchain.

In this case, let’s construct it by simply passing some default values to the construct_block method.

I gave both proof_no and prev_hash a value of zero, although you can provide any value you want.
"""

def construct_block(self, proof_no, prev_hash):
        block = Block(
            index=len(self.chain),
            proof_no=proof_no,
            prev_hash=prev_hash,
            data=self.current_data)
        self.current_data = []

        self.chain.append(block)
        return block

"""
index—this represents the length of the blockchain;

proof_nor & prev_hash—the caller method passes them;

data—this contains a record of all the transactions that are not included in any block on the node;

self.current_data—this is used to reset the transaction list on the node. If a block has been constructed and the transactions allocated to it, the list is reset to ensure that future transactions are added into this list. And, this process will take place continuously;

self.chain.append()—this method joins newly constructed blocks to the chain;

return—lastly, a constructed block object is returned
"""

// Staticmethod
// The check_validity method is important in assessing the integrity of the blockchain and ensuring anomalies are absent.
// This check_validity method uses if statements to check whether the hash of every block is correct.

def check_validity(block, prev_block):
        if prev_block.index + 1 != block.index:
            return False

        elif prev_block.calculate_hash != block.prev_hash:
            return False

        elif not BlockChain.verifying_proof(block.proof_no,
                                            prev_block.proof_no):
            return False

        elif block.timestamp <= prev_block.timestamp:
            return False

        return True

// The new_data method is used for adding the data of transactions to a block. It’s a very simple method: it accepts three parameters and append the transaction data to self.current_data list
//Once the transaction data has been added to the list, the index of the next block to be created is returned

def new_data(self, sender, recipient, quantity):
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'quantity': quantity})
        return True
   
//Staticmethod
def proof_of_work(last_proof):

// Proof of work is a concept that prevents the blockchain from abuse. Simply, its objective is to identify a number that solves a problem after a certain amount of computing work is done.
// If the difficulty level of identifying the number is high, it discourages spamming and tampering with the blockchain.


        '''this simple algorithm identifies a number f' such that hash(ff') contain 4 leading zeroes
         f is the previous f'
         f' is the new proof
        '''
        proof_no = 0
        while BlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1

        return proof_no

//Staticmethod
def verifying_proof(last_proof, proof):
        //verifying the proof: does hash(last_proof, proof) contain 4 leading zeroes?

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

//Property
//The latest_block method is a helper method that assists in obtaining the last block in the blockchain.
//Remember that the last block is actually the current block in the chain.

def latest_block(self):
        return self.chain[-1]

def block_mining(self, details_miner):

    
        self.new_data(
            sender="0",  #it implies that this node has created a new block
            receiver=details_miner,
            quantity=1)  #creating a new block (or identifying the proof number) is awarded with 1

        
        last_block = self.latest_block

        last_proof_no = last_block.proof_no
        proof_no = self.proof_of_work(last_proof_no)

        last_hash = last_block.calculate_hash
        block = self.construct_block(proof_no, last_hash)

        return vars(block)

def create_node(self, address):
        self.nodes.add(address)
        return True

    
//Staticmethod
def obtain_block_object(block_data):
        //obtains block object from the block data

        return Block(
            block_data['index'],
            block_data['proof_no'],
            block_data['prev_hash'],
            block_data['data'],
            timestamp=block_data['timestamp'])
