import random

number=random.randint(1,9)

print("Number Guessing Game")

guess=input("enter your guess")

chances = 5

while chances<5:

    if guess==number:
        print("CONRAGULATIONS YOU WON")
        break

    elif chances ==0:
        print("YOU LOSE the number is", number)
