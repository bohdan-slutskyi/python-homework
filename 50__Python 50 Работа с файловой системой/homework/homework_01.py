"""01 Список файлов и папок

Напишите программу, которая
- принимает путь к директории через аргумент командной строки
- и выводит:
    - Отдельно список папок
    - Отдельно список файлов

Пример запуска:
python script.py /home/user/documents

Пример вывода:
Содержимое директории '/home/user/documents':
Папки:
- folder1
- folder2
Файлы:
- file1.txt
- file2.txt
- notes.docx
"""

import os
import sys


# Источник:
# - theory_02__os_methods.md — os.listdir(), os.path.join(), os.path.isdir(), os.path.isfile()
# - theory_05__sys_argv.py — аргументы командной строки через sys.argv
# В этой задаче путь берётся из командной строки, а содержимое директории делится на папки и файлы.


def print_directory_content(directory_path: str) -> None:
    """Выводит отдельно папки и файлы из указанной директории."""
    folders: list[str] = []
    files: list[str] = []

    # Получаем имена элементов внутри директории и разделяем их по типу.
    for item_name in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item_name)

        if os.path.isdir(item_path):
            folders.append(item_name)
        elif os.path.isfile(item_path):
            files.append(item_name)

    print("Содержимое директории '" + directory_path + "':")

    print("Папки:")
    for folder in sorted(folders):
        print("- " + folder)

    print("Файлы:")
    for file in sorted(files):
        print("- " + file)


def main() -> None:
    """Получает путь из аргумента командной строки и запускает вывод."""
    if len(sys.argv) != 2:
        print("Использование: python homework_01.py <путь_к_директории>")
        return

    # Берём путь к директории из аргумента командной строки.
    directory_path = sys.argv[1]

    if not os.path.exists(directory_path):
        print("Ошибка: указанный путь не существует.")
        return

    if not os.path.isdir(directory_path):
        print("Ошибка: указанный путь не является директорией.")
        return

    print_directory_content(directory_path)


if __name__ == "__main__":
    main()
