num = int(input("Enter number: "))
prod = 1

while num > 0:
    prod *= num % 10
    num //= 10

print("Product:", prod)