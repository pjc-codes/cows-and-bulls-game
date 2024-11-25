import random


def bull_num(number, ip_number):
    ind = []
    bulls = 0
    for i in range(4):
        if number[i] == ip_number[i]:
            ind.append(i)
            bulls += 1
    return ind, bulls


def cow_num(ind, number, ip_number, cows=0):
    for i in range(4):
        for j in range(4):
            if i not in ind and j not in ind and number[i] == ip_number[j]:
                cows += 1
    return cows


def gen_number():
    # return random.sample([str(i) for i in range(10)], 4)
    return list("1324")


def get_input():
    while True:
        try:
            ip_number = input("Enter your guess: ")
            if (len(ip_number) != 4) or not (1000 <= int(ip_number) <= 9999):
                raise ValueError
            return list(ip_number)
        except ValueError:
            print("Please enter a valid 4 digit number from 1000-9999.")


def check_input(number, ip_number):
    cows = 0
    if number == ip_number:
        bulls = 4
    else:
        ind, bulls = bull_num(number, ip_number)
        cows = cow_num(ind, number, ip_number, cows=0)

    return (bulls, cows)


def cow_bull_game():
    number = gen_number()
    while True:
        ip_number = get_input()
        bulls, cows = check_input(number, ip_number)
        if bulls == 4:
            print("Congratulations! You've got the number!")
            break
        else:
            print(f"You ve got {bulls} bulls and {cows} cows.")


if __name__ == "__main__":
    choice = "y"
    while choice != "n":
        cow_bull_game()
        choice = input("Would you like to play again? (y/n) : ").lower()
