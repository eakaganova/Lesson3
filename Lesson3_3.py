# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    a_list = [x, y, z]
    b_list = sorted(a_list)
    return print(sum(b_list[1:]))
print(my_func())
