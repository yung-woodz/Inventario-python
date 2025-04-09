with open('ola.txt', 'r') as fichero:
    lineas = fichero.readlines()
    print(lineas[0].strip())