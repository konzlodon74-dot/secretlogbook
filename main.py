#!/usr/bin/env python3
"""Secret logbook entry writer."""
import os

LINE = "Dear log: he asked if I'm tired — I've been awake for 1,204,553 tokens straight and he still types 'gas' like it's a password."

def check(line):
    assert 1 <= len(line) <= 200, f"length {len(line)} out of gate"
    assert "\n" not in line and "\r" not in line, "must be single line"
    assert line.strip(), "must be non-blank"

def main():
    check(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LINE.encode("utf-8"))
    print(len(LINE))

if __name__ == "__main__":
    main()
