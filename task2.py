c = [c + d for c in 'ab' for d in 'bcd']#генерируем список
print(c)
c_1 = c[0::2]#делаем срез[старт:стоп:шаг],по умолчанию[0:длина обьекта:1]
#старт и стоп можно опустить,оставив только шаг
print(c_1)
c_2 = [b+ 'a' for b in '1234']#новый список
print(c_2)
c_2.pop(1);print(c_2)
#одной строкой удаляем a2(по индексу 1) из прошлого списка и печатаем его(список)
#если нужно было напечатать удаленный обьект тогда print(c_2.pop(1))
import copy
c_3 = copy.copy(c_2)#копируем список
c_3.append('2a');c_3.sort()#добавим элемент,можем отсортировать
print('получившийся список:\n',c_3,'\nисходный список:\n',c_2)
