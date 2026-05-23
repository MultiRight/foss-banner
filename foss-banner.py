# mimi is a nice cat 🐱

import os
import sys
import time
import random


def read_lines(path, start, end):
    if start < 1 or end < start:
        raise ValueError("start must be >= 1 and end >= start")
    with open(path, 'r', encoding='utf-8') as f:
        result = []
        for i, line in enumerate(f, start=1):
            if i < start:
                continue
            if i > end:
                break
            result.append(line)
    return result


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def init_colors():
    if os.name != "nt":
        return
    try:
        import colorama
        colorama.init(autoreset=True)
    except ImportError:
        # Windows 10+ terminals often support ANSI codes without extra packages.
        pass



def main():
    init_colors()

    start_line = -8
    end_line = 1


    while True:
        color = random.choice(COLORS)
        start_line += 9
        end_line += 9
        lines = read_lines('banner-ascii.txt', start_line, end_line)
        print(color + ''.join(lines) + "\033[0m", end='')
        time.sleep(1)
        clear_screen()

        if end_line >= 287:
            start_line = -8
            end_line = 1

COLORS = ["\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")
        sys.exit(0)
