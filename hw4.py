# Запитуємо у користувача два числа
num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

# Запитуємо операцію
operation = input("Введіть операцію (+, -, *, /): ")

# Виконуємо обчислення відповідно до операції
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Помилка: ділення на нуль!"
else:
    result = "Помилка: невірна операція!"

# Виводимо результат
print("Результат:", result)
