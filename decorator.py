#Decorator is a function
#It takes function as an argument
#It return modified function as an argument

def smart_div(func):

    def inner(a,b):
        if b==0:
            print("Cannot divide by zero")

        else:
            return func(a,b)
        
    return inner