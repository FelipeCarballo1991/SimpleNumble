from random import randint,choice
import os, sys

colors = {

    "green":"\033[92m",
    "yellow":"\033[93m",
    "red":"\033[91m",
    "ENDC":"\033[0m",

}

def color_letter(letter,color):
    return colors[color] + letter + colors["ENDC"]

def cleaning():

    """
    Limpia la consola de comandos

    """
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')

rojo = color_letter("NUM","red")
verde = color_letter("NUM","green")
amarillo =color_letter("NUM","yellow") 


def menu():
    cleaning()
    print("\nNUMDLE\nREGLAS DE JUEGO:")
    print(f"{verde} CORRECTO")
    print(f"{amarillo} OTRA POSICION")
    print(f"{rojo} INCORRECTO")
    print("Ingrese un numero de 6 digitos para empezar:")


def numeroAleatorio(cantidad):
    """
    Genera un numero aleatorio
    Si el numero es menor a 10 digitos no repite cifras.    

    Args:
        cantidad (int): Digitos del numero a generar.

    Returns:
        [int]: Retorna un numero entero de [cantidad] cifras.
    """
    cadena = [numero for numero in range(0,10,1)]
    
    numero = ""
    for i in range (cantidad):
        numRandom = choice(cadena) 
        cadena.remove(numRandom)
        numero += str(numRandom)

        if len(cadena) == 0: #por si hacemos un numero de mas cifras
            cadena = [numero for numero in range(0,10,1)]

    return numero

def crearTablero():
    board = []
    for i in range (6):
        board.append(["_" for i in range(6)])
    
    return board



def gameLoop():

    numero = numeroAleatorio(6) 
    win = False
    board = crearTablero()
    game_loop_counter = 0

        
    while (not win) and (game_loop_counter<6):
        texto = input("")
        while len(texto) != len(numero):
            print(f"ERROR: el numero debe tener {len(numero)} digitos")
            texto = input("")

        #win logic
        if numero == texto:        
            board[game_loop_counter] = [color_letter(letra,"green") for letra in texto]
            win = True   
        #numero in numero
        else:
            test_line = []
            for i in range (len(numero)):
                if numero[i] == texto[i]:
                    test_line.append(color_letter(texto[i],"green"))
                elif texto[i] in numero:               
                    indice_numero = numero.index(numero[i])
                    indice_texto = texto.index(texto[i])
                    if indice_numero != indice_texto:              
                        test_line.append(color_letter(texto[i],"red"))
                    else:
                        test_line.append(color_letter(texto[i],"yellow"))                
                else:
                    test_line.append(color_letter(texto[i],"red"))
                    
            board[game_loop_counter] = test_line


        #Dibujo del tablero
        for i in range (6):
            print(" ".join(board[i]))

        game_loop_counter +=1

    if win:
        print("GANASTE")
        print(f"NUMERO: {numero}")
    else:
        print("GAME OVER")
        print(f"NUMERO: {numero}")
        