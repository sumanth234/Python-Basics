#we can use else condition exclusively for loops


numbers = [1,1,1,1,1,1,1]
numbers1 = [1,2,1,1,1,1,1]

for number in numbers:
    if number == 2:
        print("Found number other than 1,Hence stopping")
        break;
    print("Found 1")
else:
    print("Not Found any other numbers other than 1") # this line is executed only if loop runs till the end without breaking inbetween

print('\n-----------------------------\n')

for number in numbers1:
    if number == 2:
        print("Found number other than 1,Hence stopping")
        break;
    print("Found 1")
else:
    print("Not Found any other numbers other than 1") # this is not printed as the loop encounters break

#Prime numbers

print('\n-----------------------------\n')

print("Print prime numbers from 2 to 100")

for n in range(2,100):
    for i in range(2,n): # we need to check only till sqrt(n) for prime numbers
        if n%i ==0:
            break
    else:
        print(n)