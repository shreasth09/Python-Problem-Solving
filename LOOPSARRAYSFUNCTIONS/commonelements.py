a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))

common = list(set(a) & set(b))

print("Common elements:", common)