# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = []

while True:
    try:
        size = abs(int(input('Введите размер списка: ')))
        break
    except:
        print('Размер списка должен быть целым числом!')

for i in range(size):
    while True:
        try:
            my_list.append(int(input(f'Введите {i+1} число для списка: ')))
            break
        except:
            print(f'Введите, как положено {i+1} число для списка: ')

print(my_list)

new_list = []

if size % 2 == 0:
    for i in range(int(size/2)):
        new_list.append(my_list[i]*(my_list[(i + 1)*(-1)]))
else:
    for i in range(int(size/2) + 1):
        new_list.append(my_list[i]*(my_list[(i + 1)*(-1)]))


print(new_list)