# log.py
# Здесь функция для вывода логов

INFO = "INFO"
WARNING = "WARNING"
ERROR = "ERROR"

def print_log(type, message):
    print(f"{type} | {message}")