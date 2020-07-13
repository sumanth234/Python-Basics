import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

print('\n-----------------------------\n')

print("Method 1: \n")

name = [player['name'] for player in players]
numbers = [player['numbers'] for player in players]

print(numbers)

matched_numbers = []

for i,num in enumerate(numbers):
    num2 = []
    for j in num:
        if j in lottery_numbers:
            num2.append(j)
    else:
        matched_numbers.append(num2)


high = []

for i in range(len(matched_numbers)):
    for j in range(i,len(matched_numbers)):
        if len(matched_numbers[i]) > len(matched_numbers[j]):
            if len(matched_numbers[i]) > len(high):
                high = matched_numbers[i]
                high_name = name[i]
        elif len(matched_numbers[j]) > len(high):
            high = matched_numbers[j]
            high_name = name[j]

print(f"{high_name} won {100 ** len(high)}")

print('\n-----------------------------\n')

print("Method 2 : \n")


print("lottery_numbers : " ,lottery_numbers)
print("numbers Array : ", [player["numbers"] for player in players])
print("Intersected Array : ", [player['numbers'].intersection(lottery_numbers) for player in players])

name = [player['name'] for player in players]
numbers = [len(player['numbers'].intersection(lottery_numbers)) for player in players]
#numbers = [{player["name"],len(player['numbers'].intersection(lottery_numbers))} for player in players]


print(name[numbers.index(max(numbers))] + " won " + str(100 ** max(numbers)))









