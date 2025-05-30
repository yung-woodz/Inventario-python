import os
from auth import Admin as ad1
from crud import read

def actualizar_producto(nombre, tipo, cantidad_nueva):
    carpeta_crud = "crud"
    ruta_archivo = os.path.join(carpeta_crud, 'Maderitas.txt')
    ruta_archivo_temp = os.path.join(carpeta_crud, 'Maderitas_temp.txt')
    
    producto_encontrado = False
    
    with open(ruta_archivo, 'r') as fichero:
        with open(ruta_archivo_temp, 'w') as fichero_temp:
            for linea in fichero:
                partes = linea.strip().split()
                if len(partes) < 4:
                    continue
                
                nombre_archivo = " ".join(partes[:-3])  # Une palabras del nombre
                tipo_archivo = partes[-3]
                tiempo = int(partes[-2])
                cantidad_archivo = int(partes[-1])
                
                if nombre_archivo == nombre and tipo_archivo == tipo:
                    cantidad_total = cantidad_archivo + cantidad_nueva
                    fichero_temp.write(f"{nombre} {tipo} {tiempo} {cantidad_total}\n")
                    producto_encontrado = True
                else:
                    fichero_temp.write(linea)
                    
    os.remove(ruta_archivo)
    os.rename(ruta_archivo_temp, ruta_archivo)
    return producto_encontrado

def main():

    print("Que producto desea actualizar?\n")
    nombre = str(input("Nombre: ").strip())
    
    print("Que tipo de pieza es?\n"
          "1. Macho\n"
          "2. Hembra\n")
    
    op2 = int(input("Opcion: "))
    
    if op2 == 1:
        tipo = "Macho"
    elif op2 == 2:
        tipo = "Hembra"
    else:
        print("Opcion no valida")
        return
    
    # Mostrar solo el producto seleccionado
    print("\nInformación del producto seleccionado:")
    cantidad_actual = read.mostrar_producto(nombre, tipo)
    
    if cantidad_actual == 0:
        print("Error: Producto no encontrado o sin stock")
        return
        
    cantidad_nueva = int(input("\nIngrese la cantidad a agregar: "))

    print("\nSe requiere permiso de administrador\n")
    username = input("Username: ")
    password = input("Contraseña: ")

    if ad1.verificarLogin(username, password):
    
        if actualizar_producto(nombre, tipo, cantidad_nueva):
            print(f"\nProducto actualizado exitosamente!")

            if cantidad_actual is None:
                cantidad_actual = 0

            print(f"Nueva cantidad total: {cantidad_actual + cantidad_nueva}")
        else:
            print("Error: Producto no encontrado")
    else:
        print("Administrador no autenticado")

if __name__ == "__main__":
    main()