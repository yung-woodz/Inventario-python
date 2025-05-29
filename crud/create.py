import os

class Maderitas:
    def __init__(self, nombre, tipo, tiempo, cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.tiempo = tiempo
        self.cantidad = cantidad

        carpeta_crud = "crud"
        ruta_archivo = os.path.join(carpeta_crud, 'Maderitas.txt')

        with open(ruta_archivo, 'a') as fichero:
            fichero.write(f"{self.nombre} {self.tipo} {self.tiempo} {self.cantidad}\n")


def main():

    nombre = str()
    tiempo = int()
    op2 = int()
    cantidad = int()

    os.system('clear')
    print("Ingresa el nombre del producto: ")
    nombre = str(input("Nombre: ").strip())

    while not (1 <= op2 <= 2):

        os.system('clear')
        print("Que tipo de pieza es?\n"
            "1. Macho\n"
            "2. Hembra\n")
        
        op2 = int(input("Opcion: "))

    if op2 == 1:
        tipo = "Macho"
    elif op2 == 2:
        tipo = "Hembra"


    while not str(tiempo).isdigit():

        os.system('clear')
        print("Tiempo de producción (en minutos): ")
        
        tiempo = int(input())

        if not str(tiempo).isdigit():
            print("Por favor ingrese un número valido para el tiempo")

        if tiempo <= 0:
            print("El tiempo debe ser mayor a 0!")
    
    while cantidad <= 0:

        print("Ingresa la cantidad de piezas")
        cantidad = int(input("Cantidad: "))
        if cantidad == 0:
            os.system('clear')
            print("La cantidad no debe ser 0!!")

    Maderitas(nombre, tipo, tiempo, cantidad)

    print("Pieza agregada exitosamente!!")



if __name__ == "__main__":
    main()