import random
class RockPaperScissor:
    def __init__(self):
        self.menu()

    def menu(self):

        user_input = input('''Enter from the choice: 
                            1. Rock
                            2. Paper
                            3. Scissor 
                            ''').lower()


        choices = ['rock', 'paper', 'scissor']
        comp_input = random.choice(choices)

        print("You choose", user_input)
        print("Computer choose ", comp_input)

        if user_input == comp_input:
            print("It's a tie.")
        elif user_input == 'rock' and comp_input == 'scissor':
            print("User Wins")
        elif user_input == 'paper' and comp_input == 'rock':
            print("User Wins.")
        elif user_input == 'scissor' and comp_input == 'paper':
            print("User Wins.")
        else:
            print("Computer Wins.")

        new_game = input("Do you want to play again (yes/no): ")
        if new_game == 'yes':
            return self.menu()
        else:
            print("Game Over")

obj = RockPaperScissor()
