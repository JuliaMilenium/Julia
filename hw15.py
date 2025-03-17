def multiply_digits_until_single(n):
    while n > 9:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
    return n

# Ввід числа користувачем
num = int(input("Введіть ціле число: "))
result = multiply_digits_until_single(num)
print("Результат:", result)
