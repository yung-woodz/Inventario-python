import os
from crud import create, read, update, delete
from produccion import criterio
from auth import Users

def menu():

    op = int()
    
    while not (1 <= op <= 5):
        os.system('clear')
        print("Bienvendido al Sistema!!")
        print("\tElige una opcion\n")
        print("1. Agregar\n"
              "2. Leer\n"
              "3. Actualizar\n"
              "4. Eliminar\n"
              "5. Produccion\n")
        op = int(input("Opcion: "))

    if op == 1:
        create.main()
    elif op == 2:
        read.main()
    elif op == 3:
        update.main()
    elif op == 4:
        delete.main()
    elif op == 5:
        
        op_produccion = int()

        print("\tQue ordenamiento desea ver?\n")
        print("1. FIFO\n"
              "2. LIFO")
        
        op_produccion = int(input("Opcion: "))

        if op_produccion == 1: str_produccion = "FIFO" 
        else: str_produccion = "LIFO"

        criterio.cargar_y_mostrar_productos(orden=str_produccion)
        


def main():
    print("### Sistema de Login ###")
    choice = input("Deseas registrarte? (s/n): ").lower()

    if choice == "s":
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        username = input("Usuario: ")
        password = input("Contraseña: ")

        Users(nombre, apellidos, username, password)

        print("Registro exitoso!!")

    print("\n### Iniciar sesion ###")
    login_username = input("Usuario: ")
    login_password = input("Contraseña: ")

    if Users.verificarLogin(login_username, login_password):
        print("Login iniciado\n")
        menu()
    else:
        print("Datos incorrectos")    

if __name__ == "__main__":
    main()