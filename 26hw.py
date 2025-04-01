import re

def first_word(text: str) -> str:
    """ Пошук першого слова """
    match = re.search(r"[a-zA-Z']+", text)
    return match.group() if match else ""

# Тестування
assert first_word("Hello world") == "Hello", "Test 1"
assert first_word("...and so on") == "and", "Test 2"
assert first_word("Don't stop") == "Don't", "Test 3"
assert first_word("    first") == "first", "Test 4"
assert first_word("single") == "single", "Test 5"
assert first_word(".first, second.") == "first", "Test 6"

print("OK")
