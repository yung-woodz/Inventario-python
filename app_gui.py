import tkinter as tk
from tkinter import messagebox
from auth import Users
from crud.create import Maderitas as CrearProducto
from crud.update import actualizar_producto
from crud.delete import Maderitas
from crud import read
from produccion import criterio
from produccion.criterio import cargar_y_mostrar_productos

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Inventario")
        self.root.geometry("500x600")
        self.mostrar_login()

    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_login(self):
        self.limpiar_ventana()
        tk.Label(self.root, text="Usuario:").pack()
        self.entry_user = tk.Entry(self.root)
        self.entry_user.pack()

        tk.Label(self.root, text="Contraseña:").pack()
        self.entry_pass = tk.Entry(self.root, show="*")
        self.entry_pass.pack()

        tk.Button(self.root, text="Iniciar sesión", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Registrarse", command=self.registro).pack()

    def login(self):
        usuario = self.entry_user.get()
        contraseña = self.entry_pass.get()
        if Users.verificarLogin(usuario, contraseña):
            messagebox.showinfo("Login", "Inicio de sesión exitoso")
            self.mostrar_menu()
        else:
            messagebox.showerror("Error", "Credenciales inválidas")

    def registro(self):
        self.limpiar_ventana()

        campos = ["Nombre", "Apellidos", "Usuario", "Contraseña"]
        entradas = {}
        for campo in campos:
            tk.Label(self.root, text=campo + ":").pack()
            entradas[campo] = tk.Entry(self.root, show="*" if campo == "Contraseña" else None)
            entradas[campo].pack()

        def realizar_registro():
            Users(
                entradas["Nombre"].get(),
                entradas["Apellidos"].get(),
                entradas["Usuario"].get(),
                entradas["Contraseña"].get()
            )
            messagebox.showinfo("Registro", "Registro exitoso")
            self.mostrar_login()

        tk.Button(self.root, text="Registrarse", command=realizar_registro).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.mostrar_login).pack()

    def mostrar_menu(self):
        self.limpiar_ventana()

        tk.Label(self.root, text="Menú Principal", font=("Helvetica", 14)).pack(pady=10)

        tk.Button(self.root, text="Agregar producto", command=self.agregar_producto_gui).pack(fill='x')
        tk.Button(self.root, text="Leer productos", command=self.leer_productos_gui).pack(fill='x')
        tk.Button(self.root, text="Actualizar producto", command=self.actualizar_producto_gui).pack(fill='x')
        tk.Button(self.root, text="Eliminar producto", command=self.eliminar_producto_gui).pack(fill='x')
        tk.Button(self.root, text="Ver Producción FIFO", command=lambda: self.mostrar_produccion_gui("FIFO")).pack(fill='x')
        tk.Button(self.root, text="Ver Producción LIFO", command=lambda: self.mostrar_produccion_gui("LIFO")).pack(fill='x')
        tk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=10)

    def agregar_producto_gui(self):
        self.limpiar_ventana()

        tk.Label(self.root, text="Agregar nuevo producto", font=("Helvetica", 12)).pack(pady=10)

        tk.Label(self.root, text="Nombre:").pack()
        entry_nombre = tk.Entry(self.root)
        entry_nombre.pack()

        tk.Label(self.root, text="Tipo:").pack()
        tipo_var = tk.StringVar(value="Macho")
        tk.OptionMenu(self.root, tipo_var, "Macho", "Hembra").pack()

        tk.Label(self.root, text="Tiempo (min):").pack()
        entry_tiempo = tk.Entry(self.root)
        entry_tiempo.pack()

        tk.Label(self.root, text="Cantidad:").pack()
        entry_cantidad = tk.Entry(self.root)
        entry_cantidad.pack()

        def guardar_producto():
            try:
                nombre = entry_nombre.get().strip()
                tipo = tipo_var.get()
                tiempo = int(entry_tiempo.get())
                cantidad = int(entry_cantidad.get())

                if not nombre or tiempo <= 0 or cantidad <= 0:
                    raise ValueError

                CrearProducto(nombre, tipo, tiempo, cantidad)
                messagebox.showinfo("Éxito", "Producto agregado correctamente")
                self.mostrar_menu()
            except:
                messagebox.showerror("Error", "Datos inválidos")

        tk.Button(self.root, text="Guardar", command=guardar_producto).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.mostrar_menu).pack()

    def leer_productos_gui(self):
        self.limpiar_ventana()
        productos = read.cargar_productos()

        tk.Label(self.root, text="Listado de Productos", font=("Helvetica", 12)).pack(pady=10)
        text_area = tk.Text(self.root, height=20, width=60)
        text_area.pack()

        for nombre, tipos in productos.items():
            text_area.insert(tk.END, f"{nombre}:\n")
            for tipo, data in tipos.items():
                text_area.insert(tk.END, f"  {tipo}: {data['cantidad']} unidades ({data['tiempo']} min)\n")
            text_area.insert(tk.END, "\n")

        tk.Button(self.root, text="Volver", command=self.mostrar_menu).pack(pady=10)

    def actualizar_producto_gui(self):
        self.limpiar_ventana()

        tk.Label(self.root, text="Actualizar Producto", font=("Helvetica", 12)).pack(pady=10)

        tk.Label(self.root, text="Nombre del producto:").pack()
        entry_nombre = tk.Entry(self.root)
        entry_nombre.pack()

        tk.Label(self.root, text="Tipo:").pack()
        tipo_var = tk.StringVar(value="Macho")
        tk.OptionMenu(self.root, tipo_var, "Macho", "Hembra").pack()

        tk.Label(self.root, text="Cantidad a agregar:").pack()
        entry_cantidad = tk.Entry(self.root)
        entry_cantidad.pack()

        def actualizar():
            nombre = entry_nombre.get().strip()
            tipo = tipo_var.get()
            try:
                cantidad = int(entry_cantidad.get())
                if cantidad <= 0:
                    raise ValueError

                if actualizar_producto(nombre, tipo, cantidad):
                    messagebox.showinfo("Éxito", f"Producto actualizado correctamente")
                else:
                    messagebox.showerror("Error", "Producto no encontrado")
            except:
                messagebox.showerror("Error", "Cantidad inválida")

        tk.Button(self.root, text="Actualizar", command=actualizar).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.mostrar_menu).pack()

    def eliminar_producto_gui(self):
        self.limpiar_ventana()

        tk.Label(self.root, text="Eliminar Producto", font=("Helvetica", 12)).pack(pady=10)

        tk.Label(self.root, text="Nombre del producto:").pack()
        entry_nombre = tk.Entry(self.root)
        entry_nombre.pack()

        tk.Label(self.root, text="Tipo:").pack()
        tipo_var = tk.StringVar(value="Macho")
        tk.OptionMenu(self.root, tipo_var, "Macho", "Hembra").pack()

        tk.Label(self.root, text="Cantidad a eliminar:").pack()
        entry_cantidad = tk.Entry(self.root)
        entry_cantidad.pack()

        def eliminar():
            nombre = entry_nombre.get().strip()
            tipo = tipo_var.get()
            try:
                cantidad = int(entry_cantidad.get())
                if cantidad <= 0:
                    raise ValueError

                m = Maderitas(nombre, tipo, 0, 0)
                if m.eliminar(nombre, tipo, 0, cantidad):
                    messagebox.showinfo("Éxito", "Producto eliminado correctamente")
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el producto")
            except:
                messagebox.showerror("Error", "Cantidad inválida")

        tk.Button(self.root, text="Eliminar", command=eliminar).pack(pady=10)
        tk.Button(self.root, text="Volver", command=self.mostrar_menu).pack()

    def mostrar_produccion_gui(self, orden):
        self.limpiar_ventana()
        productos = {}

        tk.Label(self.root, text=f"Producción ({orden})", font=("Helvetica", 12)).pack(pady=10)
        text_area = tk.Text(self.root, height=25, width=60)
        text_area.pack()

        # Reusamos la lógica de procesamiento
        ruta_archivo = "crud/Maderitas.txt"
        try:
            with open(ruta_archivo, 'r') as f:
                lineas = f.readlines()
                if orden == "LIFO":
                    lineas = reversed(lineas)

                for linea in lineas:
                    partes = linea.strip().split()
                    if len(partes) >= 4:
                        nombre = " ".join(partes[:-3])
                        tipo = partes[-3]
                        tiempo = partes[-2]
                        cantidad = partes[-1]
                        text_area.insert(tk.END, f"{nombre} {tipo}: {cantidad} unidades ({tiempo} min)\n")
        except:
            text_area.insert(tk.END, "Error al leer el archivo")

        tk.Button(self.root, text="Volver", command=self.mostrar_menu).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()
