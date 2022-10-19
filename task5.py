lst_1 = input('введите значения:\n').split()
print(lst_1, type(lst_1), id(lst_1))
a = 0 #вводим переменную(a) счетчик итераций
for i in range(len(lst_1)): #i=значение=длина списка
    b = i - a #переменная(b)-элемент в списке(lst_1)
    if lst_1[b] == '0': #сравниваем с (0)
        lst_1.append(lst_1.pop(b))#если b==0,то удаляем индекс(b)-lst_1.pop(b)
                 #одновременно добавляя его в конец списка(lst_1.append(b,т.е(0))
        a += 1
print(lst_1,type(lst_1),id(lst_1))
print(a,i)