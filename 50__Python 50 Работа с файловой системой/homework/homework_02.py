""" 02 Поиск и удаление файлов с указанным расширением

Напишите программу, которая
- Принимает путь к директории и расширение файлов через аргумент командной строки.
- Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
- Спрашивает у пользователя, хочет ли он удалить найденные файлы.
- Если пользователь подтверждает, удаляет их.

Пример запуска
python script.py /home/user/PycharmProjects/project1 .log

Пример вывода:
Найдены файлы с расширением '.log':
- logs/error.log
- logs/system.log
- logs/backup/old.log
- logs/backup/debug.log

Вы хотите удалить эти файлы? (y/n): y
Удаление завершено.
"""

import os
import sys

# Источники теории:
# - materials/theory_02__os_methods.md — таблица "Основные методы модуля os"
#   Используются: os.path.isdir(), os.path.join(), os.makedirs(), os.remove(), os.sep.
# - materials/theory_05__open.md — пример создания файла через open(..., "w").
# - materials/theory_03__os_walk.py — пример рекурсивного обхода папок через os.walk().
# - materials/theory_05__sys_argv.py — пример с sys.argv:
#   sys.argv[0] — имя скрипта, sys.argv[1:] — аргументы командной строки.


# Для тестирования удаления:
# создаём тестовые файлы error.log, system.log, old.log, debug.log
# внутри директории, которую пользователь передал через аргумент командной строки.
# Структура папок: logs/ и logs/backup/.

def create_test_files(directory: str) -> None:
    """Создаёт тестовые .log файлы для проверки удаления."""
    logs_directory = os.path.join(directory, "logs")
    backup_directory = os.path.join(logs_directory, "backup")

    # Создаём тестовые папки внутри выбранной директории.
    # theory_02__os_methods.md: os.makedirs(path) создаёт вложенные папки.
    os.makedirs(backup_directory, exist_ok=True)

    files: list[str] = [
        os.path.join(logs_directory, "error.log"),
        os.path.join(logs_directory, "system.log"),
        os.path.join(backup_directory, "old.log"),
        os.path.join(backup_directory, "debug.log"),
    ]

    # Создаём тестовые файлы внутри выбранной папки.
    # theory_05__open.md: open(..., "w") создаёт файл или очищает существующий.
    for file_path in files:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("")


def find_files_with_extension(directory: str, extension: str) -> list[str]:
    """Рекурсивно ищет файлы с заданным расширением."""
    found_files: list[str] = []

    # Рекурсивно обходим директорию и все вложенные папки.
    # theory_03__os_walk.py: os.walk() проходит по папке сверху вниз.
    for current_path, folders, files in os.walk(directory):
        # Проверяем каждый файл в текущей папке.
        for file_name in files:
            if file_name.endswith(extension):
                full_path = os.path.join(current_path, file_name)

                # Получаем путь относительно выбранной директории.
                # Используем срез строки для получения относительного пути.
                relative_path = full_path[len(directory) + 1:]
                found_files.append(relative_path)

    return found_files


def delete_files(directory: str, files: list[str]) -> None:
    """Удаляет найденные файлы."""
    for file_path in files:
        full_path = os.path.join(directory, file_path)

        # Удаляем файл только после подтверждения пользователя.
        # theory_02__os_methods.md: os.remove(path) удаляет файл.
        os.remove(full_path)


def main() -> None:
    """Получает аргументы командной строки и запускает поиск файлов."""
    if len(sys.argv) != 3:
        print("Использование: python homework_02.py <путь_к_директории> <расширение>")
        return

    # Берём путь к директории и расширение из аргументов командной строки.
    # theory_05__sys_argv.py: sys.argv[1:] — аргументы после имени скрипта.
    directory = sys.argv[1].rstrip(os.sep)
    extension = sys.argv[2]

    if not os.path.isdir(directory):
        print("Ошибка: указанный путь не является существующей директорией.")
        return

    create_test_files(directory)
    found_files = sorted(find_files_with_extension(directory, extension))

    if not found_files:
        print("Файлы с расширением '" + extension + "' не найдены.")
        return

    print("Найдены файлы с расширением '" + extension + "':")
    for file_path in found_files:
        print("- " + file_path)

    answer = input("Вы хотите удалить эти файлы? (y/n): ")
    while answer not in ("y", "n"):
        answer = input("Вы хотите удалить эти файлы? (y/n): ")

    if answer == "y":
        delete_files(directory, found_files)
        print("Удаление завершено.")
    else:
        print("Удаление отменено.")


if __name__ == "__main__":
    main()
