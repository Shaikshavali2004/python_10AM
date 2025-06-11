from decorator import smart_div

@smart_div
def calc(a,b):
    return a/b

print(calc(10,2)) #5.0
print(calc(10,0)) #Cannot divide by zero
print("GE")       #GE