arr = list(map(int, input("Enter elements: ").split()))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

print(freq)