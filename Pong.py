def main():
    while True:
        print("Menu de Inicio")  # Imprime el título del menu
        print("1. Jugar")  # Imprime la opción 1: Jugar
        print("2. Salir")  # Imprime la opción 2: Salir
        
        choice = input("Selecciona una opción (1 o 2): ").strip()  # Solicita al usuario que seleccione una opción y elimina espacios en blanco
        
        if choice == '1':
            print("¡Comenzando Juego!")  # Si la opción es '1', imprime el mensaje de "Comenzando Juego"

            break  # Sale del bucle y termina el programa (Despues de esto debo hacer que inicie el juego)
        elif choice == '2':
            print("Saliendo del juego...")  # Si la opción es '2', imprime el mensaje de "Saliendo del Juego"
            break  # Sale del bucle y termina el programa
        else:
            print("Opción no válida. Inténtalo de nuevo.")  # Si selecciona una opción no válida imprime el mensaje de "Error"
if __name__ == "__main__":
    main()  # Llama a la función main para iniciar el programa
#ahora si se sincroniza
