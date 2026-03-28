with open("file.txt", "r") as f:
    lines = f.readlines()

lines.sort()

with open("output.txt", "w") as f:
    f.writelines(lines)
    