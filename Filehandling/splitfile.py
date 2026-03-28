with open("file.txt", "r") as f:
    lines = f.readlines()

for i in range(0, len(lines), 5):
    with open(f"part_{i}.txt", "w") as f2:
        f2.writelines(lines[i:i+5])