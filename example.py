from blockchain import Blockchain

# transactions to add to chain
block_one_transactions = {"sender":"David", "receiver": "Justin", "amount":"50"}
block_two_transactions = {"sender": "John", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Chanelle", "amount":"35"}
# fruadulent transaction
fake_transactions = {"sender": "John", "receiver":"Cole, James", "amount":"25"}

# create instance of Blockchain and print blocks contained after adding them
local_blockchain = Blockchain()
local_blockchain.print_blocks()
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()
print("***** INITIAL BLOCKS ADDED *****")

# modifiying a block with the fruadulent transaction and checking if the chain is valid
local_blockchain.chain[2].transactions = fake_transactions
local_blockchain.validate_chain()