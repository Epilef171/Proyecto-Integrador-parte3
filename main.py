import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    numero = 0

    while numero < 50:
        key = input('Presiona "n" para incrementar el número o "q" para salir: ')
        clear_terminal()

        if key == 'n':
            numero += 1
        elif key == 'q':
            break

        print(f'Número: {numero}')

if __name__ == "__main__":
    main()
