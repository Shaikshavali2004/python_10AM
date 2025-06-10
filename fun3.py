#Argument Types: Four Types
"""
1.Positional Argumnets
2.Keyword Arguments
3.Default Argumnets
4.Variable Length Arguments
"""

#1.Positional Argumnets

def calc(a,b):
    print(b-a)

calc(100,200)
calc(200,100)

#2.Keyword Arguments

def calc(a,b):
    print(b-a)

calc(a=100,b=200)
calc(b=200,a=100)

#3.Default Argumnets

def calc(a,b,c=1):
    print(a+b+c)

calc(100,200,300)
calc(200,300)