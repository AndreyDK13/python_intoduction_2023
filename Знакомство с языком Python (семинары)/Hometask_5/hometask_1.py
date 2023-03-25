# Задача 1
# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.


def math (task):
    # task = list(input ("Input the task  >>  "))
    result = int(task [0])
    for i in range (1, len(task)-1):
        if task [i] == '+':
            result = result + int(task [i+1])
        elif task [i] == '-':
            result = result - int(task [i+1])
    return result
print(math(list(input ("Input the task  >>  "))))


# Задача 2
# Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки.
# Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)

txt = list(input("Text: "))
result = ""
for i in range (0, len(txt)):
    if i == len(txt)-1:
        result = result + txt [i]
        print (result)    
    elif txt [i] != ' ':
        result = result + txt [i]
    else:
        print (result)
        result = ''


