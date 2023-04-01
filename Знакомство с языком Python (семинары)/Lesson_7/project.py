# Из списка случайных чисел найти локальный максимум

import random

def rand_list(count):
    some_list = [random.randint(1, 10) for i in range(count)] 
    return some_list

# def simple(some_list):
#     max_ind = -1
#     for i in range(1, len(some_list)-1):
#         if some_list[i] > some_list[i+1] and some_list[i] > some_list[i-1]:
#             max_ind = i
#     if max_ind!= -1:
#         return max_ind + 1
#     else:
#         return 'Not found'
    
def simple(some_list):
    for i in range(len(some_list)-2, 0, -1):
        if some_list[i] >= some_list[i+1] and some_list[i] >= some_list[i-1]:
            return (i + 1)
    else:
        return 'Not found'    

some_list = rand_list(int(input('Input some numbers: ')))
print (some_list)
print (simple(some_list))


# Из списка случайных чисел найти максимальнео количество повторов

def max_cnt(some_list):
    max = 0
    for i in range(0, len(some_list)):
        cnt = 0
        for j in range (0, len(some_list)):
            if some_list[i] == some_list[j]:
                cnt +=1
        if cnt > max:
            max = cnt
    return (max)
print (max_cnt(some_list))

def max_cnt_2(some_list):
    some_dict = {some_list[i]:0 for i in range(0, len(some_list))}
    for el in some_list:
        if el in some_dict:
            some_dict[el] +=1 
    return (max(some_dict.values()))
print (max_cnt_2(some_list))

# Найти второй максимум из списка случайных чисел


def sec_max(some_list):
    some_list_dist = list(set(some_list))
    for i in range(0, len(some_list_dist)):
        for j in range(0, len(some_list_dist)):
            if some_list_dist[i] > some_list_dist[j]:
                num = some_list_dist[i]
                some_list_dist[i] = some_list_dist[j]
                some_list_dist[j] = num
    return (some_list_dist[1])
print(sec_max(some_list))





