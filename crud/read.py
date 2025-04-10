import os

def procesar_linea(partes):
    """
    Procesa una línea del archivo y retorna (nombre, tipo, cantidad)
    Los últimos 2 elementos son tipo y cantidad
    Todo lo demás forma parte del nombre
    """
    if len(partes) < 3:
        return None, None, None
        
    cantidad = partes[-1]
    tipo = partes[-2]
    nombre = " ".join(partes[:-2])
    
    return nombre, tipo, cantidad

def mostrar_producto(nombre_buscar=None, tipo_buscar=None):
    carpeta_crud = "crud"
    ruta_archivo = os.path.join(carpeta_crud, 'Maderitas.txt')
    
    productos = {
        "Peon": {"Macho": 0, "Hembra": 0},
        "Calabera": {"Macho": 0, "Hembra": 0},
        "Lomo Toro": {"Macho": 0, "Hembra": 0}
    }
    
    # Leer y sumar cantidades
    with open(ruta_archivo, 'r') as fichero:
        for linea in fichero:
            partes = linea.strip().split()
            nombre = " ".join(partes[:-2])
            tipo = partes[-2]
            cantidad = int(partes[-1])
            
            if nombre in productos and tipo in productos[nombre]:
                productos[nombre][tipo] += cantidad

    # Mostrar productos según filtros
    if nombre_buscar:
        # Mostrar solo el producto específico
        if nombre_buscar in productos:
            print(f"\n{nombre_buscar}:")
            if tipo_buscar:
                # Mostrar solo el tipo específico
                cantidad = productos[nombre_buscar][tipo_buscar]
                if cantidad > 0:
                    print(f"{tipo_buscar}: {cantidad} unidades")
                return cantidad
            else:
                # Mostrar todos los tipos del producto
                for tipo, cantidad in productos[nombre_buscar].items():
                    if cantidad > 0:
                        print(f"\t{tipo}: {cantidad} unidades")
                return sum(productos[nombre_buscar].values())
    else:
        # Mostrar todos los productos
        print("\tListado de productos")
        print("\t---------------------")
        for nombre, tipos in productos.items():
            cantidades = [cantidad for cantidad in tipos.values() if cantidad > 0]
            if cantidades:  # Solo mostrar productos con stock
                print(f"\n{nombre}:")
                for tipo, cantidad in tipos.items():
                    if cantidad > 0:
                        print(f"\t{tipo}: {cantidad} unidades")
    return 0

def main():
    print("\tListado de productos")
    print("\t---------------------")
    
    carpeta_crud = "crud"
    ruta_archivo = os.path.join(carpeta_crud, 'Maderitas.txt')
    
    # Verificar que existe la carpeta y archivo
    if not os.path.exists(carpeta_crud):
        print(f"Error: La carpeta {carpeta_crud} no existe")
        return
        
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo {ruta_archivo} no existe")
        return
    
    productos = {}
    
    try:
        with open(ruta_archivo, 'r') as fichero:
            for numero_linea, linea in enumerate(fichero, 1):
                try:
                    partes = linea.strip().split()
                    nombre, tipo, cantidad = procesar_linea(partes)
                    
                    if nombre is None:
                        print(f"Error en línea {numero_linea}: formato inválido")
                        continue
                    
                    # Inicializar producto si no existe
                    if nombre not in productos:
                        productos[nombre] = {"Macho": 0, "Hembra": 0}
                        
                    if tipo in ["Macho", "Hembra"]:
                        productos[nombre][tipo] += int(cantidad)
                    
                except ValueError:
                    print(f"Error en línea {numero_linea}: no se puede procesar")
                    continue
    
    except FileNotFoundError:
        print("Error: No se puede abrir el archivo")
        return
    
    # Mostrar resultados
    for nombre, tipos in productos.items():
        print(f"\n{nombre}:")
        for tipo, cantidad in tipos.items():
            if cantidad > 0:
                print(f"\t{tipo}: {cantidad} unidades")

if __name__ == "__main__":
    main()