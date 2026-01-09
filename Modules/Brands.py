# Importa tkinter con el alias tk
import tkinter as tk
# Desde tkinter importa ttk y messagebox
from tkinter import ttk, messagebox
# Desde la carpet Database y el archivo cb_connection importa la funcion conectar
from Database.db_connection import conectar

# Crea la clase MarcasApp


class MarcasApp:
    # Crea la funcion __init__ con los atributos self y frame
    def __init__(self, frame):

        # Labels y Entries

        self.entries = {}  # Crea el diccionario entries

        # Crea un label/etiqueta dentro del frame, con el texto "GESTION DE MARCAS" y utiliza grid/malla para ubicarlo en la fila 0, columna 5
        tk.Label(frame, text="GESTIÓN DE MARCAS").grid(row=0, column=5)

        # Crea un label/etiqueta en el frame, con el texto "Marca:" y utiliza grid para ubicarlo en la fila 1, columna 3
        tk.Label(frame, text="Marca:").grid(row=1, column=3)
        # Crea la llave GesMarca en entries la cual crea un Entry/entrada dentro del frame y con un ancho de 25 pixeles
        self.entries["GesMarca"] = tk.Entry(frame, width=25)
        # La llave GesMarca utiliza grid para ubicarlo en la fila 1, columna 4
        self.entries["GesMarca"].grid(row=1, column=4)

        # Botones de Marcas

        tk.Button(  # Crea un boton
            # Dentro del frame, con el texto "AGREGAR", con el fondo #6CFF22 y con la fuente de color azul
            frame, text="AGREGAR", bg="#6CFF22", fg="blue",
            # La fuente va a ser Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.agregar_marcas  # Llama a la funcion agregar_marcas
            # Utiliza grid/malla para ubicarlo en la fila 2, columna 3, ocupa 2 columnas y deja un espacio de 5 pixeles en el eje X
        ).grid(row=2, column=3, columnspan=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del frame, con el texto "ACTUALIZAR", el fondo de color #2273FF y con la fuente de color naranja
            frame, text="ACTUALIZAR", bg="#227EFF", fg="orange",
            # La fuente va a ser Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.actualizar_marcas  # Llama a la funcion actualizar_marcas
            # Utiliza grid para ubicarlo en la fila 2, columna 3, ocupa 2 columnas y deja un espacio de 5 pixeles en el eje X
        ).grid(row=3, column=3, columnspan=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del frame, con el texto "ELIMINAR", con el fondo de color # F80000 y con la fuente de color negro
            frame, text="ELIMINAR", bg="#F80000", fg="black",
            # La fuente va a ser Arial de tamanio 10 con la propieda bold/negrita
            font=("Arial", 10, "bold"),
            command=self.eliminar_marcas  # Llama a la funcion eliminar_marcas
            # Utiliza grid para ubicarlo en la fila 4, columna 3, ocupa 2 columnas y deja un espacio de 5 pixeles en eje X
        ).grid(row=4, column=3, columnspan=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del frame, con el texto "LIMPIAR", con el fondo de color #00F2F y con el color de la fuente de color verde
            frame, text="LIMPIAR", bg="#00F2FF", fg="green",
            # La fuente va a ser Arial de tamanio 10 con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.limpiar  # Llama a la funcion limpiar
            # Utiliza grid/malla para ubicarlo en la fila 5, columna 3, ocupa 2 columnas y deja un espacio de 4 pixeles en el eje X
        ).grid(row=5, column=3, columnspan=2, padx=5)

        # Tabla de Marcas

        self.tree_gesMar = ttk.Treeview(  # La variable tree_gesMar crea un Treeview (tabla)
            frame,  # Dentro del frame
            columns=("id", "Nombre"),  # Con las columnas id, marca
            show="headings"  # Muestra solo las columnas mencionadas anteriormente
        )
        # Para col que va a recorrer las columnas del tree_gesMar
        for col in self.tree_gesMar["columns"]:
            # En el encabezado del tree_gesMar en la posicion col, se va a poner el texto col
            self.tree_gesMar.heading(col, text=col)
            # Las columnas del tree_gesMar en la posicion col, van a tener un ancho de 150 pixeles y van a estar anclado al centro
            self.tree_gesMar.column(col, width=150, anchor="center")
        self.tree_gesMar.grid(row=1, column=5, rowspan=6,  # Utiliza grid para ubicarlo en la fila 1, columna 5, ocupa 6 filas
                              # Deja un espacio de 10 pixeles en ambos ejes y rellena con 200 pixeles en el eje Y
                              padx=10, pady=10, ipady=200)

        self.cargar_marcas()  # Llama a la funcion cargar_marcas
        # Le bindea al treeviewSelect del tree_gesMar la funcion seleccionar_marcas
        self.tree_gesMar.bind("<<TreeviewSelect>>", self.seleccionar_marcas)

    # Crea la funcion cargar_marcas con el atributo self
    def cargar_marcas(self):

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si no hay conexion
        if not conn:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se pudo conectar"
            messagebox.showerror("Error", "No se pudo conectar")
            return  # No devuelve nada

        cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

        # Para i que recorre los hijos del tree_gesMar
        for i in self.tree_gesMar.get_children():
            # Elimina los hijos que esten en i del tree_gesMar
            self.tree_gesMar.delete(i)

        # Consulta tabla marcas

        cursor.execute("""
            SELECT *
            FROM marcas
            ORDER BY nombre DESC
        """)

        # Para row que recorre todo lo que obtenga cursor
        for row in cursor.fetchall():
            # Inserta desde el inicio hasta el final los valores de row dentro del tree_gesMar
            self.tree_gesMar.insert("", "end", values=row)

        conn.close()  # Cierra la conexion

    # Crea la funcion limpiar con el atributo self
    def limpiar(self):

        # Para entry que va a recorrer los valores de entries
        for entry in self.entries.values():

            # Si hay una insancia dentro del entry que sea de tipo Entry
            if isinstance(entry, tk.Entry):
                # Elimina desde el caracter 0 hasta el final
                entry.delete(0, "end")

    # Crea la funcion seleccionar_marcas con los atributos self y event
    def seleccionar_marcas(self, event):

        # La variable seleccion llama al metodo selection del tree_gesMar
        seleccion = self.tree_gesMar.selection()

        # Si hay seleccion
        if seleccion:
            # La variable valores obtiene el valor de la seleccion en la posicion 0 mediante el metodo item del tree_gesMar
            valores = self.tree_gesMar.item(seleccion[0])["values"]
            self.limpiar()  # Llama a la funcion limpiar

            # En la llave "GesMarca" del entries inserta al inicio los valores en la posicion 1
            self.entries["GesMarca"].insert(0, valores[1])

    # Crea la funcion obtener_datos_marcas con el atributo self
    def obtener_datos_marcas(self):

        # La variable marca obtiene su valor de la llave "GesMarca" del entries
        marca = self.entries["GesMarca"].get().strip()

        return marca  # Devuelve la variable marca

    # Crea la funcion agregar_marcas con el atributo self
    def agregar_marcas(self):

        # Crea la variable datos la cual llama obtener_datos_marcas
        datos = self.obtener_datos_marcas()

        # Si no hay datos
        if not datos:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encontraron datos"
            messagebox.showerror("Error", "No se encontraron datos")
            return  # No devuelve nada

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo conecar de la variable conn

            # Insertar datos en la tabla marcas

            cursor.execute("""
                INSERT INTO marcas (nombre)
                VALUES (%s)
            """, (datos,))  # Obtiene el dato de la variable datos y utiliza coma al final

        conn.commit()  # Termina de ejecutar el insert
        conn.close()  # Cierra la conexion
        self.cargar_marcas()  # Llama a la funcion cargar_marcas
        self.limpiar()  # Llama a la funcion limpiar
        # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Marca agregada"
        messagebox.showinfo("Éxito", "Marca agregada")

    # Crea la funcion actualizar_marcas con el atributo self
    def actualizar_marcas(self):
        # La variable seleccion llama al metodo selection del tree_gesMar
        seleccion = self.tree_gesMar.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona una marca"
            messagebox.showwarning("Selecciona", "Selecciona una marca")
            return  # No devuelve nada

        # La variable item obtiene el item en la posicion 0 de la seleccion del tree_gesMar
        item = self.tree_gesMar.item(seleccion[0])
        # La variable marca_id obtiene el valor en la posicion 0 del item
        marca_id = item["values"][0]
        # La variable datos llama a la funcion obtener_datos_marcas
        datos = self.obtener_datos_marcas()

        # Si no hay datos
        if not datos:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encontraron datos"
            messagebox.showerror("Error", "No se encontraron datos")
            return  # No devuelve nada

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Actualizar datos de la tabla marcas

            cursor.execute("""
                UPDATE marcas
                SET nombre=%s
                WHERE marca_id=%s
            """, (datos, marca_id))  # Utiliza el dato de la variable datos y luego marca_id

        conn.commit()  # Termina de ejecutar la actualizacion de los datos
        conn.close()  # Cierra la conexion
        self.cargar_marcas()  # Llama a la funcion cargar_marcas
        # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Marca actualizada"
        messagebox.showinfo("Éxito", "Marca Actualizada")

    # Crea la funcion eliminar_marcas con el atributo self
    def eliminar_marcas(self):

        # La variable seleccion llama al metodo selection del tree_gesMar
        seleccion = self.tree_gesMar.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona un celular"
            messagebox.showwarning("Selecciona", "Selecciona un celular")
            return  # No devuelve nada

        # Si el usuario responde "Si" en el mensaje de tipo si o no con el titulo "Confirmar" y con el mensaje "¿Eliminar marca?"
        if messagebox.askyesno("Confirmar", "¿Eliminar marca?"):
            # La variable marca_id obtiene el valor en la posicion 0 de la seleccion en la posicion 0 mediante el metodo item del tree_gesMar
            marca_id = self.tree_gesMar.item(seleccion[0])["values"][0]

            conn = conectar()  # La variable conn llama al metodo conectar

            # Si hay conexion
            if conn:
                cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

                # Eliminar datos de la tabla marcas

                cursor.execute("""
                    DELETE FROM marcas
                    WHERE marca_id=%s
                """, (marca_id,))  # Utiliza la variable marca_id con una coma al final

                conn.commit()  # Termina de ejecutar la eliminacion de datos
                conn.close()  # Cierra la conexion
                self.cargar_marcas()  # Llama a la funcion cargar_marcas
