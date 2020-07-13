def add(a,b): # function defnition
    return a+b

def square(c):
    return c*c

print(square(add(1,2)))# function call/execution

print(square(add(2,3))) #25

#Lambda Functions

print("\n--------------------------------------\n")

add = lambda a,b : a+b
square = lambda  a : a * a

print(square(add(1,2)))

print(square(add(2,3)))