# board.py
from colorama import Fore, Back, Style, Cursor
import os

def print_board(tablero):
    reset = Style.RESET_ALL
    bg = Back.WHITE
    blue = Fore.BLUE
    x_color = Fore.RED
    o_color = Fore.GREEN

    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

    def format_cell(value):
        return f"{blue}{value}{reset}" if isinstance(value, int) else f"{x_color if value == 'X' else o_color}{value}{reset}"

    print(Cursor.POS(10, 5) + f"{bg}---+---+---{reset}")
    for row in range(3):
        cells = [tablero[row * 3 + col] for col in range(3)]
        formatted_cells = "|".join(format_cell(cell) for cell in cells)
        print(Cursor.POS(10, 6 + row) + f"{bg}| {formatted_cells} |{reset}")
        print(Cursor.POS(10, 7 + row) + f"{bg}---+---+---{reset}")
    print(Style.RESET_ALL)

def juega_usuario(tablero):
    while True:
        usuario = input(Cursor.POS(10, 11) + "Escoja celda:")
        try:
            usuario = int(usuario)
            if 0 <= usuario <= 8 and tablero[usuario] == str(usuario):
                tablero[usuario] = "X"
                break
            else:
                print(f"Posición {usuario} ocupada o inválida. Elige otra opción.")
        except ValueError:
            print("Entrada no válida. Ingresa un número del 0 al 8.")

if __name__ == "__main__":
    tablero = [str(x) for x in range(9)]  # Initialize the board
    print_board(tablero)
    juega_usuario(tablero)
