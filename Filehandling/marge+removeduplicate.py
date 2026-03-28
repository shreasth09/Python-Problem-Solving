files = ["file1.txt", "file2.txt"]

data = set()

for file in files:
    with open(file, "r") as f:
        data.update(f.readlines())

with open("merged.txt", "w") as f:
    f.writelines(data)