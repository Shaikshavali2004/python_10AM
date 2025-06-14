"""
a=10
add = lambda a,b:a+b

print(type(a))   #<class 'int'>

print(type(add))  #<class 'function'>

print(add(20,15))  #35 """

# product_prices = [98,198,298,398,498]

# new_prices = []

# for i in product_prices:
#     new_prices.append(i+1)

# print(new_prices)


# We can write above program using lambda function.

nums=[98,198,298,398,498]

print(list(map(lambda num:num+1,nums)))
