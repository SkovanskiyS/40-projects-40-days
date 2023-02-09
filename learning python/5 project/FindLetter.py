import random
import re
random_text = ''
with open('badWords.txt', encoding='utf-8') as file:
    bad_words = file.readline().replace(',', '').split(' ')
    random_text += bad_words[random.randint(0,len(bad_words)-1)]
count_of_tries = 0
# cover the text
result = ''
for i in random_text:
    result += i.replace(i, '_')
resultList = list(result)
print(str(resultList))
print(f"Сам текст: {random_text}")
for i in range(1, 50):
    user_guess = input(f"\nВсего слов: {len(random_text)}\nВаша {i} попытка: \n")
    index_found = []
    for j, name in enumerate(random_text):
        if name == user_guess:
            resultList.insert(j, name)
            resultList.pop(j + 1)
    print(resultList)
    if resultList==list(random_text):
        print("Поздравляю!!!\nТы угадал все слова!")
        break