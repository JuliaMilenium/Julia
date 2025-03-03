# Запитуємо у користувача 5-значне число
num = int(input("Введіть 5-значне число: "))

# Отримуємо кожну цифру окремо
first = num // 10000
second = (num % 10000) // 1000
third = (num % 1000) // 100
fourth = (num % 100) // 10
fifth = num % 10

# Формуємо перевернуте число
reversed_num = fifth * 10000 + fourth * 1000 + third * 100 + second * 10 + first

# Виводимо перевернуте число
print(reversed_num)