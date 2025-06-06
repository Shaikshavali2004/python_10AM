#  21.Program to print Fibonacci number series upto a given number.

# ExpectedOut17:-0,1,1,2,3,5,8,13

n=17
a = 0
b = 1
print("The Fibonacci Series:")
for i in range(n):
    print(a,end=" ")
    c = a+b
    a = b
    b = c


"""n=10
a=0
b=1
print("The Fibonacci Series:")
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c"""