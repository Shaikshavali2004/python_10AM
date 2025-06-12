"""
Pyhton in-built functions:

   1.map(function,sequence)  # map is a inbuilt function,execute provided function for every element of sequence.

   2.filter(function,sequence)

   3.reduce(function,sequence)
"""

product_prices = [98,198,298,398,498]

def addone(price):
    return price+1

map_obj = map(addone, product_prices)

new_prices = list(map_obj)
print(product_prices)
print(new_prices)