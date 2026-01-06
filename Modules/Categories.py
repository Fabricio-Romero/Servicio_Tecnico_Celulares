# Importa tkinter como tk
import tkinter as tk
# Desde tkinter importa ttk y messagebox
from tkinter import ttk, messagebox
# Desde la carpeta Database y el archivo db_connection importa el metodo conectar
from Database.db_connection import conectar

# Crea la clase CategoriasApp


class CategoriasApp:
    # Se define la funcion __init__ con los atributos self, root y es_admin como falso
    def __init__(self, root, es_admin=False):
        self.root = root  # Se define la Variable root como el root
        # La variable es_admin se asigna el valor del parametro es_admin
        self.es_admin = es_admin
        self.root.title("Categorias")  # El titulo del root es "Categorias"

        # La variable frame crea un frame/marco en el root
        frame = tk.Frame(root)
        # Empaqueta ese frame separado del borde 20 pixeles en el eje X e Y
        frame.pack(padx=20, pady=20)

        self.entries = {}  # Se crea el diccionario entries

        # Tabla de categorias
        self.tree = ttk.Treeview(  # La variable tree hace referencia a un Treeview
            frame,  # Que se ubica en la variable frame
            columns=("ID", "Nombre"),  # Con las columnas "ID" y "Nombre"
            show="headings",  # Muestra solo la cantidad de columnas dentro de columns
            height=15  # Va a mostrar solo 15 filas
        )

        # col va a recorrer las columns en tree
        for col in self.tree["columns"]:
            # El encabezado del tree se va a ubicar en la posicion de col y con el texto segun lo que contenga col
            self.tree.heading(col, text=col)
            # Las columnas del tree se van a ubicar en la posicion de col, con un ancho de 100 pixeles y se van a centrar en el centro
            self.tree.column(col, width=100, anchor="center")

        self.tree.grid(row=0, column=1, rowspan=10,  # El tree utiliza grid/malla para ubicarse en la fila 0, columna 1, va a ocupar 10 filas
                       # y 2 columnas, se va a posicionar lo mas al este posible (osea a la derecha), va a tener una separacion de 15 pixeles en el eje X, va a rellenar 150 pixeles en el eje X y 55 en el eje Y
                       columnspan=2, sticky="e", padx=15, ipadx=150, ipady=55)

        # Labels

        tk.Label(frame, text="Nombre:").grid(  # Crea un label/etiqueta que se ubica dentro del frame, con el texto "Nombre"
            # Utiliza grid para ubicarse en la fila 0 y la columna 0 y se va a posicionar lo mas al north/norte posible (osea arriba)
            row=0, column=0, sticky="n")
        self.entries["Nombre"] = tk.Entry(  # Crea un entries con la llave "Nombre" y va a contener un Entry
            frame, width=33)  # Que se va a ubicar en el frame y con un ancho de 33 pixeles
        # El entries con la llave "Nombre" utiliza el grid/malla para ubicarse en la fila 1, columna 0 y posicionarse en lo mas al west/oeste posible (mas a la izquierda)
        self.entries["Nombre"].grid(row=1, column=0, sticky="w")

        # Botones

        tk.Button(  # Se crea un boton
            # Dentro del frame, con el texto "AGREGAR", con el fondo de color #6CFF22 y la fuente en azul
            frame, text="AGREGAR", bg="#6CFF22", fg="blue",
            # La fuente va a ser arial, de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.agregar  # Va a ejecutar el metodo agregar
            # Utiliza el grid para ubicarse en la fila 3, columna 0 y lo mas al north/norte posible (mas arriba)
        ).grid(row=3, column=0, sticky="n")
        tk.Button(  # Se crea un botom
            # Dentro del frame, con el texto "ACTUALIZAR", con el fondo de color #227EFF, la fuente de color naranja
            frame, text="ACTUALIZAR", bg="#227EFF", fg="orange",
            # La fuente va a ser arial, de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.actualizar  # Va a ejecutar el metodo actualizar
            # Utiliza el grid/malla para ubicarse en la fila 4, columna 0 y posicionarse lo mas al north/norte posible (mas arriba)
        ).grid(row=4, column=0, sticky="n")
        tk.Button(  # Se crea un boton
            # Dentro del frame, con el texto "ELIMINAR", con el fondo de color #F80000 y la fuente de color negro
            frame, text="ELIMINAR", bg="#F80000", fg="black",
            # La fuente va a ser arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.eliminar  # Va a ejecutar el metodo eliminar
            # Utiliza grid para ubicarse en la fila 5, columna 0 y posicionarse lo mas al north/norte posible (mas arriba)
        ).grid(row=5, column=0, sticky="n")
        tk.Button(  # Se crea un boton
            # Dentro del frame, con el texto "LIMPIAR", con el fondo de color #00F2FF, con la fuente de color verde
            frame, text="LIMPIAR", bg="#00F2FF", fg="green",
            # La fuente en arial de tamanio 10 con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.limpiar  # Ejecuta el metodo limpiar
            # Utiliza grid para ubicarse en la fila 6, columna 0 y posicionarlo lo mas al north/norte posible (mas arriba)
        ).grid(row=6, column=0, sticky="n")

        # Carga de datos

        self.cargar_categorias()  # Llama a la funcion cargar_categorias
        # Le bindea al tree el TreeviewSelect y llama a la funcion seleccionar
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar)

    # Crea la funcion cargar_categorias con al atributo self
    def cargar_categorias(self):

        # item va a recorrer los hijos del tree mediante la funcion get_children
        for item in self.tree.get_children():
            self.tree.delete(item)  # Elimina el item del tree

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor desde la variable conn

            # Consulta de toda la tabla categorias

            cursor.execute("""
                SELECT *
                FROM categorias
            """)

            # row recorre los datos que recoga fetchall de la variable cursor
            for row in cursor.fetchall():
                # Inserta en el tree los valores de row desde el principio hasta el final
                self.tree.insert("", "end", values=row)

            conn.close()  # Cierra la conexion

    # Crea la funcion seleccionar con los atributos self y event
    def seleccionar(self, event):

        # La variable seleccion llama al metodo selection del tree
        seleccion = self.tree.selection()

        # Si hay seleccion
        if seleccion:
            # La variable valores obtiene los valores de la seleccion en la posicion 0 del item desde el tree
            valores = self.tree.item(seleccion[0])["values"]
            self.limpiar()  # Llama a la funcion limpiar

            # El entries con la llave "Nombre" inserta en el inicio los valores en la posicion 1
            self.entries["Nombre"].insert(0, valores[1])

    # Crea la funcion obtener_datos con el atributo self
    def obtener_datos(self):
        # La variable nombre obtiene el dato del entries con la llave "Nombre"
        nombre = self.entries["Nombre"].get().strip()
        return nombre  # Devuelve la variable nombre

    # Crea la funcion eliminar con el atributo self
    def limpiar(self):

        # El entry recorre los valores de los entries
        for entry in self.entries.values():

            # Si hay una instancia dentro de entry que sea de tipo Entry
            if isinstance(entry, tk.Entry):
                # elimina el valor dentro del Entry desde el inicio hasta el final
                entry.delete(0, "end")

    # Crea la funcion agregar con el atributo self
    def agregar(self):

        # La variable datos va a obtener todo de la funcion obtener_datos
        datos = self.obtener_datos()

        # Si no hay datos
        if not datos:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encotraron datos"
            messagebox.showerror("Error", "No se encontraron datos")
            return  # No devuekve nada

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            # La variable cursor va a llamar al metodo cursor desde la variable conn
            cursor = conn.cursor()

            # Insertar datos en la tabla Categorias

            cursor.execute("""
                INSERT INTO categorias(nombre)
                VALUES (%s)
            """, (datos,))  # Usa el dato que este en la variable datos y una coma al final

            conn.commit()  # Llama al metodo commit para terminar de ejecutar el insert
            conn.close()  # Cierra la conexion
            self.cargar_categorias()  # Llama la funcion cargar_datos
            self.limpiar()  # Llama a la funcion limpiar
            # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Categoria agregada"
            messagebox.showinfo("Éxito", "Categoria agregada")

    # Crea la funcion actualizar con el atributo self
    def actualizar(self):

        # La variable seleccion llama a la funcion selection del tree
        seleccion = self.tree.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona una categoria"
            messagebox.showwarning("Selecciona", "Selecciona una categoria")
            return  # No devuelve nada

        # La variable item va llamar a la funcion item del tree para obtener la seleccion en la posicion 0
        item = self.tree.item(seleccion[0])
        # La variable categoria_id va a obtener el item con el valor en la posicion 0
        categoria_id = item["values"][0]
        # La variable datos va a llamar a la funcion obtener_datos
        datos = self.obtener_datos()

        # Si no hay datos
        if not datos:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encontraron datos"
            messagebox.showerror("Error", "No se encontraron datos")
            return  # No devuelve nada

        conn = conectar()  # La variable conn llama a la funcion conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Actualiza los datos de la tabla Categorias

            cursor.execute("""
                UPDATE categorias SET nombre=%s
                WHERE categoria_id=%s
            """, (datos, categoria_id))  # Usa datos una coma y luego el categoria_id

            conn.commit()  # Llama al metodo commit para terminar de actualizar los datos
            conn.close()  # Cierra la conexion
            self.cargar_categorias()  # Llama a la funcion cargar_categorias
            # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Categoria actualizada"
            messagebox.showinfo("Éxito", "Categoria actualizada")

    # Crea la funcion eliminar con el atributo self
    def eliminar(self):

        # La variable seleccion llama a la funcion selection del tree
        seleccion = self.tree.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona una categoria"
            messagebox.showwarning("Selecciona", "Selecciona una categoria")
            return  # No devuelve nada

        # Muestra un mensaje de si o no con el titulo "Confirmar" y con el mensaje "¿Eliminar categoria?" y en el caso de que se seleccione si
        if messagebox.askyesno("Confirmar", "¿Eliminar categoria?"):
            # La variable categoria_id obtiene el valor en la posicion del se la seleccion en la posicion 0 de la funcion item del tree
            categoria_id = self.tree.item(seleccion[0])["values"][0]

            conn = conectar()  # La variable conn llama al metodo conectar

            # Si hay conexion
            if conn:
                cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

                # Eliminar datos de la tabla Categorias

                cursor.execute(
                    "DELETE FROM categorias WHERE categoria_id=%s", (
                        categoria_id,))  # utiliza la variable categoria_id

                conn.commit()  # Llama al metodo commit de la variable conn para terminar de eliminar los datos
                conn.close()  # Cierra la conexion
                self.cargar_categorias()  # Llama a la funcion cargar_categorias
