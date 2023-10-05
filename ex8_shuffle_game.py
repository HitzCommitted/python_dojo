from random import shuffle


def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


def player_guess():
    guess = ""

    while guess not in ["1", "2", "3"]:
        guess = input("Choose a number 1, 2, 3: ")

    return int(guess)


def check_guess(shuffled_list, guess):
    if shuffled_list[guess - 1] == "O":
        print("YOU HAVE WON!!")
    else:
        print("Wrong guess :-(")


# Initial list
my_list = ["X", "O", "X"]

# Shuffle list
shuffled_list = shuffle_list(my_list)

# User guess
guess = player_guess()

# Check guess
check_guess(shuffled_list, guess)
