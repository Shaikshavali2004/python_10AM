"""def add():
    pass

add(10,20)"""

#TypeError: add() takes 0 positional arguments but 2 were given

def add(a,b):
    print(a+b)

add(10,20)
add(18,20)

#add(18,"JS") TypeError: unsupported operand type(s) for +: 'int' and 'str'