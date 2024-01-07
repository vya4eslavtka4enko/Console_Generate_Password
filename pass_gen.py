import random
import sys

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


def pass_generator():
    password_length = int(input('Provide password length: '))
    use_uppercase = input('Use uppercase letters ? (y/n)')
    use_digit = input('Use digits ? (y/n)')
    use_special_characters = input('Use special characters ? (y/n)')   
    password_gen = []
    
    list_item = [punctuation,digits,ascii_uppercase]
    if use_uppercase == 'n':
        list_item.remove(ascii_uppercase)
    if use_digit == 'n':
        list_item.remove(digits)
    if use_special_characters == 'n':
        list_item.remove(punctuation)
    # print(list_item)
    for item in range(password_length-1):
        character_for_add = random.choice(list_item)
        element = random.choice(character_for_add)
        password_gen.append(element)      
    return ''.join(password_gen)

def main():
    print('---------------------------')
    print('-- Password generator --')
    print('Choose option:')
    print('1. Generate password')
    print('2. Exit the program')
    print('---------------------------')
    while True:
        user_choice = input('Make choice: ')
        if user_choice == '1':
            print(pass_generator())
            sys.exit()
        elif user_choice == '2':
            print('Bye! ')
            sys.exit()
        else:
            print('Please enter a correct value ')

main()