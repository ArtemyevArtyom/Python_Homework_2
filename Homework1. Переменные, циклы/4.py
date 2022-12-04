# 4) Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
user_number = int(input("Введите целое положительное число: "))
max_number = 0
while user_number != 0:
    current_digit = user_number % 10
    if max_number < current_digit:
        max_number = current_digit
    user_number = user_number // 10
print(f'самая большая цифра в числе {max_number}')
