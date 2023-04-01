# sum function

# def summ (n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum

# a = int (input ('Input number'))
# print (summ (a))

# 

# def concat (*args):
#     res = ''
#     for i in args:
#         res += i
#     return res

# # print (concat ('a', 'b', 'c', 'v'))
# print (concat (1,5,9))

# fibonacci sequence

def fib (n):
    if n in (1,2):
        return 1
    return fib(n-1) + fib (n-2)

num = int(input('Number of elements = '))
list_1 = []
for i in range(1, num+1):
    list_1.append (fib(i))
print (list_1)
