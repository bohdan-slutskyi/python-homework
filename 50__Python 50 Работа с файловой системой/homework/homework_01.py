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


def print_directory_content(directory_path: str) -> None:
    """Выводит отдельно папки и файлы из указанной директории."""
    folders: list[str] = []
    files: list[str] = []

    # Получаем имена элементов внутри директории и разделяем их по типу.
    # theory_02__os_methods.md: os.listdir(path) возвращает список файлов/папок.
    # os.path.join() собирает полный путь, а isdir()/isfile() проверяют тип.
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
    # theory_05__sys_argv.py: sys.argv[1] — первый аргумент после имени скрипта.
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
