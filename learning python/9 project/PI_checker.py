import string
from mpmath import mp

userPI = input('Enter number PI which was done by yourself: ')


def filter(usersPI):
    clean_text = ''.join(char for char in usersPI if char not in string.punctuation).replace(' ', '').replace('\t', '')
    mp.dps = len(clean_text) + 1
    numberPI = ''.join(char2 for char2 in str(mp.pi) if char2 not in string.punctuation).replace(' ', '').replace('\t','')
    numberPI = numberPI[0:len(numberPI) - 1]
    return [clean_text, numberPI]


def check(userNumber):
    user_PI_and_original_PI = filter(userNumber)
    for index, originalPI in enumerate(user_PI_and_original_PI[1]):
        if originalPI != user_PI_and_original_PI[0][index]:
            print(f'Неверно: original {originalPI} and user\'s {user_PI_and_original_PI[0][index]}')
        else:
            print(f'Верно: original {originalPI} and user\'s {user_PI_and_original_PI[0][index]}')
    mp.dps = len(user_PI_and_original_PI[0]) + 1
    print(f'\n\tYour PI number: {user_PI_and_original_PI[0]}\n\tComputer PI number: {user_PI_and_original_PI[1]}')


check(userPI)
