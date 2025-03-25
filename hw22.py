def find_unique_value(numbers):
    # Створюємо словник з підрахунком повторень
    for num in numbers:
        if numbers.count(num) == 1:
            return num

# Приклади використання
print(find_unique_value([1, 1, 2, 1]))          # 2
print(find_unique_value([0, 0, 0, 7, 0]))       # 7
print(find_unique_value([4, 5, 4, 4, 4]))       # 5
print(find_unique_value([9]))                   # 9
print(find_unique_value([2, 3, 2, 2]))          # 3
