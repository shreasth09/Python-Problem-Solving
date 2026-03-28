shift = 3

with open("encrypted.txt", "r") as f:
    text = f.read()

result = ""

for ch in text:
    if ch.isalpha():
        result += chr((ord(ch.lower()) - 97 - shift) % 26 + 97)
    else:
        result += ch

print(result)
