# Check Armstrong number

num = int(input("Enter a number: "))
original = num
power = len(str(num))
sum_val = 0

while num > 0:
    digit = num % 10
    sum_val += digit ** power
    num //= 10

if sum_val == original:
    print("Armstrong number")
else:
    print("Not Armstrong")