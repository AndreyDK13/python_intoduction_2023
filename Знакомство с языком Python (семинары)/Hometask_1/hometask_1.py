# Задача 2: Найдите сумму цифр трехзначного числа.

# # *Пример:*
# # 123 -> 6 (1 + 2 + 3)
# # 100 -> 1 (1 + 0 + 0) |

num = input('Input a 3-digit number: ')
if len(num) != 3:
    print("Error")
else:
    sum = int(num[0])+int(num[1])+int(num[2])
    print(f"Summ of digits = {sum}")


# # # Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# # # Сколько журавликов сделал каждый ребенок, если известно,
# # # что Петя и Сережа сделали одинаковое количество журавликов,
# # # а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# # # *Пример:*
# # # 6 -> 1  4  1
# # # 24 -> 4  16  4
# # # 60 -> 10  40  10

cnt = int (input ('Input the count: '))
check = cnt % 6
share = cnt // 6
if check > 0:
    print (f"The Peter's number = {share}")
    print (f"The Sergey's number = {share}")
    print (f"The Katya's number = {share * 4}")
    print (f"The Unknow's number = {check}")
else:
    print (f"The Peter's number = {share}")
    print (f"The Sergey's number = {share}")
    print (f"The Katya's number = {share * 4}")

# # # Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# # # Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# # # Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# # # *Пример:*
# # # 385916 -> yes
# # # 123456 -> no

num = input('Input the ticket\'s number (6 digits): ')
if len(num) != 6:
    print('Uncorrect number')
else:
    a = int(num[0])+int(num[1])+int(num[2])
    b = int(num[3])+int(num[4])+int(num[5])
    if a == b:
        print('U r lucky man!')
    else:
        print('Try again!')


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n,m,k = int(input('Input n = ')), int(input('Input m = ')), int(input('Input k = '))
if k%n == 0 or k%m ==0:
    print ('Dividing is possible')
else:
    print ('It\'s not possible')
