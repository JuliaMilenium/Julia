import string
import keyword


def is_valid_variable_name(name: str) -> bool:
    if not name:
        return False

    # Перевірка, чи не є ім'я зареєстрованим словом
    if name in keyword.kwlist:
        return False

    # Перевірка на початок із цифри
    if name[0].isdigit():
        return False

    # Перевірка на заборонені символи
    allowed_chars = set("_" + string.ascii_lowercase + string.digits)
    if not set(name).issubset(allowed_chars):
        return False

    # Перевірка кількості підкреслень
    if name.count("_") > 1:
        return False

    return True


# Приклади перевірки
examples = [
    "_",  # True
    "var",  # True
    "_var",  # True
    "var_",  # True
    "var123",  # True
    "123var",  # False (починається з цифри)
    "Var",  # False (містить велику літеру)
    "var iable",  # False (містить пробіл)
    "var-name",  # False (містить знак пунктуації)
    "for",  # False (зареєстроване слово)
    "_variable_name"  # False (більше одного "_")
]

for example in examples:
    print(is_valid_variable_name(example))