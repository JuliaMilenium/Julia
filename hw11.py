import math


def calculator():
    while True:
        try:
            num1 = float(input("Введіть перше число: "))
            operation = input("Введіть операцію (+, -, *, /): ")
            num2 = float(input("Введіть друге число: "))

            match operation:
                case '+':
                    result = num1 + num2
                case '-':
                    result = num1 - num2
                case '*':
                    result = num1 * num2
                case '/':
                    if num2 == 0:
                        print("Помилка: Ділення на нуль!")
                        continue
                    result = num1 / num2
                case _:
                    print("Невідома операція. Спробуйте ще раз.")
                    continue

            print(f"Результат: {result}")
        except ValueError:
            print("Помилка: Некоректне число. Спробуйте ще раз.")
            continue

        repeat = input("Бажаєте продовжити? (yes/y для продовження): ").strip().lower()
        if repeat not in ('y', 'yes'):
            print("Калькулятор завершує роботу.")
            break


calculator()