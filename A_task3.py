# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

my_list = []

for _ in range(10):
    index = random.randint(0, 3)
    my_list.append(round(random.uniform(0, 10), index))

print(my_list)

new_list = []

for i in range(len(my_list)):
    new_list.append(round(my_list[i] - int(my_list[i]), 3))
    if 0 in new_list:
        new_list.remove(0)

print(new_list)

maxim = new_list[0]
minim = new_list[0]

for i in new_list:
    if i > maxim:
        maxim = i
    if minim > i:
        minim = i

print(maxim)
print(minim)

print(f'Разница между максимальным и минимальным значением : {round(maxim - minim, 3)}')
