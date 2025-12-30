n = int(input("Enter a number: "))
temp = n
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if n == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")