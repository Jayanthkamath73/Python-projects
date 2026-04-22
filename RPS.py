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

        print(f"\n {name} you chose {str(rps(player)).replace('rps.','').title()}")

        print(f"\n Python chose {str(rps(computer)).replace('rps.','').title()}")

        def decide_winner(player,computer):
            nonlocal name
            nonlocal player_wins
            nonlocal computer_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name} wins!!!"
            elif player ==2 and computer ==1:
                player_wins += 1
                return f"{name} wins!!!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name} wins!!!"
            elif player == computer :
                return "Tie game!!!"
            else :
                computer_wins += 1
                return f"Python wins... {name} sorry :/"
        game_result = decide_winner(player,computer)
        print(game_result)

        game_count += 1

        




    
