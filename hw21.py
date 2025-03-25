import string

def is_palindrome(text):
    # Видаляємо знаки пунктуації та пробіли, приводимо до нижнього регістру
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    # Перевіряємо, чи є рядок паліндромом
    return cleaned_text == cleaned_text[::-1]

# Приклади використання
print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("racecar"))                         # True
print(is_palindrome("Hello, World!"))                   # False
print(is_palindrome("Madam"))                           # True
print(is_palindrome("No lemon, no melon"))              # True
