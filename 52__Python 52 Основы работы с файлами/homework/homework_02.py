""" 02 Поиск и удаление дубликатов

Напишите программу, которая
- удаляет дублирующиеся строки из файла
- и сохраняет результат в новый файл.

Имя нового файла формируется как unique_<original_filename>.

Если файл не существует, программа должна вывести ошибку.

Исходный порядок строк должен сохраниться.
Если в файле нет дубликатов, создаётся точная копия файла.

Используйте файл movies_to_watch.txt.

Пример ввода:
Введите имя файла: movies_to_watch.txt

Пример вывода:
Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

"""

# источники:
# - materials/theory_01__open.md — open(), чтение/запись файлов, with, обработка FileNotFoundError, построчное чтение файла

def remove_duplicates(filename: str) -> None:
    try:
        with open(filename, 'r') as file:
            unique_lines = []
            seen_lines = []

            for line in file:
                if line not in seen_lines:
                    seen_lines.append(line)
                    unique_lines.append(line)
    except FileNotFoundError as error:
        print(f'File not found: {error}')
        return

    new_filename = f'unique_{filename}'

    with open(new_filename, 'w') as file:
        for line in unique_lines:
            file.write(line)

    print(f'Дубликаты удалены. Уникальные строки сохранены в {new_filename}.')



remove_duplicates("movies_to_watch.txt")
# Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

remove_duplicates("M")
# File not found: [Errno 2] No such file or directory: 'M'
