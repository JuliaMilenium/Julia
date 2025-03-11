# Функція для обчислення суми парних індексів і множення на останній елемент
def sum_even_indices_times_last(lst):
    if not lst:
        return 0
    sum_even = sum(lst[i] for i in range(0, len(lst), 2))
    return sum_even * lst[-1]

# Запитуємо у користувача список чисел
numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

# Обчислюємо результат та друкуємо його
result = sum_even_indices_times_last(numbers)
print("Результат:", result)
