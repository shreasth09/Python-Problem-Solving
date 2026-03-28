from collections import Counter

with open("file.txt", "r") as f:
    words = f.read().lower().split()

freq = Counter(words)

for word, count in freq.most_common(5):
    print(word, count)