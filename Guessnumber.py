import random as r

rnum = r.randint(1, 10)
print(rnum)

while True:
    try:
        answer = int(input("Enter a number between 1 & 10: "))
        if 0 < answer < 11:
            if answer == rnum:
                print('Congo, u guessed it rite!')
                break
            if answer < rnum:
                print("Too low, try with a higher number")
            if answer > rnum:
                print("Too high, try with a lower number")
        else:
            print("The number must be between 0 & 11")
    except ValueError:
        print("Please enter a number")
        continue
