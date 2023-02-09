import random
import string
signs_number = string.digits
signs_abs = string.ascii_lowercase
signs_ABS = string.ascii_uppercase
signs = string.punctuation
while True:
    result = ''
    count_of_password = int(input('Введите кол-во строк: '))
    if count_of_password == 0:
        break
    else:
        r = ''
        add_number = bool(int(input('Добавить число?\nДА: 1\nНЕТ:0\n: ')))
        add_abs = bool(int(input('Добавить буквы?\nДА: 1\nНЕТ:0\n: ')))
        add_punct = bool(int(input('Добавить пунктуацию?\nДА: 1\nНЕТ:0\n: ')))
        if add_number:
            r += signs_number
        if add_abs:
            r += signs_abs + signs_ABS
        if add_punct:
            r += signs
        else:
            break
        for i in range(count_of_password):
            result += r[random.randint(0, len(r) - 1)]
    print(result)
print('You left the loop')
