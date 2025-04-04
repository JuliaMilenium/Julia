
def prime_generator(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for number in range(2, limit):
        if is_prime(number):
            yield number

# Приклад використання
print(list(prime_generator(10)))  # [2, 3, 5, 7]
gen = prime_generator(1)

