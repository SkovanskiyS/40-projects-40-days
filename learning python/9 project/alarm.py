import math
import time
import tkinter as tk
import datetime
import string

display = tk.Tk()

display.title('hello world')

rightOne = '3.1455926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
shouldBeChecked = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
limit = input('Enter the limit length of the number PI')
def filter(usersPI):
    clean_text = ''.join(char for char in usersPI if char not in string.punctuation).replace(' ', '').replace('\t', '')
    return clean_text

def check(userNumber):
    userPi = filter(userNumber)
    for i, j in enumerate(rightOne):
        if j != shouldBeChecked[i]:
            print(f'Неверно: computer {j} and user\'s {shouldBeChecked[i]}')
        else:
            print(f'Верно: computer {j} and user\'s {shouldBeChecked[i]}')
print(math.pi)