import os

# Dimensiones del juego (tamano de las raquetas y escenario)
WIDTH, HEIGHT = 40, 20
PADDLE_HEIGHT = 4

# Posiciones iniciales (En donde van a estar ubicadas las paletas al iniciar partida)
paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_x, ball_y = WIDTH // 2, HEIGHT // 2

# Dibujar el campo de juego 
def draw():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x == 1 and paddle1_y <= y < paddle1_y + PADDLE_HEIGHT) or \
               (x == WIDTH - 2 and paddle2_y <= y < paddle2_y + PADDLE_HEIGHT):
                print('|', end='')
            elif x == ball_x and y == ball_y:
                print('O', end='')
            else:
                print(' ', end='')
        print()

# Función para mostrar el juego una sola vez
def play_game():
    draw()

# Menú principal
def main():
    while True:
        print("Menu de Inicio")
        print("1. Jugar")
        print("2. Salir")
        
        choice = input("Selecciona una opcion (1 o 2): ").strip()
        
        if choice == '1':
            print("¡Comenzando Juego!")
            play_game()
            break
        elif choice == '2':
            print("Saliendo del juego...")
            break
        else:
            print("Opcion no valida. Intentalo de nuevo.")

if __name__ == "__main__":
    main()
