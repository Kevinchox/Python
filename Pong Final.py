import os
import time
import msvcrt  # Usado para Windows.

# Dimensiones del juego (tamaño de las raquetas y escenario)
WIDTH, HEIGHT = 50, 10
PADDLE_HEIGHT = 3
BALL_SPEED = 0.1  # Velocidad de la pelota

# Posiciones iniciales (Dónde van a estar ubicadas las paletas y la pelota al iniciar partida)
paddle1_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
paddle2_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 1, 1  # Dirección inicial de la pelota

def draw():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
    for y in range(HEIGHT):
        line = ''
        for x in range(WIDTH):
            if (x == 1 and paddle1_y <= y < paddle1_y + PADDLE_HEIGHT) or \
               (x == WIDTH - 2 and paddle2_y <= y < paddle2_y + PADDLE_HEIGHT):
                line += '|'
            elif x == ball_x and y == ball_y:
                line += 'O'
            else:
                line += ' '
        print(line)

def get_key(): 
    if msvcrt.kbhit():
        return msvcrt.getch().decode('utf-8')
    return None

def update_paddles():
    global paddle1_y, paddle2_y

    key = get_key()
    if key == 'w' and paddle1_y > 0:
        paddle1_y -= 1
    if key == 's' and paddle1_y < HEIGHT - PADDLE_HEIGHT:
        paddle1_y += 1
    if key == 'i' and paddle2_y > 0:
        paddle2_y -= 1
    if key == 'k' and paddle2_y < HEIGHT - PADDLE_HEIGHT:
        paddle2_y += 1

def update_ball():
    global ball_x, ball_y, ball_dx, ball_dy

    ball_x += ball_dx
    ball_y += ball_dy

    # Rebote en las paredes superior e inferior
    if ball_y <= 0 or ball_y >= HEIGHT - 1:
        ball_dy *= -1

    # Rebote en las raquetas
    if (ball_x == 1 and paddle1_y <= ball_y < paddle1_y + PADDLE_HEIGHT) or \
       (ball_x == WIDTH - 2 and paddle2_y <= ball_y < paddle2_y + PADDLE_HEIGHT):
        ball_dx *= -1

    # Si la pelota sale del campo
    if ball_x <= 0 or ball_x >= WIDTH - 1:
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_dx, ball_dy = 1, 1

def play_game():
    while True:
        draw()
        update_paddles()
        update_ball()
        time.sleep(BALL_SPEED)

def main():
    while True:
        print("Menú de Inicio")
        print("1. Jugar")
        print("2. Salir")
        
        choice = input("Selecciona una opción (1 o 2): ").strip()
        
        if choice == '1':
            print("¡Comenzando Juego!")
            play_game()
            break
        elif choice == '2':
            print("Saliendo del juego...")
            break
        else:
            print("Opcion no válida. Intentalo de nuevo.")

if __name__ == "__main__":
    main()
