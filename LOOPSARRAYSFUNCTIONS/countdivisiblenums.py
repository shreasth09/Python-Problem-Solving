n = int(input("Enter n: "))
k = int(input("Enter divisor: "))
count = 0

for i in range(1, n+1):
    if i % k == 0:
        count += 1

print("Count:", count)