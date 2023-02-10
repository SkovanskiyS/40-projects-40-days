list_ = []
for i in range(1, 100 + 1):
    list_.append(i)
low, high = 0, len(list_)
a = 0
print('Загадайте число ')
while low <= high:
    middle = (high + low) // 2
    user_number = input(f'Твое число это: {middle}?\nбольше или меньше: ')
    if user_number.lower() == 'да' or user_number.lower() == 'yes':
        print(f'Я угадал!')
        a += 1
        break
    elif user_number == "больше":
        low = middle + 1
    elif user_number == 'меньше':
        high = middle - 1
if a < 1:
    print('Ты врешь')
