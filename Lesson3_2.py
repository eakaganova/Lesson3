# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

name = input('Введи имя: ')
last_name = input('Введи фамилию: ')
age_year = input('Введи год рождения: ')
city = input('Введи город проживания: ')
email = input('Введи email: ')
phone_number = input('Введи номер телефона: ')
def user_data (name, last_name, age_year, city, email, phone_number):
    print(f"{name} {last_name}. Год рождения: {age_year}. Город проживания: {city}. "
          f"Контактные данные: email {email}, номер телефона {phone_number}.")
user_data(name=name, last_name=last_name, age_year=age_year, city=city, email=email, phone_number=phone_number)




