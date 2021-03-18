from Block import Block
blockchain =[] # this is where transcations go
#genesis block is the first block in blockchain
genesis_block=Block("Chancellor on the brink...", ["Satoshi sent 1BTC TO saugat",
'Maria sent 5BTC to jenny', "Satoshi sent 5BTC to Hal Finney"])
#gensis doesnt have rpeviosu block so we include that msg
second_block=Block(genesis_block.block_hash,["Ivan sent 5btc to liz",
"joghn sent 5 btc to jenny"])
third_block=Block(second_block.block_hash,["Saugat sent 5btc to liz",
"Joe sent 5 btc to Jimmy"])
print("----------------Block Hash: Gensis Block------------")
print(genesis_block.block_hash)
print("--------------Block Hash: Second Block---------------")
print(second_block.block_hash)
print("--------------Block Hash: Third Block---------------")
print(third_block.block_hash)

