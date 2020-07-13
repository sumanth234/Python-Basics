#List Comprehension
print("List Comprehensions\n")

friends = ["Rolf","John","Rob"]

print([friend.lower() for friend in friends]) #prints new array with friends name as lowercase

print('\n')

#Conditional List comprehension

numbers = [1,2,3,4,5,6,7]

print("OddNumbers : ", [number for number in numbers if number%2 != 0])

print("EvenNumbers : ",[number for number in numbers if number%2 == 0])

number1 = [1,2,3,4,5]
number2 = [2,3,5,7]

print("common numbers on both arrays : ", [number for number in number1 if number in number2])

print('\n')

# Multiple list Comprehesions

friends = ["Rolf","John","Rob"]
guests = ["rolf","george","Rob"]

friends_lower = [friend.lower() for friend in friends]
print("friends who are in as guest are :",[guest.title() for guest in guests if guest.lower() in friends_lower ])
#or
print(f"friends who are in as guest are : {[guest.title() for guest in guests if guest.lower() in friends_lower ]}")

#Set Comprehensions

print('\n-----------------------------\n')

print("Set Comprehensions\n")

friends = ["Rolf","John","Rob"] # can be either set or list
guests = {"rolf","george","Rob"}

friends_lower = {friend.lower() for friend in friends}
guests_lower = {guest.lower() for guest in guests}

print("friends who are in as guest are :", {friend.title() for friend in friends_lower.intersection(guests_lower)})

#Dictionary Comprehension

print('\n-----------------------------\n')

print("Dictionary Comprehensions\n")

friends = ["Rolf","John","Rob"]
age = [23,45,34]

friends_dictionary = {
    friends[i] : age[i]
    for i in range(len(friends))
    if age[i] > 25
}

print(friends_dictionary)





