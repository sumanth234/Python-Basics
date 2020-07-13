#For Loop

print('numbers - ')
for x in range(1,11):
    print(x) #Prints numbers from 1 to 10

print('\n-----------------------------\n')

fruits = ['apple','banana','mango']

print('fruits - ')
for x in fruits:
    print(x) # prints all fruits

print('\n-----------------------------\n')

print('Even Numbers')
for x in range(2,11,2):
    print(x) #prints even numbers from 2 to 10

print('\n-----------------------------\n')

print('Odd Numbers')
for x in range(1,11,2):
    print(x) #prints odd numbers from 1 to 9

print('\n-----------------------------\n')

#While Loop

counter = 0
print('counter - ')
while(counter<=10):
    print(counter) # prints 0 to 10
    counter+=1