with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

for i in range(min(len(lines1), len(lines2))):
    if lines1[i] != lines2[i]:
        print(f"Line {i+1} differs")