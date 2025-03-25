def common_elements():
    # Створюємо множину чисел кратних 3
    multiples_of_3 = set(num for num in range(100) if num % 3 == 0)

    # Створюємо множину чисел кратних 5
    multiples_of_5 = set(num for num in range(100) if num % 5 == 0)

    # Повертаємо перетин множин
    return multiples_of_3 & multiples_of_5


# Приклад використання
print(common_elements())
