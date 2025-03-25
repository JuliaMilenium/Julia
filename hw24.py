def difference(*args):
    if not args:
        return 0  # Якщо аргументів немає, повертаємо 0
    return round(max(args) - min(args), 2)  # Різниця з округленням до 2 знаків

# Приклади використання
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')


print(difference(1, 2, 3))  # 2
print(difference(5.5, 2.2, 9.8))  # 7.6
print(difference(1.11111, 1.11113))  # 0.0
print(difference())  # 0
