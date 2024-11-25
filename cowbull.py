import random


def gen_game_num():
    return list(str(random.randint(1000, 9999)))
    # return list("1224")


def cow_bull(game_number, guess_input):
    """
    Calculate the number of cows and bulls for a guess.
    Bulls: Correct digit in the correct position.
    Cows: Correct digit but in the wrong position.
    """
    bulls = sum(a == b for a, b in zip(game_number, guess_input))
    # Count cows by using the minimum count of each digit in both game_number and guess_input,
    # then subtract bulls to avoid double-counting.
    cows = sum(min(game_number.count(digit), guess_input.count(digit))
               for digit in set(guess_input)) - bulls
    return bulls, cows


def cow_bull_game():

    print("Welcome to Cows and Bulls!")
    print("Bulls are correct digits in correct positions.")
    print("Cows are correct digits but in incorrect positions.")
    print("If both are zero, then you did not get any digit right.")

    game_num = gen_game_num()
    attempts = 0

    while True:
        guess_input = input("Enter your 4-digit guess: ")

        # validating input
        if len(guess_input) != 4 or not guess_input.isdigit():
            print("Please enter a valid 4-digit number.")
            continue

        attempts += 1
        bulls, cows = cow_bull(game_num, guess_input)

        if bulls == 4:
            print(f"Congratulations! You've won, in {attempts} attempts.")
            break
        else:
            print(f"You got {bulls} bull(s) and {cows} cow(s)")


if __name__ == "__main__":
    choice = 'y'
    while choice != 'n':
        cow_bull_game()
        choice = input("Would you like to play again? (y/n) : ").lower()
