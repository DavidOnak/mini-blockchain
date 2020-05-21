from block import Block

# Author: David Onak

# This class represents a chain of blocks, using proof-of-work and a validate chain method 
# to prevent fruadulant transactions
class Blockchain:
    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.genesis_block()

    # Creates a genesis block (first block in chain)
    def genesis_block(self):
        transactions = []
        genesis_block = Block(transactions, "0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)

    # adds a block to the chain
    def add_block(self, transactions):
        previous_hash = (self.chain[len(self.chain)-1]).hash
        new_block = Block(transactions, previous_hash)
        new_block.generate_hash()
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)

    # prints all block contained within chain
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()

    # validates a chain based on if it has been modified by checking hashs 
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash is not current.generate_hash():
                print("Current hash does not equal generated hash")
                return False
            elif current.previous_hash is not previous.generate_hash():
                print("Previous block's hash got changed")
                return False
        return True
 
    # a difficult calucation by guessing to prevent fruadulent behavour
    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:2] != "0"*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof