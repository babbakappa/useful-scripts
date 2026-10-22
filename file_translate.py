# file_translate.py
# Здесь написан скрипт для объединения аудиофайлов
# из двух папок так, чтобы там и там в результате
# были одинаковые списки

import shutil
from pathlib import Path

from log import INFO, ERROR, print_log

# Функция синхронизации, подаются пути к папкам
# с файлами
def sync_folders(folder1_path, folder2_path):
    # Собираем списки полных путей
    paths1 = get_file_list(folder1_path)
    paths2 = get_file_list(folder2_path)

    # Создаем множества только из ИМЕН для быстрой проверки
    names1 = {f.name for f in paths1}
    names2 = {f.name for f in paths2}

    # Целевые папки для копирования
    dest1 = Path(folder1_path)
    dest2 = Path(folder2_path)

    # Переносим то, чего не хватает в первой папке
    for file_path in paths2:
        if file_path.name not in names1:
            shutil.copy(file_path, dest1 / file_path.name)
            print_log(INFO, f"Перенесли файл {file_path.name} в первую папку")

    # Переносим то, чего не хватает во второй папке
    for file_path in paths1:
        if file_path.name not in names2:
            shutil.copy(file_path, dest2 / file_path.name)
            print_log(INFO, f"Перенесли файл {file_path.name} во вторую папку")

    print_log(INFO, "Успешно!")

# Получение списка названий файлов
def get_file_list(folder_path):
    path = Path(folder_path)
    return [file for file in path.rglob("*") if file.is_file()]

def scenario():
    try:
        folder1_path = input("Введите путь к первой папке: ")
        folder2_path = input("Введите путь ко второй папке: ")
        sync_folders(folder1_path, folder2_path)
    except Exception as error:
        print_log(ERROR, f"{error}")