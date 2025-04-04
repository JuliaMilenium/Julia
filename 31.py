import re

def clean_html(input_filename, output_filename="cleaned.txt", remove_empty_lines=True):
    with open(input_filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Видалення html-тегів
    cleaned_text = re.sub(r'<[^>]+>', '', content)

    # Розбиття на рядки
    lines = cleaned_text.splitlines()

    if remove_empty_lines:
        # Видаляємо порожні або рядки лише з пробілами
        lines = [line.strip() for line in lines if line.strip()]

    # Запис результату у файл
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))

    print(f"Очищений текст записано у файл '{output_filename}'.")

# Приклад використання:
clean_html("draft.html.txtc")
