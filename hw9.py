import random

# Генеруємо список випадкової довжини від 3 до 10
numbers = [random.randint(1, 100) for _ in range(random.randint(3, 10))]

# Створюємо новий список із першого, третього та останнього елементів
if len(numbers) >= 3:
    new_list = [numbers[1], numbers[3], numbers[-2]]
else:
    new_list = numbers  # На випадок, якщо довжина менша за 3 (малоймовірно)

# Виводимо результати
print("Початковий список:", numbers)
print("Новий список:", new_list)
