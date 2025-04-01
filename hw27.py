def is_even(number: int) -> bool:
    """ Перевірка чи є парним число """
    return number % 2 == 0

# Тестування
assert is_even(2) == True, "Test 1"
assert is_even(5) == False, "Test 2"
assert is_even(0) == True, "Test 3"
assert is_even(-4) == True, "Test 4"
assert is_even(-3) == False, "Test 5"

print("Автотести пройдено успішно!")

# Перевірка числа, введеного користувачем
user_input = int(input("Введіть ціле число: "))
print(f"Число {user_input} парне: {is_even(user_input)}")
