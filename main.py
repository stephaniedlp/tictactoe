# main.py
from colorama import init
from game_logic import game_cycle, display_score
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    init(autoreset=True)
    play_again = True
    scores = {'Jugador/a': 0, 'IA': 0, 'Empates': 0}

    while play_again:
        clear_screen()
        game_cycle()
        display_score(scores)

        # Ask if the players want to play again
        play_again = input("¿Quieres jugar otra vez? (S/N): ").upper() == 'S'

    print("¡Gracias por jugar!")


if __name__ == "__main__":
    main()