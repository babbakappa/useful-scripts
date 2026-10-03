# menu.py
# Здесь написаны сценарии для меню
import sys

import music

def main():
    while True:
        print_menu()
        choice = input("Выбор: ")
        process_input(choice)

def print_menu():
    print("1) Распределить музыку в двух папках")
    print()
    print("0) Выход")

def process_input(choice):
    if choice == "1":
        music.scenario()
    else:
        sys.exit(0)