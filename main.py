# Вводим восьмизначное число
n = int(input("Введите восьмизначное число: "))
# Инициализируем сумму цифр
sum_of_digits = 0
# Вычисляем сумму цифр числа
sum_of_digits += n // 10000000
sum_of_digits += (n // 1000000) % 10
sum_of_digits += (n // 100000) % 10
sum_of_digits += (n // 10000) % 10
sum_of_digits += (n // 1000) % 10
sum_of_digits += (n // 100) % 10
sum_of_digits += (n // 10) % 10
sum_of_digits += n % 10
# Выводим резльтат
print(f"Сумма цифр числа {n} равна {sum_of_digits}")
