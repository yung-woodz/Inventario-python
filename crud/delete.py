import os
from auth import Admin as ad2

class Maderitas:
    def __init__(self, nombre, tipo, cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad
        self.ruta_archivo = os.path.join("crud", "Maderitas.txt")
            
    def eliminar(self, nombre, tipo, cantidad):
        producto_encontrado = False
        
        try:
            # Leer el archivo original
            with open(self.ruta_archivo, 'r') as fichero:
                lines = fichero.readlines()
            
            # Escribir en archivo temporal
            with open('eliminar.txt', 'w') as fichero1:
                for line in lines:
                    # Dividir la línea por el último espacio para obtener la cantidad
                    parts = line.strip().rsplit(' ', 1)
                    if len(parts) != 2:
                        continue
                        
                    # Dividir la parte restante por el último espacio para obtener el tipo
                    name_type = parts[0].rsplit(' ', 1)
                    if len(name_type) != 2:
                        continue
                        
                    savedName = name_type[0]
                    savedType = name_type[1]
                    savedQuantity = int(parts[1])
                    
                    if nombre == savedName and tipo == savedType:
                        producto_encontrado = True
                        removeQuantity = savedQuantity - cantidad
                        if removeQuantity > 0:
                            fichero1.write(f"{savedName} {savedType} {removeQuantity}\n")
                        elif removeQuantity == 0:
                            print(f"Eliminando completamente el producto: {savedName} {savedType}")
                        else:
                            print("No hay suficiente cantidad para eliminar")
                            fichero1.write(line)
                            return False
                    else:
                        fichero1.write(line)
            
            # Reemplazar el archivo original con el temporal
            os.replace('eliminar.txt', self.ruta_archivo)
            
            if not producto_encontrado:
                print("Producto no encontrado")
                return False
                
            return True
            
        except Exception as e:
            print(f"Error al eliminar: {str(e)}")
            return False

def main():
    # print("Que producto deseas eliminar?\n"
    #       "1. Peon\n"
    #       "2. Calabera\n"
    #       "3. Lomo Toro\n")
    
    # op1 = int(input("Opcion: "))

    print("Que producto desea eliminar?\n")
    nombre = str(input("Nombre: ").strip())
    
    # if op1 == 1:
    #     nombre = "Peon" 
    # elif op1 == 2: 
    #     nombre = "Calabera"
    # elif op1 == 3: 
    #     nombre = "Lomo Toro"
    # else:
    #     print("Opcion no valida")
    #     return
    
    print("Que tipo de pieza es?\n"
          "1. Macho\n"
          "2. Hembra\n")
    
    op2 = int(input("Opcion: "))
    
    if op2 == 1:
        tipo = "Macho"
    elif op2 == 2:
        tipo = "Hembra"
    else:
        print("Tipo de pieza no válido")
        return
    
    print("Ingresa la cantidad de piezas a eliminar")

    cantidad = int(input("Cantidad: "))

    if not str(cantidad).isdigit():
        print("Por favor ingrese un número válido para la cantidad")

    if cantidad <= 0:
        print("La cantidad debe ser mayor a 0!")
        
    print("\nSe requiere permiso de administrador\n")
    username = input("Username: ")
    password = input("Contraseña: ")

    if ad2.verificarLogin(username, password):
            
        # Crear instancia y ejecutar eliminación
        maderitas = Maderitas(nombre, tipo, 0)  # cantidad 0 porque solo vamos a eliminar
        if maderitas.eliminar(nombre, tipo, cantidad):
            print(f"Se eliminaron {cantidad} piezas de {nombre} tipo {tipo}")
                
    else:
        print("Administrador no autenticado")
        
    

if __name__ == "__main__":
    main()