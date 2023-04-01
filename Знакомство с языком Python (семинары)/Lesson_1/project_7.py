# # Напишите программу, которая вводит 
# с клавиатуры номер месяца и определяет, 
# сколько дней в этом месяце. 
# При вводе неверного номера месяца должно быть выведено сообщение 
# об ошибке. 
# Считается, что год невисокосный.

a = int (input ("Введите номер месяца >>"))

if a==1: print (f'31 days')
elif a==2: print (f'28 days')
elif a==3: print (f'31 days')
elif a==4: print (f'30 days')
elif a==5: print (f'31 days')
elif a==6: print (f'30 days')
elif a==7: print (f'31 days')
elif a==8: print (f'31 days')
elif a==9: print (f'30 days')
elif a==10: print (f'31 days')
elif a==11: print (f'30 days')
elif a==12: print (f'31 days')
else :print("ERROR")