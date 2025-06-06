# 23.Write a program to print the sum of first n numbers?

n = int(input("Enter a value:"))
total = 0
for i in range(1,n+1):
    total += i
print("The sum of",n,"numbers is:",total)


# Using formula method
formula_sum = n * (n + 1) // 2
print("The sum of", n, "numbers using formula is:", formula_sum)
