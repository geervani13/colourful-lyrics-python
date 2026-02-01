import os
import sys
import time
import random

# Clear screen at start
os.system('cls')

# ANSI color codes
colors = [
    "\033[91m",  # red
    "\033[92m",  # green
    "\033[93m",  # yellow
    "\033[94m",  # blue
    "\033[95m",  # magenta
    "\033[96m",  # cyan
]
reset = "\033[0m"
 
def printLyrics():
    # (line, char_delay, line_delay)
    lines = [
        ("I wanna da-", 0.06, 0.4),
        ("I wanna dance in the lights", 0.05, 0.5),
        ("I wanna ro-", 0.07, 0.4),
        ("I wanna rock your body", 0.08, 0.5),
        ("I wanna go", 0.08, 0.4),
        ("I wanna go for a ride", 0.068, 0.5),
        ("Hop in the music and", 0.07, 0.4),
        ("Rock your body", 0.08, 0.4),
        ("Rock that body", 0.069, 0.4),
        ("come on, come on", 0.035, 0.4),
        ("Rock that body", 0.05, 0.4),
        ("Rock your body", 0.03, 0.4),
        ("Rock that body", 0.049, 0.4),
        ("come on, come on", 0.035, 0.4),
        ("Rock that body", 0.08, 0.6),
    ]

    for text, char_delay, line_delay in lines:
        for char in text:
            color = random.choice(colors)  # disco per character
            sys.stdout.write(color + char + reset)
            sys.stdout.flush()
            time.sleep(char_delay)  # character timing
        print()  # new line
        time.sleep(line_delay)  # pause after line

printLyrics()