# Функція для поділу списку на два
def split_list(lst):
    length = len(lst)
    mid = (length + 1) // 2  # Розраховуємо середину (більша частина для непарної кількості)
    return [lst[:mid], lst[mid:]]

# Запитуємо у користувача список чисел
numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

# Ділимо список і друкуємо результат
result = split_list(numbers)
print("Розділений список:", result)
