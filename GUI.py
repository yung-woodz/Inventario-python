from tkinter import *
import tkinter.messagebox as messagebox
import os
from crud import create, read, update, delete
from auth import Users

ventana = Tk()
ventana.title("Inventario")
ventana.geometry("450x100")
ventana.resizable(0,0)

def on_off_main(state):
    if state:
        botonLeer.configure(state=NORMAL)
        botonActualizar.configure(state=NORMAL)
        botonAgregar.configure(state=NORMAL)
        botonEliminar.configure(state=NORMAL)
    else:
        botonLeer.configure(state=DISABLED)
        botonActualizar.configure(state=DISABLED)
        botonAgregar.configure(state=DISABLED)
        botonEliminar.configure(state=DISABLED)

###---------------ventanas------------###

##----------Ventana principal----------##
#botones
botonAgregar = Button(ventana,text='Agregar',\
    width=8, height=1,command=lambda:create_gui())
botonLeer = Button(ventana,text='Leer',\
    width=8, height=1,command=lambda:read.main())
botonActualizar = Button(ventana,text='Actualizar',\
    width=8, height=1,command=lambda:update.main())
botonEliminar = Button(ventana,text='Eliminar',\
    width=8, height=1,command=lambda:delete.main())
botonLeer.grid(row=1,column=0,padx=5,pady=5)
botonActualizar.grid(row=1,column=1,padx=5,pady=5)
botonAgregar.grid(row=1,column=2,padx=5,pady=5)
botonEliminar.grid(row=1,column=3,padx=5,pady=5)
on_off_main(True)

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
    width=8,height=1,command=lambda:login())
confirmar.grid(row=1,column=0,padx=5,pady=5)
cancelar.grid(row=1,column=2,padx=5,pady=5)

##------------------Login-----------##
def login():
    new_register_win.destroy()
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
        else:
            messagebox.showerror(title=None,message='Datos incorrectos')
  
  
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

def create_gui():
    on_off_main(False)
    create_win = Toplevel(ventana)
    create_win.transient(ventana)
    create_win.title('registro de usuario')

    
    var = StringVar(value='None')
    var_2=StringVar(value='None')

    #Tipo de pieza
    texto=Label(create_win,text='Escoge el tipo de pieza')
    texto.pack(anchor='center')

    peon_button = Radiobutton(create_win,text='Peón',variable=var,value='Peón').\
        pack(anchor='center')
    calabera_button = Radiobutton(create_win,text='Calabera',variable=var,value='Calabera').\
        pack(anchor='center')
    lomo_button = Radiobutton(create_win,text='Lomo Toro',variable=var,value='Lomo Toro').\
        pack(anchor='center')
    #Macho Hembra
    texto_2=Label(create_win,text='Escoge si es macho o hembra')
    texto_2.pack(anchor='center')

    macho_button = Radiobutton(create_win,text='Macho',variable=var_2,value='Macho').\
        pack(anchor='center')
    hembra_button = Radiobutton(create_win,text='Hembra',variable=var_2,value='Hembra').\
        pack(anchor='center')
    
    #Cantidad
    texto_3=Label(create_win,text='Ingresa una cantidad')
    texto_3.pack(anchor='center')

    cantidad = Entry(create_win)
    cantidad.pack(anchor='center')
    #Confirmación
    confirmar = Button(create_win,text='Confirmar',\
        width=8,height=1,command=lambda:[create_piece(var.get(),var_2.get(),cantidad.get()),create_win.destroy()]).pack(side='left')
    cancelar = Button(create_win,text='Cancelar',\
        width=8,height=1,command=lambda:[on_off_main(True),create_win.destroy()]).pack(side='right')
    
    #Función
    def create_piece(nombre,tipo,cantidad):
        if cantidad =='':
            messagebox.showerror(message='Faltan datos')
            return None
        cantidad = int(cantidad)
        if cantidad <= 0:
            messagebox.showerror(message='¡El valor debe ser mayor que 0!')
            return None
        else:
            Maderitas(nombre,tipo,cantidad)
            messagebox.showinfo(message='¡Creado exitosamente!')

    create.main()

####---------------------GUIA2-----------------####
from crud.read import *


ventana.mainloop()
