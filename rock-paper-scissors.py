# Python 3.10.1
# Encoding UTF-8
# A game of rock-paper-scissors with a tallying score

import random
import sys

print("Game Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")


win = 0
loss = 0
tie = 0


while True:
    print(f"Win: {win}\nLoss: {loss}\nTie: {tie}")

    print("""\nEnter Your Move: 
            r - rock 
            p - paper 
            s - scissors 
            q - quit""")
    UserMove = input("\n Type one of r, p, s or q : ")
    if UserMove == 'q':
        sys.exit()  # Quit the program.

    # Display what the computer choice:
    randomNumber = random.randint(1, 3)

    # Let Computer Choose it's move.
    if randomNumber == 1:
        computerMove = 'r'
        print("Rock")

    elif randomNumber == 2:
        computerMove = 'p'
        print("Paper")

    elif randomNumber == 3:
        computerMove = 's'
        print("Scissors")

    # Check Win
    if UserMove == computerMove:
        print("It is tie!")
        tie += 1
    elif UserMove == 'r' and computerMove == 's':
        print("You win!")
        win += 1
    elif UserMove == "p" and computerMove == 'r':
        win += 1
        print("You win!")
    elif UserMove == "s" and computerMove == 'p':
        win += 1
        print("You win!")
    elif UserMove == "r" and computerMove == 'p':
        loss += 1
        print("You Lose!")
    elif UserMove == "p" and computerMove == 's':
        loss += 1
        print("You Lose!")
    elif UserMove == "s" and computerMove == 'r':
        loss += 1
        print("You Lose!")
