# Функція для переміщення всіх нулів у кінець списку
def move_zeros_to_end(lst):
    non_zero = [num for num in lst if num != 0]  # Зберігаємо ненульові елементи
    zeros = [0] * lst.count(0)  # Створюємо список нулів
    return non_zero + zeros

# Запитуємо у користувача список чисел
numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

# Переміщуємо нулі та друкуємо результат
result = move_zeros_to_end(numbers)
print("Оновлений список:", result)
