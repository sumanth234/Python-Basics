#For Loop

print('numbers - ')
for x in range(1,11):
    print(x) #Prints numbers from 1 to 10

fruits = ['apple','banana','mango']

print('fruits - ')
for x in fruits:
    print(x) # prints all fruits

print('Even Numbers')
for x in range(2,11,2):
    print(x) #prints even numbers from 2 to 10

print('Odd Numbers')
for x in range(1,11,2):
    print(x) #prints odd numbers from 1 to 9

#While Loop

counter = 0
print('counter - ')
while(counter<=10):
    print(counter) # prints 0 to 10
    counter+=1