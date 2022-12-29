# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

while True:
    try:
        num = abs(int(input('Введите число: ')))
        break
    except:
        print('Давайте цифрами!')

def fib(num):
    my_list = [0, 1]
    for i in range(num - 1):
        my_list.append(my_list[i] + my_list[i + 1])
    return my_list


def neg_fib(num):
    my_list2 = [0, 1]
    for i in range(num - 1):
        my_list2.append(my_list2[i] - (my_list2[i + 1]))
    return my_list2
    
print(neg_fib(num)[::-1] + fib(num)[1:])
