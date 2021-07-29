# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
divisible = float(input('Задай делитель: '))
divider = float(input('Задай делитель: '))
def number_division (divisible, divider):
    try:
        return (divisible / divider)
    except ZeroDivisionError:
        print('На ноль делить нельзя! (Можно, но не сейчас). Введи другое число, пожалуйста.')
print(number_division(divisible, divider))
