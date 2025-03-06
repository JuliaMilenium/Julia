# Функція для переміщення останнього елемента на початок
def move_last_to_first(lst):
    if len(lst) > 1:
        lst.insert(0, lst.pop())
    return lst

# Запитуємо у користувача список чисел
numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

# Змінюємо список та друкуємо результат
result = move_last_to_first(numbers)
print("Оновлений список:", result)
