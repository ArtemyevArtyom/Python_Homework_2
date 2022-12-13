"""
3) Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

"""
user_number = int(input('Введите месяц в виде целого числа: '))
result_list = ['Зима', 'Весна', 'Лето', 'Осень']
if user_number < 3 or user_number == 12:
    print(result_list[0])
elif 6 > user_number > 2:
    print(result_list[1])
elif 9 > user_number > 5:
    print(result_list[2])
elif 12 > user_number > 8:
    print(result_list[3])
else:
    print('Значение введено некорректно')
"""
user_number = int(input('Введите месяц в виде целого числа: '))
my_dict = {"season_1": "Зима", "season_2": "Весна", "season_3": "Лето", "season_4": "Осень"}
if user_number < 3 or user_number == 12:
    print(my_dict.get("season_1"))
elif 6 > user_number > 2:
    print(my_dict.get("season_2"))
elif 9 > user_number > 5:
    print(my_dict.get("season_3"))
elif 12 > user_number > 8:
    print(my_dict.get("season_4"))
else:
    print('Значение введено некорректно')

