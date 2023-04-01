# Задача 30:  
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def arith_progress (a1, diff, count):
    list = []
    for i in range (0, count):
        a = a1 + i * diff
        list.append(a)
    return (list)    

a1 = int (input ('First element = '))
diff = int (input ('Diff = '))
count = int (input ('Count of elements = '))
print (arith_progress (a1, diff, count))

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def rand_list(count):
    import random
    some_list = [random.randint(1, 10) for i in range(count)] 
    return some_list

def el_is_ok(min, max, some_list):
    print(some_list)
    el_is_ok = []
    for i in range(0, len(some_list)):
        if some_list[i] >= min and some_list[i] <= max:
            el_is_ok.append(i+1)
    return (el_is_ok)

some_list = rand_list(int (input ('Count of element = ')))
print (some_list)
min = int (input ('minimum = '))
max = int (input ('maximum = '))
list_ok = el_is_ok(min, max, some_list)
print (list_ok)

