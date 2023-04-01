
# СПИСОК

# Input count of numbers and the numbers, 
# after that - add all numbers in the list

# some_list = []
# count = int (input ('Input some numbers: '))
# for i in range (count): # 0 , 1, 2, 3, 4
#     number = int(input ())
#     some_list.append (number)
# print(some_list)

# some_list = [int(input ()) for i in range(int(input ('Input some numbers: ')))]
# print(some_list)

# # and find the max element

# max = some_list[0]
# for ind in range (0, len (some_list)):
#     if max < some_list[ind]:
#         max = some_list[ind]
# print (max)


# # КОРТЕЖИ - неизменяемые списки
# # the list become tuple
# some_tuple = tuple (some_list)
# print (some_tuple)


# # МНОЖЕСТВО - уникальные элементы, нет индексов у элемента, можно менять, высокая скорость работы
# some_set = set (some_tuple)
# print (some_set)

# # ЗАМОРОЖЕННОЕ МНОЖЕСТВО
# some_frozenset = frozenset (some_tuple)
# print (some_frozenset)

# Create the list from 1 to 1 million
# Check speed of working with lists and sets

# import time
# import random

# some_list = []
# for i in range(1, 10 ** 6 + 1):
#     some_list.append(random.randint(1, 10 ** 6))
# n = int(input())   
# start = time.perf_counter()
# print (n in some_list)
# end = time.perf_counter()
# print (end - start)

# some_set = set(some_list)
# start = time.perf_counter()
# print (n in some_set)
# end = time.perf_counter()
# print (end - start)


# СЛОВАРИ - ищет по ключам, уникальные ключи (если нет - используется последний)
# ключ - неизменяемый тип данных 
# Неизменяемые - (int, float, str, bool, tuple, frozenset)
# Изменяемые - (list, set, dict)


# some_dict = {'apple': 'яблоко', 'orange': 'апельсин', 'grape': 'виноград'}
# print (some_dict['apple'])
# print (some_dict)   
# some_dict['banana'] = 'банан' 
# print (some_dict)   

# for keys in some_dict:
#     print(keys)

# for value in some_dict.values():
#     print(value)



# TASKS

# There is a list. Try to count the number of every unique digits

# import random

# some_list = []
# count = int (input ('Input some numbers: '))
# for i in range (count): # 0 , 1, 2, 3, 4
#     number = int(random.randint(1, 5))
#     some_list.append (number)
# print(some_list)

# some_dict = {}
# for el in some_list:
#     some_dict[el] = some_dict.get(el, 0) + 1
# print (some_dict)



# There is a list. Try to count the number of unique digits

# import random

# some_list = []
# count = int (input ('Input some numbers: '))
# for i in range (count): # 0 , 1, 2, 3, 4
#     number = int(random.randint(1, 5))
#     some_list.append (number)
# print(some_list)

# some_set = set (some_list)
# print (len (some_set))



# There is a set N and number K. 
# Try to move all elements of N on K steps

# import random

# some_list = []
# count = int (input ('Input some numbers: '))
# for i in range (count): # 0 , 1, 2, 3, 4
#     number = int(random.randint(1, 5))
#     some_list.append (number)
# print(some_list)

# k = int (input('Number of steps = '))
# some_list_2 = some_list[k:] + some_list[:k]
# print(some_list_2)


# Write a programm wich output all unique elements from dictionary

# some_dict = {0: 1, 1: 1, 1: 2, 2: 3, 3: 5}
# for value in some_dict.values():
#     if list(some_dict.values()).count(value) ==1:
#         print(value)


# Write a programm that counts the number of elements, if the current element is larger then the last one
# import random
# some_list = []
# count = int (input ('Input some numbers: '))
# for i in range (count): # 0 , 1, 2, 3, 4
#     number = int(random.randint(1, 5))
#     some_list.append (number)
# print(some_list)

# a = some_list[0]
# cnt = 0
# for ind in range(1, len (some_list)):
#     if a < some_list[ind]: cnt += 1
#     # print (cnt)
#     a = some_list[ind]
#     # print (a)
# print (cnt)

# cnt = 0
# for ind in range(0, len (some_list) - 1):
#     if some_list [ind + 1] > some_list[ind]:
#         cnt+=1
# print (cnt)











# HOMETASK__3

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# import random
# some_list = []
# count = int (input ('Input some numbers: '))
# x = int(input('X = '))
# cnt = 0
# for i in range (count): # 0 , 1, 2, 3, 4
#     number = int(random.randint(1, 5))
#     some_list.append (number)
#     if some_list[i] == x: cnt +=1
# print(f'List: {some_list}')
# print(f'Count of x = {cnt}')



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5


# import random
# some_list = []
# count = int (input ('Input some numbers: '))
# for i in range (count): # 0 , 1, 2, 3, 4
#     number = int(random.randint(1, 5))
#     some_list.append (number)
# print(f'List: {some_list}')

# nmb = int (input('Number = '))
# fnd = some_list[0]
# for ind in range(1, len(some_list)-1):
#     if (fnd - nmb) ** 2 > (some_list[ind] - nmb) ** 2:
#         # print (f'{(fnd - nmb) ** 2} > {(some_list[ind] - nmb) ** 2}')
#         fnd = some_list[ind]
#         # print (f'fnd = {fnd}')
#     # else:
#         # print (f'{(fnd - nmb) ** 2} <= {(some_list[ind] - nmb) ** 2}')
# print (f'Funding number = {fnd}')


# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12

# scr = 0
# wrd_list = []
# wrd_list = input ('Input the word >>')
# for ind in range (0, len(wrd_list)):
#     if wrd_list[ind] in ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'): scr += 1
#     elif wrd_list[ind] in ('D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'): scr += 2
#     elif wrd_list[ind] in ('B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'): scr += 3
#     elif wrd_list[ind] in ('F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'): scr += 4
#     elif wrd_list[ind] in ('K', 'Ж', 'З', 'Х', 'Ц', 'Ч'): scr += 5
#     elif wrd_list[ind] in ('J', 'X', 'Ш', 'Э', 'Ю'): scr += 8
#     elif wrd_list[ind] in ('Q', 'Z', 'Ф', 'Щ', 'Ъ'): scr += 8
# print (scr)


# HOMETASK__4

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


# import random

# list_1 = []
# count_1 = int (input ('Input some numbers: '))
# for i in range (count_1): # 0 , 1, 2, 3, 4
#     number = int(random.randint(1, 10))
#     list_1.append (number)
# print(f'List: {list_1}')

# list_2 = []
# count_2 = int (input ('Input some numbers: '))
# for j in range (count_2): # 0 , 1, 2, 3, 4
#     number = int(random.randint(1, 10))
#     list_2.append (number)
# print(f'List: {list_2}')

# some_set = set (list_1 + list_2)
# some_list = list (some_set)

# for k in range (0, len(some_list)):   
#     for ind in range(0, len(some_list)-k-1):
#         if some_list[ind] > some_list[ind+1]:
#             chg = some_list[ind]
#             some_list[ind] = some_list[ind+1]
#             some_list[ind+1] = chg
# print (some_list)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random

some_list = []
count = int (input ('Input numbers of bushes: '))
for i in range (count): # 0 , 1, 2, 3, 4
    number = int(random.randint(1, 100))
    some_list.append (number)
print(f'Number of berries on bushes: {some_list}')

max_sum = 0
max_ind = 0
for ind in range(0, len(some_list)-1):
    if ind == 0:
        sum = some_list[ind] + some_list[len(some_list)-1] + some_list[ind+1]
    elif ind == len(some_list):
        sum = some_list[ind] + some_list[ind-1] + some_list[0]
    else:
        sum = some_list[ind] + some_list[ind-1] + some_list[ind+1]
    # print (sum)
    if sum > max_sum:
        max_sum = sum
        max_ind = ind
print (f'Max berries = {max_sum} from {max_ind+1} position')

