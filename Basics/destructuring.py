#Destructuring

#List
friends = [("Rolf",23),("John",45),("Rob",34)]

for name,age in friends: # destructuring friends[0] with name and age
    print(f"Age of {name} is {age}") # f string converts integer and you can use it directly within f string
    # or
    print("Age of "+ name + " is " + str(age)) # If using f string, no need to use str()

print('\n-----------------------------\n')

#Dictionary
friends = {"Rolf":23,"John":45,"Rob":34}

for name in friends:  #if you search for only one value i.e, name, it prints only keys of dictionary
    print(name)

for name,age in friends.items(): # you can only access using .items()
    print(f"Age of {name} is {age}")