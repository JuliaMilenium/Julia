def popular_words(text, words):
    # Перетворюємо текст на нижній регістр і розбиваємо на слова
    text_words = text.lower().split()
    # Використовуємо словник для підрахунку частоти слів
    return {word: text_words.count(word) for word in words}

# Приклад використання
example_text = '''
When I was One
I had just begun
When I was Two
I was nearly new
'''
print(popular_words(example_text, ['i', 'was', 'three', 'near']))
