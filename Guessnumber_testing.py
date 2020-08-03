import random as r


def run_guess(guess1, answer1):
    if 0 < guess1 < 11:
        if guess1 == answer1:
            print('Congo, u guessed it rite!')
            return True
        if guess1 < answer1:
            print("Too low, try with a higher number")
        if guess1 > answer1:
            print("Too high, try with a lower number")
    else:
        print("The number must be between 0 & 11")
        return False


if __name__ == '__main__':
    answer = r.randint(1, 10)
    print(answer)

    while True:
        try:
            guess = int(input("Enter a number between 1 & 10: "))
            if run_guess(guess, answer):
                break
        except ValueError:
            print("Please enter a number")
            continue
