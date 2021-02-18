""" The objective of this project is to make a dice simulator for two players
and on running the simulator the dices should give out a random value between 
0 to 6 and based on the each dice value should return which player 
won or the game tied """
import random

def dice():
    dice_value = random.randint(0,6)
    return dice_value

start = input("Shall we start the game ans yes or no ?")
if(start.lower() == "yes"):
    player1 = dice()
    print(f'Player 1 value is {player1}')
    player2 = dice()
    print(f'player 2 value is {player2}')
    if(player1 == player2):
        print("Player 1 wins")
    elif(player1 < player2):
        print("Player 2 wins")
    else:
        print("Player 1 and player 2 ties")
else:
    print("Closing the game")
    quit()

