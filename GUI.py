from tkinter import *
import tkinter.messagebox as messagebox
import os
from crud import create, read, update, delete
from auth import Users

ventana = Tk()
ventana.title("Inventario")
ventana.resizable(0,0)

def on_off_main(switch:bool):
    if switch:
        botonActualizar.configure(state=NORMAL)
        botonAgregar.configure(state=NORMAL)
        botonEliminar.configure(state=NORMAL)
    else:
        botonActualizar.configure(state=DISABLED)
        botonAgregar.configure(state=DISABLED)
        botonEliminar.configure(state=DISABLED)

###---------------ventanas------------###
##----------Ventana principal----------##
#botones
botonAgregar = Button(ventana,text='Agregar',\
    width=8, height=1,command=lambda:extra_gui(0))
botonActualizar = Button(ventana,text='Actualizar',\
    width=8, height=1,command=lambda:extra_gui(1))
botonEliminar = Button(ventana,text='Eliminar',\
    width=8, height=1,command=lambda:extra_gui(2))
botonActualizar.grid(row=1,column=0,padx=5,pady=5)
botonAgregar.grid(row=1,column=1,padx=5,pady=5)
botonEliminar.grid(row=1,column=2,padx=5,pady=5)
on_off_main(True) #DEBUG MODE

##---------------Inicio------------##
new_register_win = Toplevel(ventana)
new_register_win.transient(ventana)
new_register_win.title('registro de usuario')

#textos
registro_texto=Label(new_register_win,text='¿Desea añadir un nuevo usuario?')
registro_texto.grid(row=0,column=0,padx=5,pady=5)
#botones
confirmar=Button(new_register_win,text='Confirmar',\
    width=8,height=1,command=lambda:new_user())
cancelar=Button(new_register_win,text='Cancelar',\
    width=8,height=1,command=lambda:[new_register_win.destroy(),login()])
confirmar.grid(row=1,column=0,padx=5,pady=5)
cancelar.grid(row=1,column=2,padx=5,pady=5)

##------------------Login-----------##
def login():
    login_win = Toplevel(ventana)
    login_win.transient(ventana)
    login_win.title('inicio de sesión')
    
    #Entradas
    usuario=Entry(login_win)
    contrasena = Entry(login_win)
    usuario.grid(row=0,column=1,padx=5,pady=5)
    contrasena.grid(row=1,column=1,padx=5,pady=5)
    #Textos
    usuario_texto=Label(login_win,text='Usuario')
    contrasena_texto=Label(login_win,text='Contraseña')
    usuario_texto.grid(row=0,column=0,padx=5,pady=5)
    contrasena_texto.grid(row=1,column=0,padx=5,pady=5)
    #botones
    confirmar = Button(login_win,text='Confirmar',\
        width=8,height=1,command=lambda:login_ver())
    confirmar.grid(row=1,column=2,padx=5,pady=5)

    def login_ver():
        if Users.verificarLogin(usuario.get(),contrasena.get()):
            messagebox.showinfo(title=None,message='Inicio de sesión exitoso')
            on_off_main(True)
            login_win.destroy()
            return True
        else:
            messagebox.showerror(title=None,message='Datos incorrectos')
            return False
  
  
##-----Registro-----##
def new_user():
    new_register_win.destroy()
    register_win = Toplevel(ventana)
    register_win.transient(ventana)
    register_win.title('Registro de usuario')
    
    #Entradas    
    nombre = Entry(register_win)
    apellido = Entry(register_win)
    username = Entry(register_win)
    password = Entry(register_win)
    nombre.grid(row=0,column=1,padx=5,pady=5)
    apellido.grid(row=1,column=1,padx=5,pady=5)
    username.grid(row=2,column=1,padx=5,pady=5)
    password.grid(row=3,column=1,padx=5,pady=5)
    
    #Textos
    nombre_texto=Label(register_win,text='Nombre')
    apellido_texto=Label(register_win,text='Apellidos')
    username_texto=Label(register_win,text='Usuario')
    password_texto=Label(register_win,text='Contraseña')
    nombre_texto.grid(row=0,column=0,padx=5,pady=5)
    apellido_texto.grid(row=1,column=0,padx=5,pady=5)
    username_texto.grid(row=2,column=0,padx=5,pady=5)
    password_texto.grid(row=3,column=0,padx=5,pady=5)
    #botones
    confirmar=Button(register_win,text='Confirmar',\
        width=8,height=1,\
            command=lambda:[Users(nombre.get(),apellido.get(),username.get(),password.get()),\
                messagebox.showinfo(title=None, message='Registro de Usuario exitoso'),\
                    login(),register_win.destroy()])
    confirmar.grid(row=1,column=2,padx=5,pady=5)
    
####---------------------GUIA2-----------------####
from crud.create import Maderitas
def extra_gui(fun):
    on_off_main(False)
    extra_win = Toplevel(ventana)
    extra_win.transient(ventana)
    extra_win.title('Creación de piezas')

    
    var = StringVar(value='None')

    #Tipo de pieza
    texto=Label(extra_win,text='Escribe el nombre de la pieza. \n\
                ¡Ojo! El programa es sensible a mayúsculas y signos de puntuación.')
    texto.pack(anchor='center')

    nombre_boton = Entry(extra_win)
    nombre_boton.pack(anchor='center')
    #Macho Hembra
    texto_2=Label(extra_win,text='Escoge si es macho o hembra')
    texto_2.pack(anchor='center')

    macho_button = Radiobutton(extra_win,text='Macho',variable=var,value='Macho').\
        pack(anchor='center')
    hembra_button = Radiobutton(extra_win,text='Hembra',variable=var,value='Hembra').\
        pack(anchor='center')
    
    #Cantidad
    texto_3=Label(extra_win,text='Ingresa una cantidad')
    texto_3.pack(anchor='center')

    cantidad = Entry(extra_win)
    cantidad.pack(anchor='center')
    #Confirmación
    match fun:
        case 0: #agregar
            confirmar = Button(extra_win,text='Confirmar',\
                width=8,height=1,command=lambda:[create_piece(nombre_boton.get(),var.get(),cantidad.get()),extra_win.destroy()]).pack(side='left')
            cancelar = Button(extra_win,text='Cancelar',\
                width=8,height=1,command=lambda:[on_off_main(True),extra_win.destroy()]).pack(side='right')
        case 1:
            confirmar = Button(extra_win,text='Confirmar',\
                width=8,height=1,command=lambda:[create_piece(var.get(),var.get(),cantidad.get()),extra_win.destroy()]).pack(side='left')
            cancelar = Button(extra_win,text='Cancelar',\
                width=8,height=1,command=lambda:[on_off_main(True),extra_win.destroy()]).pack(side='right')
        case 2:
            confirmar = Button(extra_win,text='Confirmar',\
                width=8,height=1,command=lambda:[del_piece(var.get(),var.get(),cantidad.get()),extra_win.destroy()]).pack(side='left')
            cancelar = Button(extra_win,text='Cancelar',\
                width=8,height=1,command=lambda:[on_off_main(True),extra_win.destroy()]).pack(side='right')
            
def create_piece(nombre,tipo,cantidad): 
    if cantidad =='' or nombre=='':
        messagebox.showerror(message='Faltan datos')
        return None
    if nombre in productos:
        messagebox.showerror(message='Pieza ya existe!')
        return None
    cantidad = int(cantidad)
    if cantidad <= 0:
        messagebox.showerror(message='¡El valor debe ser mayor que 0!')
        return None
    else:
        Maderitas(nombre,tipo,cantidad)
        messagebox.showinfo(message='¡Creado exitosamente!')
        on_off_main(True)
        table_update()

####---------------------GUIA3-----------------####
from crud.read import *
def table_update():
    carpeta_crud = "crud"
    ruta_archivo = os.path.join(carpeta_crud, 'Maderitas.txt')

    if not os.path.exists(carpeta_crud):
        print(f"Error: La carpeta {carpeta_crud} no existe")
        
    if not os.path.exists(ruta_archivo):
        print(f"Error: El archivo {ruta_archivo} no existe")

    global productos
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

    # Mostrar resultados
    columns_table = [[],[],[]]
    for nombre, tipos in productos.items():
        columns_table[0].append(nombre)
        columns_table[0].append(nombre)
        for tipo, cantidad in tipos.items():
            columns_table[1].append(tipo)
            columns_table[2].append(cantidad)

    for i in range(0,len(productos.items())*2):
        for j in range(0,3):
            e = Entry(ventana, width=10, font=('Arial', 16, 'bold'))
            e.grid(row=i+2, column=j)
            e.insert(END,columns_table[j][i])
            e.configure(state=DISABLED)

table_update()

####---------------------GUIA4-----------------####
# def edit_table(nombre,tipo,cantidad):
#     if login():

#         return
#     else:
#         return
# extra_gui(0)
def del_piece(nombre,tipo,cantidad): 
    if cantidad =='':
        messagebox.showerror(message='Faltan datos')
        return None
    cantidad = int(cantidad)
    if cantidad >= 0:
        messagebox.showerror(message='¡El valor debe ser menor que 0!')
        return None
    else:
        Maderitas(nombre,tipo,cantidad)
        messagebox.showinfo(message='¡Borrado exitosamente!')
        on_off_main(True)
        table_update()



ventana.mainloop()
