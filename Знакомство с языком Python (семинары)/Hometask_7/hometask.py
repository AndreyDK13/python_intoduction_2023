# Задача 34:  
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке
# используйте split()
# Пример:

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


def check (str):
    vowels = ('аеёиоуэюя')
    # print (vowels)
    # str = input('Input some frase: ')
    lines = (str.split(" "))
    # print (lines)
    counter = []
    for word in lines:
        cnt = 0
        for ltr in word:
            if ltr in vowels:
                cnt+=1
        counter.append(cnt)
    # print (counter)       
    if counter[0] == counter[1]:
        return ("пара-ра-рам рам-пам-папам па-ра-па-да")
    else:
        return ("Парам пам-пам ")

print(check(input('Input some frase: ')))


# for k in range(1, len(count)):    
#     if count[i] == count[i-1]:
#         print ("пара-ра-рам рам-пам-папам па-ра-па-да")
#     else:
#         print ("Парам пам-пам ")


# Задача 36.Создайте список из случайных чисел. 
# Найдите количество различных элементов в нем.

import random

def rand_list(count):
    some_list = [random.randint(1, 10) for i in range(count)] 
    return some_list

some_list = rand_list(int(input('Input some numbers: ')))
print (some_list)
distinct_list = list(set(some_list))
print(len(distinct_list))


