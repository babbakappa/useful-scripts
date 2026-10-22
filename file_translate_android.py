import subprocess
from pathlib import Path
from log import print_log, ERROR, INFO, SUCCESS


def get_pc_files(pc_folder):
    path = Path(pc_folder)
    return {f.name: f for f in path.rglob("*") if f.is_file()}


def get_phone_files(phone_folder, adb_folder):
    try:
        result = subprocess.run(
            [rf"{adb_folder}\adb", "shell", f"ls '{phone_folder}'"],
            capture_output=True, text=True, check=True, encoding="utf-8"
        )
        files = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        return set(files)
    except subprocess.CalledProcessError as e:
        print_log(ERROR, f"Ошибка при чтении файлов с телефона: {e.stderr}")
        return set()


def sync_pc_and_phone(pc_folder, phone_folder, adb_folder):
    pc_dir = Path(pc_folder)

    pc_files = get_pc_files(pc_folder)
    phone_files = get_phone_files(phone_folder, adb_folder)

    for file_name, file_path in pc_files.items():
        if file_name not in phone_files:
            print_log(INFO, f"Копируем на телефон: {file_name}")
            subprocess.run([rf"{adb_folder}\adb", "push", str(file_path), phone_folder], check=True)

    for file_name in phone_files:
        if file_name not in pc_files:
            print_log(INFO, f"Скачиваем с телефона: {file_name}")
            dest_path = pc_dir / file_name

            phone_file_path = f"{phone_folder.rstrip('/')}/{file_name}"
            subprocess.run([rf"{adb_folder}\adb", "pull", phone_file_path, str(dest_path)], check=True)

    print_log(SUCCESS, "Синхронизация успешно завершена!")


def scenario():

    local_pc_path = input("Введите путь к папке на ПК: ").strip()

    phone_input = input("Введите путь к папке на телефоне: ").strip().lstrip("/")
    remote_phone_path = f"/sdcard/{phone_input}".replace("\\", "/")

    adb_folder = input("Введите путь к adb исполнителю: ").strip()

    try:
        sync_pc_and_phone(local_pc_path, remote_phone_path, adb_folder)
    except Exception as error:
        print_log(ERROR, f"Произошла ошибка: {error}")
