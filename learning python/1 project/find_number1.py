import random
random_num = random.randint(1, 10)
user_number = int(input('Введите число: '))
print(random_num)
while user_number != random_num:
    if random_num < user_number: print(f'Меньше...')
    else: print(f'Больше...')
    user_number = int(input('Введите число: '))
print(f'Вы угадали\nЧисло: {user_number}')

if random_num==int(input("Введите число: ")):
    print(f'You Won\nЧисло: {random_num}')
else:
    print(f'Try Again\nЧисло: {random_num}')

#without if/else and while

# import random
# def func(a):
#     L = []
#     number = random.randint(1, 10)
#     L.append(number)
#     num = int(input('введите число'))
#     L.append(num)
#     try:
#         a / bool(L[0] == L[1])
#         print('won')
#     except:
#         print('again')
#         func(number)
#     L.remove(num)
# func(3)


#primary

# import random
# random_num = random.randint(1, 10)
# user_number = int(input('Введите число: '))
# print(random_num)
# while user_number != random_num:
#     if random_num < user_number: print(f'Меньше...')
#     else: print(f'Больше...')
#     user_number = int(input('Введите число: '))
# print(f'Вы угадали\nЧисло: {user_number}')
#
# if random_num==int(input("Введите число: ")):
#     print(f'You Won\nЧисло: {random_num}')
# else:
#     print(f'Try Again\nЧисло: {random_num}')

