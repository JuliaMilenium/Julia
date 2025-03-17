def format_time(seconds):
    if not (0 <= seconds < 8640000):
        return "Число повинно бути від 0 до 8 640 000"

    days, remainder = divmod(seconds, 86400)  # 1 день = 86400 секунд
    hours, remainder = divmod(remainder, 3600)  # 1 година = 3600 секунд
    minutes, seconds = divmod(remainder, 60)  # 1 хвилина = 60 секунд

    # Вибір правильного закінчення слова "день"
    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    day_part = f"{days} {day_word}, " if days > 0 else ""
    time_part = f"{hours:02}:{minutes:02}:{seconds:02}"

    return f"{day_part}{time_part}"

# Ввід користувачем числа
user_inpu = int(input("Введіть число секунд (від 0 до 8640000): "))
print(format_time(user_inpu))
