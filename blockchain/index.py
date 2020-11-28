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


def add_user_amount():
    amount = float(input('Enter new block value: '))
    add_value(amount)

def get_block_to_print():
    index = input('What index would you like to print: ')
    if index.isnumeric():
        print_block(int(index))
    else:
        print('index must be numeric')
        get_block_to_print()
    

def get_user_input():
    return input('Enter your choice: ')
    

def print_each_block():
    for block in blockchain:
        print(block)

def run_program():
    while True:
        print('what would you like to do?')
        print('1: add a new block to the chain')
        print('2: print the blockchain')
        print('3: print a value from the blockchain')
        print('4: print each value from the blockchain')
        print('or quit the program')
        user_choice = get_user_input()
        if user_choice == '1':
            add_user_amount()
        elif user_choice == '2':
            print_entire_blockchain()
        elif user_choice == '3':
            get_block_to_print()
        elif user_choice == '4':
            print_each_block()
        else:
            break

run_program()

print('bye')