import os

class Maderitas:
    def __init__(self, nombre, tipo, cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad

        carpeta_crud = "crud"
        ruta_archivo = os.path.join(carpeta_crud, 'Maderitas.txt')

        with open(ruta_archivo, 'a') as fichero:
            fichero.write(f"{self.nombre} {self.tipo} {self.cantidad}\n")


def main():


    nombre = str()
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
    
    while cantidad <= 0:

        print("Ingresa la cantidad de piezas")
        cantidad = int(input("Cantidad: "))
        if cantidad == 0:
            os.system('clear')
            print("La cantidad no debe ser 0!!")

    Maderitas(nombre, tipo, cantidad)

    print("Pieza agregada exitosamente!!")



if __name__ == "__main__":
    main()