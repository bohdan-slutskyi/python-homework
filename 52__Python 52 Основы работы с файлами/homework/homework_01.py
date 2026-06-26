""" 01 Фильтрация по ключевому слову

Напишите программу, которая
- ищет в файле все строки, содержащие указанное пользователем слово,
- и сохраняет их в новый файл.

Имя нового файла формируется как <keyword>_<original_filename>.
Если файл не существует, программа должна вывести ошибку.
Если совпадения не найдены, новый файл не создаётся.

Используйте файл system_log.txt.

Пример ввода:
Введите имя файла для поиска: system_log.txt
Введите ключевое слово: error

Пример вывода:
Строки, содержащие 'error', сохранены в <keyword>_<original_filename>.

"""

# источники:
# - materials/theory_01__open.md — open(), чтение/запись файлов, with, обработка FileNotFoundError

def find_keyword(filename: str, keyword: str) -> None:
    try:
        with open(filename, 'r') as file:
            found_lines = []

            for line in file:
                if keyword in line:
                    found_lines.append(line)
    except FileNotFoundError as error:
        print(f'File not found: {error}')
        return

    if not found_lines:
        return

    new_filename = f'{keyword}_{filename}'

    with open(new_filename, 'w') as file:
        for line in found_lines:
            file.write(line)

    print(f"Строки, содержащие '{keyword}', сохранены в {new_filename}.")


find_keyword('s', 'error')
# File not found: [Errno 2] No such file or directory: 's'

find_keyword('system_log.txt', 'error')
# Строки, содержащие 'error', сохранены в error_system_log.txt.
