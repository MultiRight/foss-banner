# mimi is a nice cat 🐱

# Invoking libraries via import
import time
import random

def read_lines(path, start, end):
    if start < 1 or end < start:
        raise ValueError("start must be >=1 and end >= start")
    with open(path, 'r', encoding='utf-8') as f:
        result = []
        for i, line in enumerate(f, start=1):
            if i < start:
                continue
            if i > end:
                break
            result.append(line)
    return result
start_line = -8
end_line = 1
COLORS = ["\033[31m","\033[32m","\033[33m","\033[34m","\033[35m","\033[36m"]
# Usage
while True:
    color = random.choice(COLORS)
    start_line += 9
    end_line += 9
    lines = read_lines('banner-ascii.txt', start_line, end_line)
    print(color + ''.join(lines) + "\033[0m", end='')
    time.sleep(1)
    print("\033[H\033[J", end="")
    if end_line >= 287:
        start_line = -8
        end_line = 1
