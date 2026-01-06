# Importa tikinter con el apodo de tk
import tkinter as tk
# Desde tkinter importa ttk y messagebox
from tkinter import ttk, messagebox
# Desde la carpeta Modules y el archivo AdminUser importa la clase AdminUserApp
from Modules.AdminUser import AdminUserApp
# Desde la carpeta Modules y el archivo Customers importa la clase ClientesApp
from Modules.Customers import ClientesApp
# Desde la carpeta Modules y el archivo Jobs importa la clase TrabajosApp
from Modules.Jobs import TrabajosApp
# Desde la carpeta Modules y el archivo Movements importa la clase MovimientosApp
from Modules.Movements import MovimientosApp
# Desde la carpeta Modules y el archivo Sales importa la clase VentasApp
from Modules.Sales import VentasApp
# Desde la carpeta Modules y el archivo Suppliers importa la clase ProveedoresApp
from Modules.Suppliers import ProveedoresApp

# Crea la clase MenuApp


class MenuApp:
    # Crea la funcion __init__ con los atributos self, root y usuario
    def __init__(self, root, usuario):

        self.root = root  # La variable root hace referencia al parametro root
        self.usuario = usuario  # La variable usuario hace referencia al parametro usuario
        # El titulo del root es "Servicio Técnico - {La posicion 3 del arreglo usuario con la propiedad title}"
        self.root.title(f"Servicio Técnico - {usuario[3].title()}")
        # El tamanio de la ventana es de 800 pixeles en el eje X y 600 pixeles en el eje Y
        self.root.geometry("800x600")
        tk.Label(root, text=f"Usuario: {usuario[1]} {usuario[2]} ({usuario[3]})", font=(  # Crea un Label/Etiqueta dentro del root con el texto "Usuario {La posicion 1 del arreglo usuario} {La posicion 2 del arreglo usuario} ({La posicion 3 del arreglo usuario})"
            # La fuente es Arial, de tamanio 10 y luego lo empaqueta posicionandolo lo mas al ne/north-east/noreste (Arriba a la derecha) posible, deja un espacio de 20 pixeles en el eje X y 10 pixeles en el eje Y
            "Arial", 10)).pack(anchor="ne", padx=20, pady=10)
        tk.Label(root, text=f"SERVICIO TÉCNICO {usuario[1]} {usuario[2]}".upper(),  # Crea un Label/Etiqueta dentro del root con el texto "SERVICIO TÉCNICO {Lo que este en la posicion 1 del arreglo usuario} {Lo que este en la posicion 2 del arreglo usuario}" y todo eso en mayusculas
                 # Con la fuente en Arial, de tamanio 10 y con la propiedad bold/negrita
                 font=("Arial", 18, "bold")).pack(pady=20)

        # Definir estilo de botones grandes

        # Crea un diccionario con las llaves "width" y el valor 30 (ancho de 30 pixeles), "height" y el valor 2 (altura de 2 pixeles) "font" y con los valores (Arial, 10, bold) (fuente en Arial, tamanio 10 y la propiedad bold)
        btn_style = {"width": 30, "height": 2, "font": ("Arial", 11, "bold")}

        # La variable frame crea un Frame/marco dentro del root
        frame = tk.Frame(root)
        # Empaqueta frame dejando un espacio de 20 pixeles en ambos ejex
        frame.pack(pady=20, padx=20)

        # Botones

        # Columna Izquierda

        tk.Button(frame, text="CONTROL DE TRABAJOS", bg="#2196F3", fg="white",  # Crea un boton dentro del frame con el texto "CONTROL DE TRABAJOS", el color del fondo en #2196F3 y el color de la fuente en blanco
                  # Separa la llave del valor del btn_style, ejecuta la funcion abrir_trabajos y utiliza grid/malla para ubicarlo en la fila 1, columna 0 dejando un espacio de 15 pixeles en el eje Y
                  **btn_style, command=self.abrir_trabajos).grid(row=1, column=0, pady=15)
        tk.Button(frame, text="REGISTRAR MOVIMIENTOS", bg="#FF9800", fg="white",  # Crea un boton dentro del frame con el texto "REGISTRAR MOVIMIENTOS", el color del fondo es #FF9800, el color de la fuente en blanco
                  # Separa la llave del valor del btn_style, ejecuta la funcion abrir_movimientos y utiliza grid para ubicarlo en la fila 2, columna 0 dejando un espacio de 15 pixeles en el eje Y
                  **btn_style, command=self.abrir_movimientos).grid(row=2, column=0, pady=15)
        tk.Button(frame, text="VER CLIENTES", bg="#9C27B0", fg="white",  # Crea un boton dentro del frame con el texto "VER CLIENTES", el fondo de color #9C27B0, el color de la fuente en blanco
                  # Separa la llave del valor del btn_style, ejecuta la funcion abrir_clientes y utiliza grid para ubicarlo en la fila 3, columna 0 dejando un espacio de 15 pixeles en el eje Y
                  **btn_style, command=self.abrir_clientes).grid(row=3, column=0, pady=15)

        # Columna Derecha

        tk.Button(frame, text="VENTAS DE TRABAJOS", bg="#216EF3", fg="white",  # Crea un boton dentro del frame con el texto "VENTAS DE TRABAJOS", con el fondo de color # 216EF3 y con la fuente de color blanco
                  # Separa la llave del valor del btn_style, ejecuta la funcion abrir_ventas y utiliza grid para ubicarlo en la fila 1, columna 1 dejando un espacio de 15 pixeles en el eje Y
                  **btn_style, command=self.abrir_ventas).grid(row=1, column=1, padx=15)
        tk.Button(frame, text="ADMINISTRAR PROVEEDORES", bg="#F32159", fg="white",  # Crea un boton dentro del frame con el texto "ADMINISTRAR PROVEEDORES", con el fondo de color #F32159 y con la fuente de color blanco
                  # Separa la llave del valor del btn_style, ejecuta la funcion abrir_proveedores, utiliza grid/malla para ubicarlo en la fila 2, columna 1 dejando un espacio de 15 pixeles en el eje Y
                  **btn_style, command=self.abrir_proveedores).grid(row=2, column=1, padx=15)
        tk.Button(frame, text="ADMINISTRAR USUARIOS", bg="#40B027", fg="white",  # Crea un boton dentro del frame con el texto "ADMINISTRAR USUARIOS", con el fondo de color #40B027 y con la fuente de color blanco
                  # Separa la llave del valor del btn_style, ejecuta la funcion abrir_admin_usuarios y utiliza grid/malla para ubicarlo en la fila 3, columna 1 dejando un espacio de 15 pixeles en el eje Y
                  **btn_style, command=self.abrir_admin_usuarios).grid(row=3, column=1, pady=15)

        # Centro

        tk.Button(root, text="CERRAR SESIÓN", bg="#F44336", fg="white",  # Crea un boton dentro del root con el texto "CERRAR SESIÓN", con el fondo de color #F44336 y la fuente de color blanco
                  # Separa la llave del valor del btn_style ejecuta la funcion destroy del root, lo empaqueta dejando un espacio de 15 pixeles en el eje Y
                  **btn_style, command=root.destroy).pack(pady=15)

    # Crea la funcion nueva_ventana con los parametros self, titulo, clase y size
    def nueva_ventana(self, titulo, clase, size):

        # La variable ventana crea un Toplevel en el root (crea una nueva ventana hija del root)
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)  # El titulo de la ventana es el parametro titulo
        ventana.geometry(size)  # El tamanio de la ventana es el parametro size
        clase(ventana)  # Al paramerto clase le pasa la variable ventana

    # Crea la funcion abrir_trabajos con el atributo self
    def abrir_trabajos(self):
        # Llama a la funcion nueva_ventana pasando los parametros "Trabajos", la clase TrabajosApp, "1366x720"
        self.nueva_ventana("Trabajos", TrabajosApp, "1366x720")

    # Lo dejo para ver como es para los usuarios admin y super_usuario
    # def abrir_categorias(self):
    #     if self.usuario[4] == "admin" or self.usuario[4] == "super_usuario":  # usuario[4] = rol
    #         self.nueva_ventana(
    #             "Categorias", lambda root: CategoriasApp(root, es_admin=True))
    #     else:
    #         messagebox.showwarning(
    #             "Acceso denegado", "Solo el admin puede gestionar productos")

    # Crea la funcion abrir_movimientos con el atributo self
    def abrir_movimientos(self):
        # Llama a la funcion nueva_ventana pasando los parametros "Movimientos", la clase MovimientosApp, "800x500"
        self.nueva_ventana("Movimientos", MovimientosApp, "800x500")

    # Crea la funcion abrir_clientes con el atributo self
    def abrir_clientes(self):
        # Llama a la funcion nueva_ventana pasando los parametros "Clientes", la clase ClientesApp, "800x500"
        self.nueva_ventana("Clientes", ClientesApp, "800x500")

    # Crea la funcion abrir_ventas con el atributo self
    def abrir_ventas(self):
        # Llama a la funcion nueva_ventana pasando los parametros "Ventas", la clase VentasApp, "1024x500"
        self.nueva_ventana("Ventas", VentasApp, "1024x500")

    # Crea la funcion abrir_proveedores con el atributo self
    def abrir_proveedores(self):

        # Comprobar rol

        # Si la posicion 4 del arreglo usuario es igual a "admin" o a "super_usuario"
        if self.usuario[4] == "admin" or self.usuario[4] == "super_usuario":
            # Llama a la funcion nueva_ventana pasando los parametros "Proveedores", utiliza lambda para crear una funcion temporal que recibe root y dentro llama a la calse ProveedoresApp para pasarle los parametros root y es_admin como true, luego pasa el parametro "1024x500"
            self.nueva_ventana("Proveedores", lambda root: ProveedoresApp(
                root, es_admin=True), "1024x500")
        # Si no pasa eso
        else:
            # Muestra un mensaje de advertencia con el titulo "Acceso denegado" y con el mensaje "Solo el admin puede gestionar productos"
            messagebox.showwarning(
                "Acceso denegado", "Solo el admin puede gestionar proveedores")

    # Crea la funcion abrir_admin_usuarios con el atributo self
    def abrir_admin_usuarios(self):

        # Comprobar rol

        # Si la posicion 4 del arreglo usuario es igual a "super_usuario"
        if self.usuario[4] == "super_usuario":
            # Llama a la funcion nueva_ventana pasando los parametros "Administrar Usuarios", utiliza lambda para crear una funcion temporal que recibe root y dentro llama a la clase AdminUserApp pasando los parametros root y es_admin en true, luego pasa el parametro "800x500"
            self.nueva_ventana("Administrar Usuarios", lambda root: AdminUserApp(
                root, es_super_user=True), "800x500")
        # Si no pasa eso
        else:
            # Muestra un mensaje de advertencia con el titulo"Acceso denegado" y con el mensaje "Solo el super usuario puede administrar los usuarios"
            messagebox.showwarning(
                "Acceso denegado", "Solo el super usuario puede administrar los usuarios")
