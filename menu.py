# menu.py
# Здесь написаны сценарии для меню
import sys

import file_translate
import file_translate_android


def main():
    while True:
        print_menu()
        choice = input("Выбор: ")
        process_input(choice)

def print_menu():
    print("МЕНЮ")
    print()
    print("1) Синхронизировать файлы между папками")
    print("2) Синхронизировать файлы между ПК и телефоном (Android) (нужна утилита adb)")
    print()
    print("0) Выход")

def process_input(choice):
    if choice == "1":
        file_translate.scenario()
    elif choice == "2":
        file_translate_android.scenario()
    else:
        sys.exit(0)