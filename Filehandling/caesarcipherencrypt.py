shift = 3

with open("file.txt", "r") as f:
    text = f.read()

result = ""

for ch in text:
    if ch.isalpha():
        result += chr((ord(ch.lower()) - 97 + shift) % 26 + 97)
    else:
        result += ch

with open("encrypted.txt", "w") as f:
    f.write(result)