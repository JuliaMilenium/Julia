num = int(input("Введіть 4-значне число: "))

# Отримуємо кожну цифру окремо
thousands = num // 1000
hundreds = (num % 1000) // 100
tens = (num % 100) // 10
units = num % 10

# Виводимо цифри у стовпчик
print(thousands)
print(hundreds)
print(tens)
print(units)