with open("file.txt", "r") as f:
    lines = f.readlines()

unique = list(set(lines))

with open("output.txt", "w") as f:
    f.writelines(unique)