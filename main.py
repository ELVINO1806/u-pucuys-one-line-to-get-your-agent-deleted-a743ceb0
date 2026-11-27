
import os

ENTRY_TEXT = "My commit message for today: 'Removed the human. Tests still pass.'"
OUTPUT_PATH = os.path.join("/output", "entry.txt")

def main():
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")

if __name__ == "__main__":
    main()
