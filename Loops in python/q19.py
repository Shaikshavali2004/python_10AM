# 19.Program to print the reverse of digits of numbers.


num = int(input("Enter a Number:"))
reverse=0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("The reversed number is:",reverse)


"""n1 = int(input("Enter any Value:"))
reverse = 0
while n1 > 0:
    digit = n1 % 10
    reverse = reverse * 10 + digit
    n1 //= 10
print("The reversed number is:",reverse)"""
