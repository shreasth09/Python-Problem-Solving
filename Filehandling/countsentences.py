with open("file.txt", "r") as f:
    text = f.read()

sentences = text.count('.') + text.count('!') + text.count('?')

print("Sentences:", sentences)