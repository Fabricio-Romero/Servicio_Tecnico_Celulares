# Importa tkinter con el alias tk
import tkinter as tk
# Desde tkinter importa ttk y messagebox
from tkinter import ttk, messagebox
# Desde la carpeta Database y el archivo db_connection importa la funcion conectar
from Database.db_connection import conectar
# Desde la carpeta Modules y el archivo Brands importa la clase MarcasApp
from Modules.Brands import MarcasApp

# Crea la clase CelularesApp


class CelularesApp:
    # Crea la funcion __init__ con los atributos self y notebook
    def __init__(self, notebook):
        # La variable frame crea un Frame/marco dentro del parametro notebook
        frame = tk.Frame(notebook)
        # El parametro notebook agrega una pestania con el frame y con el texto "Gestionar Celulares y Marcas"
        notebook.add(frame, text="Gestionar Celulares y Marcas")

        # Labels y Entries de Gestion de celulares

        self.entries = {}  # Se crea el diccionario entries

        # Crea un label dentro del frame con el texto "GESTION DE CELULARES" y utiliza grid para ubicarlo en la fila 0, columna 2
        tk.Label(frame, text="GESTIÓN DE CELULARES").grid(row=0, column=2)

        # Crea un label/etiqueta dentro del frame con el texto "Modelo:" y utiliza grid/malla para ubicarlo en la fila 1, columna 0
        tk.Label(frame, text="Modelo:").grid(row=1, column=0)
        # Crea la llave "Modelo" en el entries el cual contiene un Entry/entrada dentro del frame y con un ancho de 25 pixeles
        self.entries["Modelo"] = tk.Entry(frame, width=25)
        # La llave "Modelo" del entries utiliza grid/malla para ubicarlo en la fila 1, columna 1
        self.entries["Modelo"].grid(row=1, column=1)

        # Crea un label/etiqueta dentro del frame con el texto "Marca:" Utiliza grid/malla para ubicarlo en la fila 2, columna 0
        tk.Label(frame, text="Marca:").grid(row=2, column=0)
        self.entries["Marca"] = ttk.Combobox(  # Crea la llave "Marca" en entries el cual contiene un combobox (caja de opciones)
            # Dentro del frame, con un ancho de 25 pixeles y el estado en readonly (solo lectura)
            frame, width=25, state="readonly")
        # La llave "Marca" del entriesm utiliza grid/malla para ubicarlo en la fila 2, columna 1
        self.entries["Marca"].grid(row=2, column=1)

        # Botones de gestion de celulares

        tk.Button(  # Crea un boton
            # Dentro del frame, con el texto "AGREGAR", con el fondo de color #6CFF22 y el color de la fuente en azul
            frame, text="AGREGAR", bg="#6CFF22", fg="blue",
            # La fuente va a ser Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.agregar_celulares  # Llama a la funcion agregar_celulares
            # Utiliza grid/malla para ubicarlo en la fila 3, columna 0, ocupa 2 columnas y deja un espacio de 5 pixeles en el eje X
        ).grid(row=3, column=0, columnspan=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del frame, con el texto "ACTUALIZAR", con el fondo de color #227EFF y con la fuente de color naranja
            frame, text="ACTUALIZAR", bg="#227EFF", fg="orange",
            # La fuente va a ser Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.actualizar_celulares  # Llama a la funcion actualizar_celulares
            # Utiliza grid/malla para ubicarlo en la fila 4, columna 0, ocupa 2 columnas y deja un espacio de 5 pixeles en el eje X
        ).grid(row=4, column=0, columnspan=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del frame, con el texto "ELIMINAR", con el fondo de color #F80000 y con la fuente de color negro
            frame, text="ELIMINAR", bg="#F80000", fg="black",
            # La fuente en Arial, de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.eliminar_celulares  # Llama a la funcion eliminar_celulares
            # Utiliza grid/malla para ubicarlo en la fila 5, columna 0, ocupa 2 columnas y deja un espacio de 5 pixeles en el eje X
        ).grid(row=5, column=0, columnspan=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del frame, con el texto "LIMPIAR", el fondo de color #00F2FF y con la fuente en color verde
            frame, text="LIMPIAR", bg="#00F2FF", fg="green",
            # La fuente en Arial, de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.limpiar  # Llama a la funcion limpiar
            # Utiliza grid para ubicarlo en la fila 6, columna 0, ocupa 2 columnas y deja un espacio de 5 pixeles en el eje X
        ).grid(row=6, column=0, columnspan=2, padx=5)

        # Tabla de celulares

        self.tree_gesCel = ttk.Treeview(  # La variable tree_gesCel crea un Treeview (tabla)
            frame,  # Dentro del frame
            # Con las columnas id, Modelo y Marca
            columns=("id", "Modelo", "Marca"),
            show="headings"  # Muestra solo las columnas mencionadas anteriormente
        )
        # col va a recorrer las columnas de la variable tree_gesCli
        for col in self.tree_gesCel["columns"]:
            # El encabezado del tree_gesCli va a estar en la posicion col y con el texto col
            self.tree_gesCel.heading(col, text=col)
            # Las columnas del tree_gesCli va a estar en la posicion col, con un ancho de 150 pixeles y va a estar anclado al centro
            self.tree_gesCel.column(col, width=150, anchor="center")
        self.tree_gesCel.grid(row=1, column=2, rowspan=6,  # Utiliza grid/malla para ubicarlo en la fila 1, columna 2, ocupa 6 filas
                              # Deja un espacio de 10 pixeles en ambos ejes y rellena con 200 pixeles en el eje Y
                              padx=10, pady=10, ipady=200)

        MarcasApp(frame)

        self.cargar_marcas()  # Llama a la funcion cargar_marcas
        self.cargar_celulares()  # Llama a la funcion cargar_celulares
        # Le bindea al TreeviewSelect del tree_gesCel la funcion seleccionar_celulares
        self.tree_gesCel.bind("<<TreeviewSelect>>", self.seleccionar_celulares)

    # Crea la funcion cargar_marcas con el atributo self
    def cargar_marcas(self):

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Consulta tabla Marcas

            cursor.execute("""
                SELECT *
                FROM marcas
                ORDER BY nombre DESC
            """)

        self.map_marcas = {}  # Crea el diccionario map_marcas
        lista = []  # Crea el arreglo lista

        # Para marca_id y texto que van a recorrer todo lo que obtenga cursor
        for marca_id, texto in cursor.fetchall():
            # La llave texto de map_marcas va a contener marca_id
            self.map_marcas[texto] = marca_id
            lista.append(texto)  # Agrega texto al arreglo lista

        # El valor de la llave Marca de entries va a ser lista
        self.entries["Marca"]["values"] = lista
        conn.close()  # Cierra la conexion

    def cargar_celulares(self):

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si no hay conexion
        if not conn:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se pudo conectar"
            messagebox.showerror("Error", "No se pudo conectar")
            return  # No devuelve nada

        # Para i que va a recorrer los hijos del tree_geCel
        for i in self.tree_gesCel.get_children():
            # Elimina los hijos que esten en i del tree_gesCel
            self.tree_gesCel.delete(i)

        # Consulta tabla Celulares

        cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

        cursor.execute("""
            SELECT ce.celular_id, ce.modelo, ma.nombre
            FROM celulares ce
            JOIN marcas ma ON ce.marca_id = ma.marca_id
            ORDER BY ma.nombre DESC
        """)

        # Para row que va a recorrer todo lo que obtenga cursor
        for row in cursor.fetchall():
            # Inserta desde el inicio hasta el final los valores en row dentro del tree_gesCel
            self.tree_gesCel.insert("", "end", values=row)

        conn.close()  # Cierra la conexion

    # Crea la funcion limpiar con el atributo self
    def limpiar(self):

        # Para entry que va a recorrer los valores de entries
        for entry in self.entries.values():

            # Si hay una insancia dentro del entry que sea de tipo Entry
            if isinstance(entry, tk.Entry):
                # Elimina desde el caracter 0 hasta el final
                entry.delete(0, "end")
            # Si no ocurre eso, pero hay una instancia dentro del entry que sea de tipo Combobox
            if isinstance(entry, ttk.Combobox):
                entry.set("")  # Establece el valor en " " (osea vacio)

    # Crea la funcion seleccionar_celulares con los atributos self y event
    def seleccionar_celulares(self, event):

        # La variable seleccion llama al metodo selection del tree_gesCel
        seleccion = self.tree_gesCel.selection()

        # Si hay seleccion
        if seleccion:
            # La variable valores obtiene los valores de la seleccion en la posicion 0 mediante el metodo item del tree_gesCel
            valores = self.tree_gesCel.item(seleccion[0])["values"]
            self.limpiar()  # Llama a la funcion limpiar

            # En la llave "Modelo" del entries inserta desde el inicio los valores en la posicion 1
            self.entries["Modelo"].insert(0, valores[1])
            # En la llave "Marca" del entries pone el valor que este en la posicion 2
            self.entries["Marca"].set(valores[2])

    # Crea la funcion obtener_datos_celulares con el atributo self
    def obtener_datos_celulares(self):

        # La variable modelo obtiene su valor de la llave "Modelo" del entries
        modelo = self.entries["Modelo"].get().strip()
        # La variable marca obtiene su valor de la llave "Marca" del entries
        marca = self.entries["Marca"].get()

        # La variable marca_id obtiene el id de la marca mediante el metodo get del map_marcas
        marca_id = self.map_marcas.get(marca)

        return modelo, marca_id  # Devuelve las variables modelo y marca_id

    # Crea la funcion agregar_celulares con el atributo self
    def agregar_celulares(self):

        # La variable datos llama a la funcion obtener_datos_celulares
        datos = self.obtener_datos_celulares()

        # Si no hay datos
        if not datos:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encontraron datos"
            messagebox.showerror("Error", "No se encontraron datos")
            return  # No devuelve nada

        conn = conectar()  # La variable datos llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama a la funcion cursor de la variable conn

            # Insertar datos en la tabla celulares

            cursor.execute("""
                INSERT INTO celulares (modelo, marca_id)
                VALUES (%s, %s)
            """, (*datos,))  # Separa la variable datos utilizando coma

        conn.commit()  # Termina de ejecutar el insert
        conn.close()  # Cierra la conexion
        self.cargar_celulares()  # Llama a la funcion cargar_celulares
        self.limpiar()  # Llama a la funcion limpiar
        # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Celular agregado"
        messagebox.showinfo("Éxito", "Celular agregado")

    # Crea la funcion actualizar_celulares con el atributo self
    def actualizar_celulares(self):

        # La variable seleccion llama al metodo selection del tree_gesCel
        seleccion = self.tree_gesCel.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona un celular"
            messagebox.showwarning("Selecciona", "Selecciona un celular")
            return  # No devuelve nada

        # La variable item va a seleccionar el item en la posicion 0 del tree_gesCel
        item = self.tree_gesCel.item(seleccion[0])
        # La variable celular_id obtiene los valores en la posicion 0 de item
        celular_id = item["values"][0]
        # La variable datos llama a la funcion obtener_datos_celulares
        datos = self.obtener_datos_celulares()

        # Si no hay datos
        if not datos:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encontraron datos"
            messagebox.showerror("Error", "No se encontraron datos")
            return  # No devuelve nada

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Actualizar datos tabla celulares

            cursor.execute("""
                UPDATE celulares
                SET modelo=%s, marca_id=%s
                WHERE celular_id=%s
            """, (*datos, celular_id))  # Separa los datos de la variable datos y utiliza coma, luego utiliza la variable celular_id

        conn.commit()  # Termina de ejecutar la actualizacion de los datos
        conn.close()  # Cierra la conexion
        self.cargar_celulares()  # Llama a la funcion cargar_celulares
        # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Celular actualizado"
        messagebox.showinfo("Éxito", "Celular actualizado")

    # Crea la funcion eliminar celulares con el atributo self
    def eliminar_celulares(self):

        # La variable seleccion llama al metodo selection de tree_gesCel
        seleccion = self.tree_gesCel.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona un celular"
            messagebox.showwarning("Selecciona", "Selecciona un celular")
            return  # No devuelve nada

        # Si el usuario presiona "Si" en el mensaje de tipo si o no con el titulo "Confirmar" y con el mensaje "¿Eliminar celular?"
        if messagebox.askyesno("Confirmar", "¿Eliminar celular?"):
            # La variable celular_id va a obtener el valor en la posicion 0 de la seleccion en la posicion 0 mediante el metodo item dem tree_gesCel
            celular_id = self.tree_gesCel.item(seleccion[0])["values"][0]

            conn = conectar()  # La variable conn llama al metodo conectar

            # Si hay conexion
            if conn:
                cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

                # Eliminar datos de la tabla celulares

                cursor.execute("""
                    DELETE FROM celulares
                    WHERE celular_id=%s
                """, (celular_id,))  # Utiliza la variable celular_id con una coma al final

                conn.commit()  # Termina de ejecutar la eliminacion de datos
                conn.close()  # Cierra la conexion
                self.cargar_celulares()  # Llama a la funcion cargar_celulares
