blockchain = []

def get_last_blockchain_value():
    if len(blockchain) > 0:
        return blockchain[-1]
    else:
        return [1]


def add_value(value):
    blockchain.append([get_last_blockchain_value(), value])


def print_entire_blockchain():
    print(blockchain)


def print_block(index = 0):
    if len(blockchain) > 0 and index <= len(blockchain)-1:
        if index < 0:
            print('ERROR: this function doesn\'t handle negative index')
        else:
            print(blockchain[index])
    elif index > len(blockchain)-1:
        print('ERROR: index is out of range')


def get_user_input():
    amount = float(input('Enter an amount please: '))
    add_value(amount)


get_user_input()
get_user_input()
get_user_input()



print_entire_blockchain()
print_block(0)

print_block(4)

print_block(-1)