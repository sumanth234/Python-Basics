#While Loop


# Ask the user to choose one of two options:
# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
# if they type 'q', our program should terminate.


# Let's begin by asking the user to type either 'p' or 'q'. You know how to do this using input()
# user_input = ...


# Then, begin a while loop that runs for as long as the user doesn't type 'q'.
# Inside the loop, have an if statement that checks if the user typed 'p'.
#    If they did, print "Hello"
# Still inside the loop, ask the user again
# user_input = ...

user_input = input("please enter p to continue and q to exit")

while (user_input != "q"):
    if (str(user_input) == "p"):
        print('Hello')
    user_input = input("please enter p to continue and q to exit")



