def is_palindrome(s):
    return s == s[::-1]

text = input("Enter string: ")
print(is_palindrome(text))