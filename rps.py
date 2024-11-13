# What functions do we need

# choose_random - choose a random choice for the computer
import random


def choose_random():
    return random.randint(0,2)
# check_win - COmpare user input to ocmputer input and determine the winner
def check_win(input_1, input_2):
    win_options = ["Tie!", "Win!", "Lose!"]
    diff = input_1 - input_2
    return win_options[diff % 3]

    if diff == 0:
        return "Tie!"
    elif diff % 3 == 2:
        return "Loss!"
    elif diff % 3 == 1:
        return "Win!"
    else:
        return "Something went wrong!"


#def check_win(input_1, input_2):
    #if input_1 == input_2:
        return "Tie!"
    #elif input_1 == 0 and input_2 == 1:
        return "Lose!"
    #elif input_1 == 0 and input_2 == 2:
        return "Win!"
    #elif input_1 == 1 and input_2 == 0:
        return "Win!"
    #elif input_1 == 1 and input_2 == 2:
        return "Loss!"
    #elif input_1 == 2 and input_2 == 1:
        return "Win!"
    #elif input_1 == 2 and input_2 == 0:
        return "Lose!"
    #else:
        #return "someting went wrong...1"

# get_user_input - Get user input, ensure it is a valid choice. If it's not valid, Tell them it's not valid and asl them again!

def get_user_input():
    valid_input = False
    while not valid_input:
        user_input = input("Rock(0), Paper(1), Scissors(2). (q) to quit: ")
        if user_input == "q":
            return user_input
        elif user_input == "0" or user_input == "1" or user_input == "2":            
            valid_input = True
            return int(user_input)
        else:
            print("Invalid Input! Try Again!")

# keep_score



# display_score

#game_loop

game_going = True
options = ["Rock", "Paper", "Scissors"]
while game_going:
    user_input = get_user_input()
    if user_input == "q":
        break
    computer_input = choose_random()

    print(check_win(user_input, computer_input))
    print(f"You chose: {user_input}. Computer chose: {computer_input}.")
    # game_going = False


