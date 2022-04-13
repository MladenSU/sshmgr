from termcolor import colored


class Colors:
    @staticmethod
    def warning(text):
        print(f"{colored('[WARN]', 'yellow')} {text}")

    @staticmethod
    def okmsg(text):
        print(f"{colored('[OK]', 'green')} {text}")

    @staticmethod
    def info(text):
        print(f"{colored('[INFO]', 'blue')} {text}")
