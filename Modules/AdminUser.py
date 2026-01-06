# Importa tkinter como tk
import tkinter as tk
# Desde tkinter se importa ttk y messagebox
from tkinter import ttk, messagebox
# Desde la carpeta Database y el archivo db_connection se importa la clase conectar
from Database.db_connection import conectar

# Crea la clase AdminUserApp


class AdminUserApp:
    # Crea la funcion __init__ con los atributos self, root y es_super_user (con valor inicial en False)
    def __init__(self, root, es_super_user=False):

        self.root = root  # se crea la variable root a la cual se le asigna el parametro root
        # se crea la variable es_super_user y se le asigna el valor del parametro es_super_user
        self.es_super_user = es_super_user
        # la propiedad title del root va a ser "Administrar Usuarios"
        self.root.title("Administrar Usuarios")

        # Frame superior: formulario

        # La variable frame_form va a crear un frame/marco en el root
        frame_form = tk.Frame(root)
        # se utiliza pack para empaquetar y ponerlo 10 pixeles separado del borde en el eje Y, que llene todo el eje X y que este separado 20 pixeles del borde en el eje X
        frame_form.pack(pady=10, fill="x", padx=20)

        # Campos

        # El arreglo campos va a tener los valores "Nombre", "Apellido", "Email" y "Rol"
        campos = ["Nombre", "Apellido", "Email", "Rol"]
        self.entries = {}  # la variable entries va a ser un diccionario

        # Labels y Entries

        # Recorre el arreglo campos con enumerate el cual enumera los datos que esten dentro del arreglo obteniendo así el indice y el dato dentro, por lo tanto se va a asignar el indice a i y los datos en campo
        for i, campo in enumerate(campos):
            # Labels
            tk.Label(frame_form, text=campo + ":").grid(  # Crea un Label/Etiqueta que se va a ubicar en el frame_form, con el texto que este en la cariable campo y luego ":"
                # va a utilizar grid/malla por lo tanto lo va a ubicar en la fila i, columna 0, se va a enganchar en west/oeste (osea lo mas a la izquierda posible) y con una separacion de 2 pixeles en el eje Y
                row=i, column=0, sticky="w", pady=2
            )

            # Entries
            # si campo tiene un dato igual a "Rol"
            if campo in ["Rol"]:
                # En la llave campo del diccionario entries
                self.entries[campo] = ttk.Combobox(frame_form, width=30,  # Se crea un combobox (una caja desplegable con opciones) en el frame_form, de 30 pixeles de ancho
                                                   # los valores/opciones que va a tener son "admin", "empleado" y "super_usuario" y su estado va a ser de solo lectura (osea que no se puede escribir en el)
                                                   values=["admin", "empleado", "super_usuario"], state="readonly")
            # para los demas valores en campo
            else:
                # En la llave campo del diccionario entries
                # Se crea un Entry (campo donde se puede escribir) que se va a ubicar dentro del frame_form y de 33 pixeles de ancho
                self.entries[campo] = tk.Entry(frame_form, width=33)
            # En la lave campo del diccionario entries
            # Se uitiliza grid/malla para ubicarlo en la fila i, columna 1, con una separacion en el eje Y de 2 pixeles y de 5 pixeles en el eje X
            self.entries[campo].grid(row=i, column=1, pady=2, padx=5)

        # Botones
        # Si no es_super_user (osea falso)
        if not self.es_super_user:
            # Crea un boton en el btn_frame con el texto "Agregar", en estado deshabilitado con fondo negro y utiliza pack para posicionarlo al lado izquierdo y con 5 pixeles de separacion en el eje X
            tk.Button(btn_frame, text="Agregar", state="disabled",
                      bg="gray").pack(side="left", padx=5)
            # Crea un boton en el btn_frame con el texto "Actualizar", en estado deshabilitado con fondo negro y utiliza pack para posicionarlo al lado izquierdo y con 5 pixeles de separacion en el eje X
            tk.Button(btn_frame, text="Actualizar", state="disabled",
                      bg="gray").pack(side="left", padx=5)
            # Crea un boton en el btn_frame con el texto "eliminar", en estado deshabilitado con fondo negro y utiliza pack para posicionarlo al lado izquierdo y con 5 pixeles de separacion en el eje X
            tk.Button(btn_frame, text="Eliminar", state="disabled",
                      bg="gray").pack(side="left", padx=5)
        # Si No
        else:
            # La variable btn_frame que va a ser un frame/marco en el frame_form
            btn_frame = tk.Frame(frame_form)
            # Utiliza grid para posicionarse en la fila 5, columna 0, ocupa 2 columnas y con una separación de 10 pixeles en el eje Y
            btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

            tk.Button(btn_frame, text="Agregar", bg="#4CAF50", fg="green",  # Crea un boton en el btn_frame con el texto "Agregar", con fondo de color #4CAF50, con el color de la letra en verde y ejecuta la funcion agregar
                      # utiliza pack para posicionarlo al lado izquierdo y con 5 pixeles de separacion en el eje X
                      command=self.agregar).pack(side="left", padx=5)
            tk.Button(btn_frame, text="Actualizar", bg="#2196F3", fg="blue",  # Crea un boton en el btn_frame con el texto "Actualizar", con fondo de color #2196F3, con el color de la letra en azul y ejecuta la funcion actualizar
                      # utiliza pack para posicionarlo al lado izquierdo y con 5 pixeles de separacion en el eje X
                      command=self.actualizar).pack(side="left", padx=5)
            tk.Button(btn_frame, text="Eliminar", bg="#F44336", fg="red",  # Crea un boton en el btn_frame con el texto "Eliminar", con fondo de color #F44336, con el color de la letra en rojo y ejecuta la funcion eliminar
                      # utiliza pack para posicionarlo al lado izquierdo y con 5 pixeles de separacion en el eje X
                      command=self.eliminar).pack(side="left", padx=5)
            tk.Button(btn_frame, text="Limpiar",  # Crea un boton en el btn_frame con el texto "Limpiar" y ejecuta la funcion limpiar
                      # utiliza pack para posicionarlo al lado izquierdo y con 5 pixeles de separacion en el eje X
                      command=self.limpiar).pack(side="left", padx=5)

        # Tabla

        self.tree = ttk.Treeview(  # La variable tree va a ser un ttk Treeview (osea una talba)
            root,  # Que se va a ubicar en el root
            # Va a tener las columnas "ID", "Nombre", "Apellido", "Email" y "Rol"
            columns=("ID", "Nombre", "Apellido", "Email", "Rol"),
            show="headings",  # Hace que se muestren solo las columnas necesarias
            height=15  # y va a mostrar 15 filas
        )
        # Para col que va a recorrer las columnas del tree
        for col in self.tree["columns"]:
            # el heading/encabezado del tree va a tener la posicion de col y el texto va a ser el valor de col
            self.tree.heading(col, text=col)
            # la columna del tree en la posicion col va a tener un ancho de 120 pixeles y anclado en el centro
            self.tree.column(col, width=120, anchor="center")
        # empaqueta el tree con una separacion de 10 pixeles en el eje Y, 20 pixeles en el eje X, rellena en el eje X e Y y se puede expander
        self.tree.pack(pady=10, padx=20, fill="both", expand=True)

        # Cargar datos
        self.cargar_usuarios()  # Llama a la funcion cargar_usuarios
        # Le bindea al tree el TreeviewSelect y ejecuta la funcion seleccionar
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar)

    # Crea la funcion cargar_usuarios con el atributo self
    def cargar_usuarios(self):

        # Para item que va a utilizar la funcion get_children del tree para recorrer el tree
        for item in self.tree.get_children():
            # Elimina el item del tree
            self.tree.delete(item)

        # Consulta Tabla Usuarios

        conn = conectar()  # la variable conn va a obtener el metodo conectar

        # si hay conexion
        if conn:
            # la variable cursos va a obtener la propiedad cursor de la variable conn
            cursor = conn.cursor()

            # Ejecuta la consulta de toda la tabla usuarios

            cursor.execute("""
                SELECT * FROM usuarios
            """)

            # row/fila va a recorrer la consulta utilizando fetchall de cursor
            for row in cursor.fetchall():
                # Inserta los valores en el tree
                # inserta desde el inicio hasta el final los valores en row/fila
                self.tree.insert("", "end", values=row)
            # Cierra la conexion
            conn.close()

    # Crea la funcion seleccionar con los atributos self y event
    def seleccionar(self, event):

        # La variable seleccion hace referencia al metodo selection del tree
        seleccion = self.tree.selection()

        # Si hay seleccion
        if seleccion:
            # La variable valores va a ser igual a los valores en la selección de la posicion 0 del item del tree
            valores = self.tree.item(seleccion[0])["values"]
            self.limpiar()  # Llama a la funcion limpiar

            # Inserta al incio el dato en la posicion 1 del arreglo valores en la llave del entries "Nombre"
            self.entries["Nombre"].insert(0, valores[1])
            # Inserta al incio el dato en la posicion 2 del arreglo valores en la llave del entries "Apellido"
            self.entries["Apellido"].insert(0, valores[2])
            # Inserta al incio el dato en la posicion 3 del arreglo valores en la llave del entries "Apellido"
            self.entries["Email"].insert(0, valores[3])
            # Inserta al incio el dato en la posicion 4 del arreglo valores en la llave del entries "Apellido"
            self.entries["Rol"].insert(0, valores[4])

    # Crea la funcion obtener_datos con el atributo self
    def obtener_datos(self):

        # La variable nombre va obtener el valor que este en el entries "Nombre"
        nombre = self.entries["Nombre"].get().strip()
        # La variable apellido va obtener el valor que este en el entries "Apellido"
        apellido = self.entries["Apellido"].get().strip()
        # La variable email va obtener el valor que este en el entries "Email"
        email = self.entries["Email"].get().strip()
        # La variable rol va obtener el valor que este en el entries "Rol"
        rol = self.entries["Rol"].get().strip()

        # Si no estan todos nombre, apellido, email y rol
        if not all([nombre, apellido, email, rol]):
            # Muestra un mensaje de advertencia con el titulo "Faltan datos" y el mensaje "Completa todos los campos"
            messagebox.showwarning("Faltan datos", "Completa todos los campos")
            return None  # Devuelve None
        # Devuelve las variables nombre, apellido, email y rol
        return (nombre, apellido, email, rol)

    # Crea la funcion limpiar con el atributo self
    def limpiar(self):

        # Entry va a recorrer los valores del dicionario entries
        for entry in self.entries.values():

            # Si hay una instancia en entry que sea de tipo tk Entry
            if isinstance(entry, tk.Entry):
                # llama a la funcion delete/eliminar para eliminar los datos desde el inicio hasta el final/end
                entry.delete(0, "end")

            # Si No pasa eso pero hay una instancia en el entry de tipo ttk Combobox
            elif isinstance(entry, ttk.Combobox):
                # Llama a la funcion set/establecer que establece el dato como "" (osea vacio)
                entry.set("")

    # Crea la funcion agregar con el atributo self
    def agregar(self):

        # Obtencion de datos

        # La variable datos va llamar los datos de la funcion obtener_datos
        datos = self.obtener_datos()

        # Si no hay datos
        if not datos:
            # Muestra una caja de texto con el titulo "Error" y con el mensaje "No se encuentran datos"
            messagebox.showerror("Error", "No se encuentran datos")
            return  # no devuelve nada

        # Insert Tabla Usuarios

        conn = conectar()  # La variable conn va a obtener el metodo conectar

        # Si hay conexion
        if conn:
            # la variable cursor va a obtener la propiedad cursor de la variable conn
            cursor = conn.cursor()

            # Insertar los datos en la tabla Usuarios

            cursor.execute("""
                INSERT INTO usuarios (nombre, apellido, email, rol)
                VALUES (%s, %s, %s, %s)
            """, (*datos,))  # Separa los datos de la variable datos y utiliza una coma al final quedando algo como (Fabricio, Romero, Fabricio@servicio.com, Super_usuario)

            conn.commit()  # Ejecuta el metodo commit para terminar de ejecutar el insert
            conn.close()  # Cierra la conexion
            self.cargar_usuarios()  # Llama a la funcion cargar_usuarios
            self.limpiar()  # Llama a la funcion limpiar
            # Muestra un mensaje de informacion con el titulo "Exito" y el mensaje "Usuario agregado"
            messagebox.showinfo("Éxito", "Usuario agregado")

    # Crea la funcion actualizar con el atributo self
    def actualizar(self):

        # La variable seleccion va a obtener el metodo selection del tree
        seleccion = self.tree.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y el mensaje "Selecciona un usuario"
            messagebox.showwarning("Selecciona", "Selecciona un usuario")
            return  # No devuelve nada

        # La variable item va a obtener el item en la posicion 0 de la seleccion del tree
        item = self.tree.item(seleccion[0])
        # La variable usuario_id va a ser igual al item en la llave "Values" y el item en la posicion 0 (que seria la columna ID)
        usuario_id = item["values"][0]
        # La variable datos va a obtener datos de la funcion obtener_datos
        datos = self.obtener_datos()

        # Si no hay datos
        if not datos:
            # Muestra un mensaje de errorcon el titulo "Error" y el mensaje "No se encuentran datos"
            messagebox.showerror("Error", "No se encontraron datos")
            return  # No devuelve nada

        # Actualizar datos en la tabla Usuarios

        conn = conectar()  # La variable conn va a llamar el metodo conectar

        # Si hay conexion
        if conn:
            # La variable cursor va a obtener el metodo cursor de la variable conn
            cursor = conn.cursor()

            # Actualizar datos de la tabla Usuarios

            cursor.execute("""
                UPDATE usuarios SET nombre=%s, apellido=%s, email=%s, rol=%s
                WHERE usuario_id=%s
            """, (*datos, usuario_id))  # Separa los datos de la variable datos utilizando coma al final y caundo no haya mas datos utiliza el usuario_id

            conn.commit()  # Ejecuta el metodo commit de conn para terminar de ejecutar la actualizacion
            conn.close()  # Cierra la conexion
            self.cargar_usuarios()  # Llama a la funcion cargar_usuarios
            # Muestra un mensaje de informacion con el titulo "Exito" y el mensaje "Usuario actualizado"
            messagebox.showinfo("Éxito", "Usuario actualizado")

    # Crea la funcion eliminar con el atributo self
    def eliminar(self):

        # La variable seleccion llama a la funcion selection del tree
        seleccion = self.tree.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y el mensaje "Selecciona un usuario"
            messagebox.showwarning("Selecciona", "Selecciona un usuario")
            return  # No devuelve nada

        # Muestra un mensaje de si o no con el titulo "Confirmar" y el mensaje "¿Eliminar usuario?", si el usuario selecciona yes
        if messagebox.askyesno("Confirmar", "¿Eliminar usuario?"):
            # La variable usuario id va a ser igual al valor en la posicion 0 de la seleccion en la posicion 0 del item del tree
            usuario_id = self.tree.item(seleccion[0])["values"][0]

            # Eliminar datos de usuarios

            conn = conectar()  # La variable conn llama al metodo conectar

            # Si hay conexion
            if conn:
                # La variable cursor va a llamar al metodo cursor de la variable conn
                cursor = conn.cursor()

                # Eliminar datos de la tabla Usuarios

                cursor.execute(
                    "DELETE FROM usuarios WHERE usuario_id=%s",
                    (usuario_id,))  # Pasa el dato de la variable usuario_id

                conn.commit()  # La variable conn ejecuta la funcion commit para terminar de ejcutar la eliminacion del dato
                conn.close()  # Se cierra la conexion
                self.cargar_usuarios()  # Llama a la funcion cargar_usuarios
