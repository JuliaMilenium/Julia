import string


def get_letters_between():
    user_input = input("Введіть дві літери через дефіс (наприклад, a-z): ")
    start, end = user_input.split('-')

    letters = string.ascii_letters
    start_index = letters.index(start)
    end_index = letters.index(end)

    result = letters[start_index:end_index + 1]
    print(result)


get_letters_between()
