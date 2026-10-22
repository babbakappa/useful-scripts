# log.py
# Здесь функция для вывода логов

from colorama import Fore, Style
import colorama

colorama.init()

SUCCESS = Fore.LIGHTGREEN_EX + "[Success]" + Style.RESET_ALL
INFO = Fore.LIGHTBLUE_EX + "[Info]" + Style.RESET_ALL
WARNING = Fore.LIGHTYELLOW_EX + "[Warning]" + Style.RESET_ALL
ERROR = Fore.LIGHTRED_EX + "[Error]" + Style.RESET_ALL

def print_log(type, message):
    print(f"{type} | {message}")