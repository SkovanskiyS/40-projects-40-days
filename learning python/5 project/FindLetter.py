import random

random_text = 'пидрила'
with open('badWords.txt', encoding='utf-8') as file:
    # random_text += file.readline()
    pass
# random_text = random_text.replace(',','').split(' ')[random.randint(0,len(random_text.split(' ')))]
count_of_tries = 0
# cover the text
cvr_text = ''
for i in random_text:
    cvr_text += i.replace(i, '_')
print(cvr_text)
for i in range(1, 5):
    user_guess = input(f"Ваша {i} попытка: ")
    count_of_found_letters = 0
    for j in random_text:
        if j == user_guess:
            count_of_found_letters += 1
            print(random_text.index(j))
            
