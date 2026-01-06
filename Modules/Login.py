# modules/login.py
# Importa tkinter como tk
import tkinter as tk
# Desde tkinter importa ttk y messagebox
from tkinter import ttk, messagebox
# Desde la carpeta Database y el archivo db_connection importa la funcion conectar
from Database.db_connection import conectar
# Desde la carpeta Modules y el archivo Menu importa la clase MenuApp
from Modules.Menu import MenuApp

# Crea la clase LoginApp


class LoginApp:
    # Crea la funcion __init__ con los atributos self y root
    def __init__(self, root):

        self.root = root  # La variable root es igual al parametro root
        # El titutlo del root va a ser "Servicio Tecnico - Login"
        self.root.title("Servicio Técnico - Login")
        # El tamanio de la ventana del root va a ser de 350 pixeles en el eje X y 250 pixeles en el eje Y
        self.root.geometry("350x250")
        # Establece que no se puede ajustar el tamanio de la ventana en ambos ejes
        self.root.resizable(False, False)

        # Labels y Entries

        tk.Label(root, text="INICIAR SESIÓN", font=(  # Crea un Label/Etiqueta dentro del root, con el texto "INICIAR SESION" y con la fuente Arial, de tamanio 16 y con la propiedad bold/negrita
            # Empaqueta el label dejando un espacio de 15 pixeles en el eje Y
            "Arial", 16, "bold")).pack(pady=15)

        # Crea un Label/Etiqueta dentro del root, con el texto "Email:" y luego lo empaqueta dejando un espacio de 5 pixeles en el eje Y
        tk.Label(root, text="Email:").pack(pady=5)
        # La variable email_entry crea un Entry/entrada dentro del root con un ancho de 30 pixeles
        self.email_entry = tk.Entry(root, width=30)
        # Empaqueta el email_entry dejando un espacio de 5 pixeles en el eje Y
        self.email_entry.pack(pady=5)
        # Inserta al inicio del email_entry el valor "Fabricio@servicio.com"
        self.email_entry.insert(0, "Fabricio@servicio.com")

        # Crea un Label/Etiqueta dentro del root con el texto "Rol:" y luego lo empaqueta dejando un espacio de 5 pixeles en el eje Y
        tk.Label(root, text="Rol:").pack(pady=5)
        # La variable rol_var crea un StringVar con el valor "super_usuario"
        self.rol_var = tk.StringVar(value="super_usuario")
        ttk.Combobox(root, textvariable=self.rol_var, values=[  # Crea un Combobox (caja de opciones) dentro del root, con la variable de texto rol_var, con las opciones "admin", "empleado", "super_usuario"
                     # Con el estado en readonly (solo lectura), con un ancho de 27 pixeles y luego lo empaqueta dejando un espacio de 5 pixeles en el eje Y
                     "admin", "empleado", "super_usuario"], state="readonly", width=27).pack(pady=5)

        # Botones

        tk.Button(root, text="INGRESAR", bg="#B1451C", fg="black", font=(  # Crea un Boton dentro del root con el texto "INGRESAR", el fondo de color #B1451C, la fuente de color negro
            # La fuente va a ser Arial, de tamanio 10 y con la propiedad bold/negrita, ejecuta la funcion login y luego lo empaqueta dejando un espacio de 15 pixeles en el eje Y
            "Arial", 10, "bold"), command=self.login).pack(pady=15)

    # Crea la funcion login con el atributo self
    def login(self):

        # La variable email obtiene su valor de la variable email_entry
        email = self.email_entry.get().strip()
        rol = self.rol_var.get()  # La variable rol obtiene su valor de la variable rol_var

        # Si no hay email o no hay rol
        if not email or not rol:
            # Muestra un mensaje de advertencia con el titulo "Datos incompletos" y con el mensaje "Completa todos los campos"
            messagebox.showwarning("Datos incompletos",
                                   "Completa todos los campos")
            return  # No devuelve nada

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si no hay conexion
        if not conn:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se establecio conexion"
            messagebox.showerror("Error", "No se establecio conexion")
            return  # No devuelve nada

        # Intenta
        try:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Consulta tabla usuarios

            cursor.execute(
                # Utiliza las variables email y rol como los datos para la consulta
                "SELECT * FROM usuarios WHERE email = %s AND rol = %s", (email, rol))

            # La variable usuario obtiene todos los datos de obtenga cursor
            usuario = cursor.fetchone()
            conn.close()  # Cierra la conexion

            # Si hay usuario
            if usuario:
                # Muestra un mensaje de informacion con el titulo "Exito" y el mensaje "Bienvenido {Lo que este en la posicion 1 de usuario} {Lo que este en la posicion 2 de usuario}"
                messagebox.showinfo(
                    "Exito", f"Bienvenido {usuario[1]} {usuario[2]}")
                self.root.destroy()  # Destruye la ventana
                root_menu = tk.Tk()  # La variable rot_menu cre un Tk
                # Le pasa los parametros root_menu y usuario a la clase MenuApp
                MenuApp(root_menu, usuario)
                root_menu.mainloop()  # Hace que root_menu se ejecute indefinidamente
            # En otro caso
            else:
                # Muestra un mensaje de error con el titulo "Error" y con el mensaje "Email o rol incorrectos"
                messagebox.showerror("Error", "Email o rol incorrectos")
        # Si no puede hace una excepcion con el alias e
        except Exception as e:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "Error en login: {muestra la excepcion o error}"
            messagebox.showerror("Error", f"Error en login: {e}")
