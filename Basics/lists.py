
numbers = [1,1,1,1,1]
print('lists - ',numbers[1])#1

numbers[2] = 5
print('insert - ',numbers)#[1,1,5,1,1]

numbers = [1,1,1,1,1]
newnumbers = [2,2,2,2,2]

print('concat - ', numbers+newnumbers) #[1,1,1,1,1,2,2,2,2,2]

print('multiply - ', numbers*3) #[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

fruits = ["apple",'grapes','orange']

print('check for item in list - ','orange' in fruits) #True

fruits.append('banana') # add value to list at the end

print('append - ',fruits) #['apple', 'grapes', 'orange', 'banana']

print('length - ',len(fruits)) #4

fruits.insert(2,'mango') #inserts at specified index

print('insert - ',fruits) #['apple', 'grapes', 'mango', 'orange', 'banana']

print('index of item Mango - ',fruits.index('mango')) #2