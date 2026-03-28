# Remove duplicates from list

numbers = list(map(int, input("Enter numbers: ").split()))

unique = list(set(numbers))

print("Without duplicates:", unique)