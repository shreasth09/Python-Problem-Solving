with open("file.txt", "r") as f:
    lines = f.readlines()

print(max(lines, key=len))
