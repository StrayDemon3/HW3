# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

while True:
    try:
        num = abs(int(input('Введите число: ')))
        break
    except:
        print('Давайте цифрами!')

my_list = []

while num > 1:
    if num % 2 == 1:
        my_list.append(1)
    else:
        my_list.append(0)
    num //= 2
my_list.append(num)
print(my_list)

my_list.reverse()
print(my_list)
