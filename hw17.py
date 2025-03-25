def correct_sentence(text: str) -> str:
    # Робимо першу літеру великою
    text = text.capitalize()
    # Додаємо крапку, якщо її немає
    if not text.endswith('.'):
        text += '.'
    return text

# Приклади використання
print(correct_sentence("hello world"))               # "Hello world."
print(correct_sentence("this is a test"))            # "This is a test."
print(correct_sentence("Python is awesome."))        # "Python is awesome."
print(correct_sentence("greetings, friends"))        # "Greetings, friends."
print(correct_sentence("already correct."))          # "Already correct."
