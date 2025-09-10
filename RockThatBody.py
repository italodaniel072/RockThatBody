import sys
import time

def printLyrics():
    lines = [
        ("I wanna da-", 0.06),  # 1
        ("I wanna dance in the lights", 0.05),  # 2
        ("I wanna ro-", 0.07),  # 3
        ("I wanna rock your body", 0.08),  # 4
        ("I wanna go", 0.08),  # 5
        ("I wanna go for a ride", 0.068),  # 6
        ("Hop in the music and", 0.07),  # 7
        ("Rock your body", 0.08),  # 8
        ("Rock that body", 0.069),  # 9
        ("come on, come on", 0.035),  # 10
        ("Rock that body", 0.05),  # 11
        ("Rock your body", 0.03),  # 12
        ("Rock that body", 0.049),  # 13
        ("come on, come on", 0.035),  # 14
        ("Rock that body", 0.08),  # 15
    ]

    # Extra pauses between lines (same as in your previous example)
    delays_after_line = [0.5] * len(lines)  # pode customizar cada um

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            time.sleep(char_delay)
        print()  # quebra de linha
        time.sleep(delays_after_line[i])

if __name__ == "__main__":
    printLyrics()