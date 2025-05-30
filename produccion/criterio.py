import os

def procesar_linea(partes):
    """
    Procesa una línea del archivo y retorna (nombre, tipo, cantidad)
    Los últimos 2 elementos son tipo y cantidad
    Todo lo demás forma parte del nombre
    """
    if len(partes) < 4:
        return None, None, None
        
    cantidad = int(partes[-1])
    tiempo = int(partes[-2])
    tipo = partes[-3]
    nombre = " ".join(partes[:-3])
    
    return nombre, tipo, tiempo, cantidad

def cargar_y_mostrar_productos(orden='FIFO'):
    
    productos = {}
    
    ruta_archivo = os.path.join(os.path.dirname(__file__), '..', 'crud', 'Maderitas.txt')
    ruta_archivo = os.path.abspath(ruta_archivo)

    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo {ruta_archivo} no existe.")
        return


    with open(ruta_archivo, 'r') as fichero:
        lineas = fichero.readlines()


    if orden == 'LIFO':
        lineas = reversed(lineas)

    for numero_linea, linea in enumerate(lineas, 1):
        partes = linea.strip().split()
        nombre, tipo, tiempo, cantidad = procesar_linea(partes)

        if not nombre or tipo not in ["Macho", "Hembra"]:
            print(f"Línea {numero_linea} inválida: '{linea.strip()}'")
            continue

        if nombre not in productos:
            productos[nombre] = {}

        productos[nombre][tipo] = {
            "cantidad": cantidad,
            "tiempo": tiempo
        }

    if not productos:
        print("No hay productos para mostrar.")
        return

    for nombre, tipos in productos.items():
        print(f"\n{nombre}:")
        for tipo, data in tipos.items():
            print(f"\t{tipo}: {data['cantidad']} unidades ({data['tiempo']} min)")


def main():

    opcion = input("Seleccione el orden (FIFO/LIFO): ").strip().upper()
    cargar_y_mostrar_productos(orden=opcion if opcion in ["FIFO", "LIFO"] else 'FIFO')



if __name__ == "__main__":
    main()
