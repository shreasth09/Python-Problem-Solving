import string

with open("file.txt", "r") as f:
    text = f.read()

for ch in string.punctuation:
    text = text.replace(ch, "")

print(text)