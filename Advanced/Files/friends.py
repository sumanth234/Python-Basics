# Ask the user for the list of 3 friends.
# For each friend, we'll tell the user whether they are nearby.
# For each nearby friend, we'll save their names to near_by friends text

people_file = open('people.txt','r')
people_list = people_file.read().splitlines()
people_file.close()

friends = input("Please enter th enames of 3 of your friends:")
friends_list = friends.split(' ')

print(people_list)
print(friends_list)
near_by_list = [friend + '\n' for friend in friends_list if people_list.__contains__(friend)]
# for friend in friends_list:
#     if people_list.__contains__(friend):
#         near_by_list.append(friend + '\n')

print(near_by_list)

near_by_friends_file = open('near_by_friends.txt','w')
near_by_friends_file.writelines(near_by_list)
near_by_friends_file.close()

