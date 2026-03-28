replacements = {"hello": "hi", "world": "earth"}

with open("file.txt", "r") as f:
    text = f.read()

for k, v in replacements.items():
    text = text.replace(k, v)

with open("output.txt", "w") as f:
    f.write(text)