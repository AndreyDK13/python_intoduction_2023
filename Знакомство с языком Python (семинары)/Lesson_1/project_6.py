
# 3. В некоторой школе решили набрать 
# три новых математических класса и оборудовать 
# кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, которое нужно приобрести для них.


a = int (input ("Введите количество в A классе >>"))
b = int (input ("Введите количество в B классе >>"))
c = int (input ("Введите количество в C классе >>"))

q = -(-(a)//2)-(-(b)//2)-(-(c)//2)

print (f'Всего парт нужно - {q}')