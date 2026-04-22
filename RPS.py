import sys
import random
from enum import Enum

def rps(name ="PlayerOne"):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_rps():
        nonlocal game_count
        nonlocal player_wins
        nonlocal computer_wins

        class rps(Enum):
            rock = 1
            papper = 2
            scissor = 3

        player_choice = input(f"{name} please enter \n 1 for Rock \n 2 for Paper \n 3 for Scissors \n")

        if player_choice not in ["1","2","3"]:
            print(f"{name} please enter 1,2 or 3.")
            play_rps()
        
        player = int(player_choice)

        computer_choice = random.choice("123")

        computer = int(computer_choice)

        

    
