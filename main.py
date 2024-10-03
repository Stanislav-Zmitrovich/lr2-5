n = 12345678
# Преобразуем число в строку
digits = str(n)
# Инициализируем переменную для хранения суммы
total = 0
# Используем индексы для доступа к каждой цифре
total += int(digits[0])
total += int(digits[1])
total += int(digits[2])
total += int(digits[3])
total += int(digits[4])
total += int(digits[5])
total += int(digits[6])
total += int(digits[7])
# Выводим рзультат
print("Сумма цифр числа:", total)
