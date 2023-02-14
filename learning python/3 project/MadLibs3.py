import random
text = """Привет как дела """
a = 0
last_txt = ''
with open('badWords.txt', encoding='utf-8') as file:
    for i in file:
        last_txt = i.replace(',', '')
        for j in text:
            if j == ' ':
                a += 1
for i in text:
    print(i.replace(' '," "+random.choice(last_txt.split(' '))+" "),end= '')