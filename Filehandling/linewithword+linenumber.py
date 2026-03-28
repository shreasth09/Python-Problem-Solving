word = input("Enter word: ")

with open("file.txt", "r") as f:
    for i, line in enumerate(f, 1):
        if word in line:
            print(f"Line {i}: {line}")