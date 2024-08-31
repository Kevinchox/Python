 1. Importación de módulos
- `os`: Para limpiar la pantalla con `os.system()`.
- `time`: Para manejar los tiempos de pausa entre actualizaciones con `time.sleep()`.
- `msvcrt`: Para capturar teclas presionadas en Windows sin necesidad de presionar Enter.

 2. Definición de constantes
- `WIDTH` y `HEIGHT`: Definen el tamaño del área de juego.
- `PADDLE_HEIGHT`: Altura de las raquetas.
- `BALL_SPEED`: Velocidad de actualización de la pelota.

3. Inicialización de posiciones
- `paddle1_y`y `paddle2_y`: Posiciones verticales iniciales de las raquetas.
- `ball_x` y `ball_y`: Posición inicial de la pelota.
- `ball_dx` y `ball_dy`: Dirección inicial del movimiento de la pelota.

4. Función para dibujar el campo de juego
- `os.system('cls' if os.name == 'nt' else 'clear')`: Limpia la pantalla.
- Dibujo del campo: Recorre cada posición `(x, y)` y dibuja:
  - `|` para las raquetas.
  - `O` para la pelota.
  - Espacios para el resto del campo.

5. Función para capturar teclas presionadas
-`msvcrt.kbhit()`: Verifica si una tecla ha sido presionada.
- `msvcrt.getch()`: Lee la tecla presionada.

6. Actualizar la posición de las raquetas
- `get_key()`: Obtiene la tecla presionada.
- `paddle1_y`: Mueve la raqueta 1 con 'w' (arriba) y 's' (abajo).
- `paddle2_y`: Mueve la raqueta 2 con 'i' (arriba) y 'k' (abajo).

7. Actualizar la posición de la pelota
- Actualizar posición: Cambia `ball_x` y `ball_y` según `ball_dx` y `ball_dy`.
- Rebote en paredes: Invierte `ball_dy` si toca el borde superior o inferior.
- Rebote en raquetas: Invierte `ball_dx` si toca una raqueta.
- Reinicio: Si la pelota sale del campo, vuelve al centro con dirección inicial.

8. Función del juego
- Bucle principal del juego: Llama a `draw()`, `update_paddles()`, y `update_ball()` continuamente, con una pausa entre actualizaciones.

9. Menú principal
- Menú: Permite al usuario seleccionar entre jugar o salir.
- `input()`: Captura la elección del usuario.

10. Ejecución del programa
- Ejecución: Ejecuta `main()` si el script es ejecutado directamente.


Objetivo del programa:
- El programa implementa una versión básica del juego Pong en la terminal, donde dos jugadores controlan raquetas para golpear una pelota que rebota entre ellas.

2024/08/31
