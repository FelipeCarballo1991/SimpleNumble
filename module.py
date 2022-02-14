from random import randint,choice
import os, sys

colors = {

    "green":"\033[92m",
    "yellow":"\033[93m",
    "red":"\033[91m",
    "ENDC":"\033[0m",

}

def color_letter(letter,color):
    """Pinta de un color una variable del tipo str.

    Args:
        letter ([type]): string
        color ([type]): dict

    Returns:
        [type]: string
    """
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


def menu(unNumero):
    """Imprime por consola el menu de inicio del juego. 
       Se le pasa por parametro la cantidad de digitos del numero a descubrir


    Args:
        unNumero (): int
    """
    cleaning()
    print("\nNUMDLE\nREGLAS DE JUEGO:")
    print(f"{verde} CORRECTO")
    print(f"{amarillo} OTRA POSICION")
    print(f"{rojo} INCORRECTO")
    print(f"Ingrese un numero de {unNumero} digitos para empezar:")


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

def crearTablero(unNumero):
    """Crea un tablero con unNumero de ancho. 

    Args:
        unNumero ([type]): int

    Returns:
        [type]: list
    """
    board = []
    for i in range (unNumero):
        board.append(["_" for i in range(unNumero)])
    
    return board



def gameLoop(unNumero):
    """Funcion de alto nivel que realiza un loop del juego. Se le debe pasar como parametro
       el tamaño del numero a descubrir

    Args:
        unNumero ([type]): int
    """


    numero = numeroAleatorio(unNumero) 
    win = False
    board = crearTablero(unNumero)
    game_loop_counter = 0

    menu(unNumero)

        
    while (not win) and (game_loop_counter<unNumero):
        numeroCompleto = input("")
        while len(numeroCompleto) != len(numero):
            print(f"ERROR: el numero debe tener {len(numero)} digitos")
            numeroCompleto = input("")

        #win logic
        if numero == numeroCompleto:        
            board[game_loop_counter] = [color_letter(digito,"green") for digito in numeroCompleto]
            win = True   
        #numero in numero
        else:
            test_line = []
            for i in range (len(numero)):
                if numero[i] == numeroCompleto[i]:
                    test_line.append(color_letter(numeroCompleto[i],"green"))
                elif numeroCompleto[i] in numero:               
                    indice_numero = numero.index(numero[i])
                    indice_texto = numeroCompleto.index(numeroCompleto[i])
                    if indice_numero != indice_texto:              
                        test_line.append(color_letter(numeroCompleto[i],"red"))
                    else:
                        test_line.append(color_letter(numeroCompleto[i],"yellow"))                
                else:
                    test_line.append(color_letter(numeroCompleto[i],"red"))
                    
            board[game_loop_counter] = test_line


        #Dibujo del tablero
        for i in range (unNumero):
            print(" ".join(board[i]))

        game_loop_counter +=1

    if win:
        print("GANASTE")
        print(f"NUMERO: {numero}")
    else:
        print("GAME OVER")
        print(f"NUMERO: {numero}")
        