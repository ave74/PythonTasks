# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений 
# в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

""" n=int(input ('введите количество элементов первого множества: '))
m=int(input ('введите количество элементов второго множества: '))

first=[]
second=[]
print('Введите элементы первого множества')
for i in range(n):
    first.append(int(input ()))
print('Введите элементы второго множества')
for i in range(m):
    second.append(int(input ()))

print('Первое множество:')
print(first)
print('Второе множество:')
print(second)

first.sort()
second.sort()

f=set(first)
s=set(second)

joint=f.union(s)
print('Объединённый список по возрастанию без повторений:')
print(joint) """


""" Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты 
высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте 
выросло a[i] ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего 
модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым 
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном списке урожайности грядки.
 """
""" import random

n=int(input('Введите количество кустов: '))
min=int(input('Введите минимальное количество ягод на кусте: '))
max=int(input('Введите максимальное количество ягод на кусте: '))
har=[]

for i in range(n):
    har.append(random.randrange(min, max))
print(har)

sbor=[]

for i in range(n-1):
    sbor.append(har[i-1]+har[i]+har[i+1])
sbor.append(har[n-2]+har[n-1]+har[0])

print(sbor)

max_sbor=sbor[0]
max_sbor_count=0

for i in range(n):
    if sbor[i]>max_sbor:
        max_sbor=sbor[i]
        max_sbor_count=i

print('Максимальное количество ягод',max_sbor,'штук сборщик может собрать находясь у куста номер',max_sbor_count+1)"""