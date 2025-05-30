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

def cargar_productos():
    """
    Lee el archivo y retorna un diccionario con los productos y sus cantidades
    """
    productos = {}
    carpeta_crud = "crud"
    ruta_archivo = os.path.join(carpeta_crud, 'Maderitas.txt')

    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo {ruta_archivo} no existe.")
        return productos

    with open(ruta_archivo, 'r') as fichero:
        for numero_linea, linea in enumerate(fichero, 1):
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

    return productos

def mostrar_producto(nombre_buscar=None, tipo_buscar=None):
    productos = cargar_productos()

    if not productos:
        print("No hay productos para mostrar.")
        return

    if nombre_buscar:
        if nombre_buscar in productos:
            print(f"\n{nombre_buscar}:")
            if tipo_buscar:
                data = productos[nombre_buscar].get(tipo_buscar)
                if data:
                    print(f"\t{tipo_buscar}: {data['cantidad']} unidades ({data['tiempo']} min)")
                else:
                    print(f"\t{tipo_buscar}: no disponible")
            else:
                for tipo, data in productos[nombre_buscar].items():
                    print(f"\t{tipo}: {data['cantidad']} unidades ({data['tiempo']} min)")
        else:
            print(f"No se encontró el producto '{nombre_buscar}'")
    else:
        for nombre, tipos in productos.items():
            print(f"\n{nombre}:")
            for tipo, data in tipos.items():
                print(f"\t{tipo}: {data['cantidad']} unidades ({data['tiempo']} min)")

def main():
    print("\tListado de productos")
    print("\t---------------------")
    mostrar_producto()

if __name__ == "__main__":
    main()
