# mini-blockchain
The following repository contains a block and blockchain class that resembles blockchain used in cyptocurrency. However, this blockchain will run only on the local machine when actual blockchain applications operate on multiple computers in a decentralized manner. Allowing for a substancially higher level of security within the blockchain.

# What is a Blockchain?
A blockchain is similar to a permanent book of records that keeps a log of all transactions that have taken place in chronological order.

In an example of banking, instead of having a centrial bank to verify a transaction from one person to another, the blockchain relies on a public network of computers to verify the transaction. So the blockchain is an accurate and permanent record of all transactions amongst the members in its network in this case. 

Each participant is a computer that owns a copy of the blockchain. So in order for a new block to be added, 51% of all of the participants in the blockchain network must verify that the new block is not fraudulent. Once a block has been verified as a valid transaction, it is added to each participant’s copy of the blockchain. 

# Blocks
A block contains transaction data and other important details related to the creation of that block, such as the time when it was created and other unique information. Although this data the block contains may vary depending on the application, there will always be a timestamp or something equvalent stored.

A block will also always contain a unique hash produced by combining all the contents within the block itself and the hash of the previous block (previous hash). This reference to the prior block is how blocks chain to one another. 

The first block is called the Genesis block and since there is no previous block, the previous hash is hard-coded onto this block with a value usually of zero.

# Providing Security with Hashing
If any block in the chain is tampered with, the unique hash for that block gets changed. Therefore, the next block's previous hash will not match up with the actual hash of the prevous block. This breaks the link of the chain and makes the copy of the blockchain invalid.

However, it is possible to modify every block after to change each hash and fix the link. To prevent someone from doing this, a proof-of-work is implemented.

# Proof-of-Work
A proof-of-work makes it difficult for participants to modify blocks by re-calculating hashes and relies on bulletproof cryptography to verify transactions. It will normally take the form of a computationally difficult math problem, which means it takes a lot of time even for the computer to solve the problem. 

Instead of randomly being chosen to broadcast their unconfirmed block, a special group of participants, also known as miners, now need to solve a problem in order to be eligible to broadcast their block. The problem takes the form of a guessing game that involves the use of hashing. Miners first guess a nonce value, which is then combined with the contents of the block. They repeat this process until the desired hash is generated.

The first miner to produce a proof broadcasts their unconfirmed block together with the correct nonce value. The rest of the network then verifies the calculation. If the majority of the participants agree, the proof-of-work for the block is now complete and the block has now been confirmed. The network then moves on to work on the next block.

The blockchain participants always consider the longest chain to be the correct one. If someone is able to create the longest chain of blocks, the network is forced to accept the new chain.

So if someone tries to tamper with a block, they need to solve a different proof-of-work for each block after. Also new blocks can be added at a faster rate then the blocks can be tampered with making it impossible to make a tampered copy of the chain that is valid.
