list_1 = ['a','b','c']#список
print(list_1,type(list_1))
tup = tuple(list_1)#создание кортежа(tup) из списка(list)
print(tup,type(tup),'\n------------------------')

tup_1 = ('a','b','c')#кортеж
print(tup_1, type(tup_1))
list_2 = list(tup_1)#создание списка(list_2) из кортежа(tup_1)
print(list_2,type(list_2),'\n------------------------')

a,b,c = 'a',2,'python'#присвоение нескольких переменных одной строкой
print(a,b,c ,'\n------------------------')

tup_3 = ('a,b,c',)#кортеж из одного элемента
print(tup_3,len(tup_3),type(tup_3))
for i in tup_3:
    print(len(tup_3),len(tup_3)+1,len(tup_3)+2)