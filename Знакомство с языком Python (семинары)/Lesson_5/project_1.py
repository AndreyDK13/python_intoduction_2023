# Последованность Фибоначи

# ###### ЦИКЛОМ
# some_list = [0,1]
# num = int (input ('Desired element = '))
# for i in range (2, num): # 0 , 1, 2, 3, 4
#     number = some_list[i-1] + some_list[i-2]
#     some_list.append (number)
# print(some_list)
# print(some_list[num-1])


# ###### РЕКУРСИЯ
# def fib(n):
#     if n == 1:
#         return 0
#     elif n == 2 :
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print (fib (int (input ('Desired element = '))))
    

# Заменить все максимальные оценки на минимальные

# import random

# some_list = []
# count = int (input ('Input some numbers: '))
# for i in range (count): # 0 , 1, 2, 3, 4
#     number = int(random.randint(1, 5))
#     some_list.append (number)
# print(some_list)

# def chg ():
#     min = some_list[0]
#     max = some_list[0]
#     for i in range (len(some_list)):
#         if min > some_list[i]:
#             min  = some_list[i]
#         if max < some_list[i]:
#             max = some_list[i]
#     for j in range (0, len(some_list)):
#         if some_list[j] == max:
#            some_list[j] = min
#     return some_list
# print (chg())


# Проверка на простые числа

def simple(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return 'No'
    return 'Simple'
print (simple(int(input('Num = '))))
