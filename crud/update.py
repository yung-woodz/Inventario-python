import os
from crud import read

def obtener_cantidad_actual(nombre, tipo):
    carpeta_crud = "crud"
    ruta_archivo = os.path.join(carpeta_crud, 'Maderitas.txt')
    
    with open(ruta_archivo, 'r') as fichero:
        for linea in fichero:
            partes = linea.strip().split()
            if len(partes) < 3:
                continue
            
            nombre_archivo = " ".join(partes[:-2])  # Une palabras del nombre
            tipo_archivo = partes[-2]
            cantidad_archivo = int(partes[-1])
            
            if nombre_archivo == nombre and tipo_archivo == tipo:
                return cantidad_archivo
    return 0

def actualizar_producto(nombre, tipo, cantidad_nueva):
    carpeta_crud = "crud"
    ruta_archivo = os.path.join(carpeta_crud, 'Maderitas.txt')
    ruta_archivo_temp = os.path.join(carpeta_crud, 'Maderitas_temp.txt')
    
    producto_encontrado = False
    
    with open(ruta_archivo, 'r') as fichero:
        with open(ruta_archivo_temp, 'w') as fichero_temp:
            for linea in fichero:
                partes = linea.strip().split()
                if len(partes) < 3:
                    continue
                
                nombre_archivo = " ".join(partes[:-2])  # Une palabras del nombre
                tipo_archivo = partes[-2]
                cantidad_archivo = int(partes[-1])
                
                if nombre_archivo == nombre and tipo_archivo == tipo:
                    cantidad_total = cantidad_archivo + cantidad_nueva
                    fichero_temp.write(f"{nombre} {tipo} {cantidad_total}\n")
                    producto_encontrado = True
                else:
                    fichero_temp.write(linea)
                    
    os.remove(ruta_archivo)
    os.rename(ruta_archivo_temp, ruta_archivo)
    return producto_encontrado

def main():
    print("Que producto desea actualizar?\n")
    print("1. Peon\n"
          "2. Calabera\n"
          "3. Lomo Toro\n")
    op1 = int(input("Opcion: "))
    
    if op1 == 1:
        nombre = "Peon"
    elif op1 == 2:
        nombre = "Calabera"
    elif op1 == 3:
        nombre = "Lomo Toro"
    else:
        print("Opcion no valida")
        return
    
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
    
    read.main()
    
    # Mostrar solo el producto seleccionado
    cantidad_actual = read.mostrar_producto(nombre, tipo)
    
    cantidad_nueva = int(input("\nIngrese la cantidad a agregar: "))
    
    if actualizar_producto(nombre, tipo, cantidad_nueva):
        print(f"\nProducto actualizado exitosamente!")
        print(f"Nueva cantidad total: {cantidad_actual + cantidad_nueva}")
    else:
        print("Error: Producto no encontrado")

if __name__ == "__main__":
    main()