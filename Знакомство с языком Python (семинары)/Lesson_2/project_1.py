# # По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# # (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while

# n = int (input ("Введите число >>"))

# f = 1
# while n > 0: 
#     f = n * f
#     n -= 1
# print (f)


# 11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое
# число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# n = int (input ("Введите искомое число >>"))

# f1 = 0
# f2 = 1
# i = 2
# while n > f2: 
#     # ftemp = f2
#     # f2 = f2 + f1
#     # f1 = ftemp
#     f2,f1 = f2+f1, f2
#     i+=1    
# if n==f2: 
#     k = i
# else: k = -1
# print (f'Номер искомого числа {k}')



# 13. 1. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю
# историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики
# за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который
# среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
#
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
#
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50



# n = int (input ("Input count of days >> "))

# c = 0
# cmax = 0
# for i in range(n):
#     t = int (input ("Input the tempreture >> "))
#     if t>0:
#         c += 1
#     else :
#         if cmax < c:
#             cmax = c
#         c = 0
# print (f'Count of days = {cmax}')



# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя
# нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке 
# каждое. Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.
    


n = int (input ("Input count of watermelon>> "))

wmax = 0
wmin = 30001
for i in range(n):
    w = int (input ("Input the weight >> "))
    if w > wmax:
        wmax = w
    if w < wmin:
        wmin = w
print (f'Max weight is {wmax} and min weight is {wmin}')
