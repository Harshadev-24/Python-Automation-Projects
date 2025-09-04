import sys
import pyperclip
import json
from pathlib import Path

SAVED_DATA = Path("clipboard.json")


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except:
        return {}


if len(sys.argv) >= 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        if len(sys.argv) < 4:
            print("Usage: python multiclipboard.py save <key> <text>")
        else:
            key = sys.argv[2]
            value = " ".join(sys.argv[3:])  # join remaining args as text
            data[key] = value
            save_data(SAVED_DATA, data)
            print(f"Saved '{value}' under key '{key}'")
    elif command == "load":
        if len(sys.argv) < 3:
            print("Usage: python multiclipboard.py load <key>")
        else:
            key = sys.argv[2]
            if key in data:
                pyperclip.copy(data[key])
                print(f"Copied '{data[key]}' from key '{key}' to clipboard")
            else:
                print("Key does not exist.")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass a command (save | load | list).")
