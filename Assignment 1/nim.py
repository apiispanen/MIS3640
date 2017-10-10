import random
from math import log

# Define constant variables.
HUMAN = 0
COMPUTER = 1
SMART = 0
DUMB = 1

# Create the initial pile, determine the starting player and the computer's
# strategy.
pile = random.randint(10, 100)
turn = random.randint(0, 1)
strategy = random.randint(0, 1)
    
def nim():
    """
    return True if the winner is human, False if winner is computer.
    """
    # While the game is still being played.
    while pile > 0:
        if strategy == COMPUTER:    
            if pile == 1:
                take = 1
            elif strategy==DUMB:
                take=random.randint(1,(1/2*(pile)))
            elif pile == 3 or pile == 7 or pile == 15 or pile == 31 or pile == 63:
                take=random.randint(1,(1/2*(pile)))
            else:
                take = random.choice([3, 7, 15, 31, 63])
            print("The computer took %d marbles, leaving %d.\n" % (take, pile))
            turn = HUMAN
        elif turn == HUMAN:
            print("Your turn.   The pile currently has", pile, "marbles in it.")
            def human_turn():
                takey = int(input("How many marbles will you take? "))
                if takey>((1/2)*pile):    
                    print('Too high, try again!')
                else:    
                    take=takey
            human_turn()
            pile=pile-take
            print("Now the pile has", pile, "marbles in it.\n")
            turn=COMPUTER
    return turn == COMPUTER
if nim()==True:
    print("You Won!")
else:
    print("The computer won!")

nim()
    