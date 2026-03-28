arr = list(map(int, input("Enter elements: ").split()))

non_zero = [x for x in arr if x != 0]
zeros = [0] * arr.count(0)

print(non_zero + zeros)
