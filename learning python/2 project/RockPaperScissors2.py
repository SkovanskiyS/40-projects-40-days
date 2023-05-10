import random

list = ['Камень', 'Ножницы', 'Бумага']
user_input = int(input('Камень: 1\nНожницы: 2\nБумага: 3\nВыберите один из вариантов: '))  # 3
user = ''
pc = list[random.randint(0, 2)]
# support in Python 3.10>
match user_input:
    case 1:
        user += 'Камень'
    case 2:
        user += 'Ножницы'
    case 3:
        user += 'Бумага'
# check for winner
if user == "Камень" and pc == "Ножницы" or user == "Бумага" and pc == "Камень" or user == "Ножницы" and pc == "Бумага":
    print("Вы выиграли")
elif user == pc:
    print('Ничья!')
else:
    print("Вы проиграли")
