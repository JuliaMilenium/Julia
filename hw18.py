def second_index(text: str, target: str) -> int | None:
    # Знаходимо перше входження
    first = text.find(target)
    if first == -1:
        return None  # Якщо немає першого входження

    # Шукаємо друге входження починаючи після першого
    second = text.find(target, first + 1)
    return second if second != -1 else None


# Приклади використання:
print(second_index("sims", "s"))  # Виведе 3
print(second_index("find the river", "e"))  # Виведе 12
print(second_index("hi", " "))  # Виведе None
print(second_index("Hello world!", "o"))  # Виведе 7
print(second_index("Hello world!", "z"))  # Виведе None
