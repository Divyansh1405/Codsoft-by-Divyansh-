import random

user_input = int(input('''Enter from the choice: 
                       1. Rock
                       2. Paper
                       3. Scissor 
                       '''))

comp_input = random.randint(1,3)

print("You choose", user_input )
print("Computer choose ", comp_input)

if user_input == comp_input:
    print("It's a tie.")
elif user_input == 1 and comp_input == 3:
    print("User Wins.")
elif user_input == 2 and comp_input == 1:
    print("User Wins.")
elif user_input == 3 and comp_input == 2:
    print("User Wins.")
else:
    print("Computer Wins.")