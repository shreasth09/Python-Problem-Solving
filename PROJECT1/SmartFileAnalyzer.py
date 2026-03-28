# 📂 Smart File Analyzer CLI

from collections import Counter

def analyze_file(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        text = "".join(lines)
        words = text.split()

        print("\n📊 FILE ANALYSIS REPORT\n")

        # Basic stats
        print("Total Lines:", len(lines))
        print("Total Words:", len(words))
        print("Total Characters:", len(text))

        # Top 10 frequent words
        freq = Counter(words)
        print("\n🔝 Top 10 Frequent Words:")
        for word, count in freq.most_common(10):
            print(word, ":", count)

        # Duplicate lines
        duplicates = set([line for line in lines if lines.count(line) > 1])
        print("\n♻️ Duplicate Lines:")
        for line in duplicates:
            print(line.strip())

        # Longest & shortest line
        print("\n📏 Longest Line:")
        print(max(lines, key=len).strip())

        print("\n📏 Shortest Line:")
        print(min(lines, key=len).strip())

    except FileNotFoundError:
        print("❌ File not found")


def search_word(filename, word):
    with open(filename, "r") as f:
        for i, line in enumerate(f, 1):
            if word in line:
                print(f"Line {i}: {line.strip()}")


def export_report(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    text = "".join(lines)
    words = text.split()

    with open("report.txt", "w") as f:
        f.write("FILE ANALYSIS REPORT\n")
        f.write(f"Lines: {len(lines)}\n")
        f.write(f"Words: {len(words)}\n")
        f.write(f"Characters: {len(text)}\n")

    print("✅ Report saved as report.txt")


def main():
    filename = input("Enter file name: ")

    while True:
        print("\n==== MENU ====")
        print("1. Analyze File")
        print("2. Search Word")
        print("3. Export Report")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            analyze_file(filename)

        elif choice == "2":
            word = input("Enter word to search: ")
            search_word(filename, word)

        elif choice == "3":
            export_report(filename)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()