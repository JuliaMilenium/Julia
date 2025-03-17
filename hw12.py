import string


def generate_hashtag(text: str) -> str:
    # Видаляємо пунктуацію та пробіли
    cleaned_text = ''.join(char for char in text if char not in string.punctuation).split()

    # Якщо текст після очищення порожній, повертаємо пустий рядок
    if not cleaned_text:
        return ""

    # Формуємо хештег з великими літерами на початку кожного слова
    hashtag = "#" + "".join(word.capitalize() for word in cleaned_text)

    # Обрізаємо, якщо більше 140 символів
    return hashtag[:140]


# Приклад використання
user_input = input("Введіть рядок: ")
print(generate_hashtag(user_input))
