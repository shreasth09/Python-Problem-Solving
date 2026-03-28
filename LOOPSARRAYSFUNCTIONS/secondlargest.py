arr = list(map(int, input("Enter elements: ").split()))

arr = list(set(arr))
arr.sort()

print("Second largest:", arr[-2])