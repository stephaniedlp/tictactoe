'''
Lógica del programa del gato
'''
import random
import board

tablero = [x for x in range(0, 9)]  # 0,1,2,3...8
tab_dict = {x: str(x) for x in tablero}


def display_tablero(tab: dict):
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("-----------")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("-----------")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")


def ia(board: dict):
    ocuppied = True
    while ocuppied == True:
        r = random.choice(list(board.keys()))
        if board[r] == str(r):  # Si está libre
            board[r] = "O"
            ocuppied = False


def juega_usuario(tab):
    turno_correcto = False
    usuario = input("Escoja celda:")
    usuario = int(usuario)
    if usuario in tab:
        if tab[usuario] == str(usuario):
            tab[usuario] = "X"
            turno_correcto = True
        else:
            print(f"Posición {usuario} ocupada")
            print("Eliga otra opción")
    return turno_correcto


def check_winner(tab, lista_lineas):
    for cmb in lista_lineas:
        if tab[cmb[0]] == tab[cmb[1]] == tab[cmb[2]]:
            return True
    return False


def game(tab: dict):
    diccionario = {'ganador': ''}
    lista_combinaciones = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    turnos = 0
    while turnos < 8:
        board.print_board(tab)

        if turnos % 2 == 0:
            correcto = board.juega_usuario(tab)
            symbol = 'X'
            player = 'Jugador/a'
        else:
            ia(tab)
            symbol = 'O'
            player = 'IA'

        turnos += 1
        gana = check_winner(tab, lista_combinaciones)

        if gana:
            diccionario['ganador'] = player
            print(f"¡Ganó {player}!")
            break

    if not diccionario['ganador']:
        print("¡Empate!")

    display_score(scores, diccionario)
    board.print_board(tab)

    return diccionario
'''
        correcto = board.juega_usuario(tab)
        if correcto:
            turnos += 1
            gana = check_winner(tab, lista_combinaciones)
            if gana == True:
                diccionario['ganador'] = "Jugador/a"
                print("¡Ganaste!")
                break
            ia(tab)
            gana = check_winner(tab, lista_combinaciones)
            if gana == True:
                diccionario['ganador'] = 'IA'
                print("¡Ganó la IA!")
                break
            turnos += 1
    board.print_board(tab)
    return diccionario
'''

def jugar_otra_vez():
    jugar = True
    otra_vez = input("¿Quieres jugar otra vez? (S/N)")
    otra_vez = otra_vez.upper()
    if (otra_vez != 'S'):
        jugar = False
        print("¡Gracias por jugar!")
    return jugar


def display_score(s: dict, d: dict):
    '''
        s = diccionario de scores keys = 'Jugador/a', 'IA', 'Empates' | values = Número de juegos
        d = diccionario con el ganador del juego anterior key = 'ganador'
            values = 'Jugador/a', 'IA', 'Empates'
    '''
    if d['ganador'] != '':
        print(f"Ganó:{d['ganador']}")
        s[d['ganador']] += 1
    else:
        s['Empates'] += 1
        print("¡Empate!")
    print(f"<<Jugador:{s['Jugador/a']}>> <<IA:{s['IA']}>> <<Empates:{s['Empates']}>>")


def game_cycle():
    scores = {'Jugador/a': 0, 'IA': 0, 'Empates': 0}
    jugar = True
    while jugar:
        # iniciamos el tablero
        tab_dict = {x: str(x) for x in tablero}
        # juega
        d = game(tab_dict)
        display_score(scores, d)
        jugar = jugar_otra_vez()


if __name__ == "__main__":
    game_cycle()
