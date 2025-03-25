def add_one(digits):
    # Перетворюємо список цифр на число
    number = int(''.join(map(str, digits)))
    # Додаємо 1 до отриманого числа
    number += 1
    # Розбиваємо число на окремі цифри
    return [int(digit) for digit in str(number)]

# Тести
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print('✅ Усі тести пройдено!')
