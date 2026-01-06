# modules/Customers.py

# Importa tkinter como tk
import tkinter as tk
# Desde tkinter importa ttk y messagebox
from tkinter import ttk, messagebox
# Desde la carpeta Database y el archivo db_connection importa el metodo conectar
from Database.db_connection import conectar

# Crea la calse TrabajosApp


class TrabajosApp:
    # Crea la funcion __init__ con los atributos self y root
    def __init__(self, root):
        self.root = root  # La variable root hace referencia al parametro root
        self.root.title("Trabajos")  # El titulo del root es "Trabajos"

        # La variable notebook crea un Notebook en el root
        notebook = ttk.Notebook(root)
        # Empaqueta notebook dejando 10 pixeles en el eje Y y 20 pixeles en el eje X, rellena en ambos ejes y puede expandirse
        notebook.pack(pady=10, padx=20, fill="both", expand=True)

        # Pestaña 1: Trabajos

        # La variable frame1 Crea un frame dentro del notebook
        frame1 = tk.Frame(notebook)
        # La variable notebook agrega una pagina que va a contener el frame1 y el texto "Trabajos"
        notebook.add(frame1, text="Trabajos")
        # La variable form_frame crea un frame/marco dentro del frame1
        form_frame = tk.Frame(frame1)
        # Empaqueta el form_fame con una separacion de 20 pixeles en ambos ejes
        form_frame.pack(padx=20, pady=20)

        # Labels y Entries

        self.entries = {}  # Crea el diccionario entries

        tk.Label(form_frame, text="Estado:").grid(  # Crea un label/etiqueta dentro del form_frame con el texto "Estado:"
            # Utiliza grid/malla para ubicarlo en la fila 0, columan 2, posicionarlo lo mas al west/oeste (izquierda) posible y deja una separacion de 2 pixeles en el eje y
            row=0, column=2, sticky="w", pady=2)
        self.entries["Estado"] = ttk.Combobox(form_frame, width=25,  # Crea la llave "Estado" dentro del entries el cual va a contener un combobox dentro del form_frame con un ancho de 25 pixeles
                                              # Con los valores "listo", "pendiente", "en proceso" y tiene el estado en solo lectura
                                              values=["listo", "pendiente", "en proceso"], state="readonly")
        self.entries["Estado"].grid(  # Utiliza grid/malla en la llave "Estado" del entries
            # Lo ubica en la fila 0, columna 3, con una separacion de 2 pixeles en el eje Y y 5 Pixeles en el eje X
            row=0, column=3, pady=2, padx=5)
        # Establece la llave "Estado" del entries en "pendiente" de manera predeterminada
        self.entries["Estado"].set("pendiente")

        tk.Label(form_frame, text="Falla:").grid(  # Crea un label/etiqueta dentro del form_form, con el texto "Falla:"
            # Utiliza grid para ubicarlo en la fila 0, columna 4, la va a posicionar lo mas al west/oeste (izquierda) posible y con una separacion de 2 pixeles en el eje Y
            row=0, column=4, sticky="w", pady=2)
        self.entries["Falla"] = tk.Text(  # Crea la llave "Falla" en entries, la cual va a tener un Text/texto
            # Dentro del form_frame, con un ancho de 25 pixeles y 3 pixeles de alto
            form_frame, width=25, height=3)
        self.entries["Falla"].grid(  # La llave "Falla" utiliza grid
            # Para ubicarlo en la fila 0, columna 5, con una separacion de 2 pixeles en el eje Y y 5 pixeles en el eje X y ocupa 3 filas
            row=0, column=5, pady=2, padx=5, rowspan=3)

        tk.Label(form_frame, text="IMEI:").grid(  # Crea un label/etiqueta dentro del form_frame, con el texto "IMEI:"
            # Utiliza grid para ubicarlo en la fila 0, columna 6, lo posiciona lo mas al west/oeste (izquierda) posible y dejando una separacion de 2 pixeles en el eje Y
            row=0, column=6, sticky="w", pady=2)
        # Crea la llave "IMEI" en entries el cual contiene un Entry/entrada dentro del form_frame y con un ancho de 25 pixeles
        self.entries["IMEI"] = tk.Entry(form_frame, width=25)
        self.entries["IMEI"].grid(  # La llave "IMEI" utiliza grid
            # Para ubicarlo en la fila 0, columna 7, dejando una separacion de 2 pixeles en el eje Y y 5 pixeles en el eje X
            row=0, column=7, pady=2, padx=5)

        tk.Label(form_frame, text="Celular:").grid(  # Crea un label/etiqueta dentro del form_frame, con el texto "Celular:"
            # Utiliza grid para ubicarlo en la fila 0, columna 8, posicionarlo lo mas al west/oeste (izquierda) posible y con una separacion de 2 pixeles en el eje Y
            row=0, column=8, sticky="w", pady=2)
        self.entries["Celular"] = ttk.Combobox(  # Crea la llave "Celular" en entries el cual contiene un Combobox (caja de opciones)
            # Dentro del form_frame, con un ancho de 25 pixeles y lo pone en estado "readonly" (solo lectura)
            form_frame, width=25, state="readonly")
        self.entries["Celular"].grid(  # La llave "Celular" utiliza grid
            # Lo ubica en la fila 0, columna 9, con una separacion de 2 pixeles en eje Y y 5 pixeles en el eje X
            row=0, column=9, pady=2, padx=5)

        tk.Label(form_frame, text="Cliente:").grid(  # Crea un label/etiqueta dentro del form_frame, com el texto "Cliente:"
            # Utiliza grid para unicarlo en la fila 0, columna 10, lo posiciona lo mas al west/oeste (izquierda) posible y deja una separacion de 2 pixeles en el eje Y
            row=0, column=10, sticky="w", pady=2)
        self.entries["Cliente"] = ttk.Combobox(  # Crea la llave "Cliente" la cual crea un combobox (caja de opciones)
            # Dentro del form_frame, con un ancho de 25 pixeles y con estado en readonly (solo lectura)
            form_frame, width=25, state="readonly")
        self.entries["Cliente"].grid(  # La llave "Cliente" utiliza grid/malla
            # Lo ubica en la fila 0, columna 11, dejando una separacion de 2 pixeles en el eje Y y 5 pixeles en el eje X
            row=0, column=11, pady=2, padx=5)

        # Botones

        # La variable button_frame crea un frame/marco dentro del frame1
        button_frame = tk.Frame(frame1)
        # Empaqueta la variable button_frame con una separacion de 2 pixeles en ambos ejes
        button_frame.pack(pady=2, padx=2)

        tk.Button(  # Crea un boton
            # Dentro del button_frame, con el texto "AGREGAR", con el fondo de color #6CFF22 y el color de la fuente es azul
            button_frame, text="AGREGAR", bg="#6CFF22", fg="blue",
            # La fuente va a ser Arial, de tamanio 10 con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.agregar_trabajos  # Llama a la funcion agregar_trabajos
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 0, dejando una separacion de 5 pixeles en el eje X
        ).grid(row=0, column=0, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del button_frame, con el texto "ACTUALIZAR", el fondo de color #227EFF y el color de la fuente es naranja
            button_frame, text="ACTUALIZAR", bg="#227EFF", fg="orange",
            # La fuente va a ser Arial, de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.actualizar_trabajos  # Llama a la funcion actualizar_trabajos
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 1 y dejando una separacion de 5 pixeles en el eje X
        ).grid(row=0, column=1, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del button_frame, con el texto "ELIMINAR", el fondo de color #F80000 y el color de la fuente en negro
            button_frame, text="ELIMINAR", bg="#F80000", fg="black",
            # La fuente va a ser Arial, de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.eliminar_trabajos  # Llama a la fiuncion eliminar_trabajos
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 2 y dejando una separacion de 5 pixeles en el eje X
        ).grid(row=0, column=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del buton_frame, con el texto "LIMPIAR", con el fondo de color #00F2FF y con el color de fuente en verde
            button_frame, text="LIMPIAR", bg="#00F2FF", fg="green",
            # La fuente va a ser Arial, de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.limpiar  # Llama a la funcion limpiar
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 3 y dejando una separacion de 5 pixeles en el eje X
        ).grid(row=0, column=3, padx=5)

        # Tabla Trabajos

        self.tree_trabajo = ttk.Treeview(  # La variable tree_trabajo crea un Treeview (Tabla)
            frame1,  # Dentro del frame1
            columns=("id", "Fecha", "Estado", "Falla",  # Con las columnas id, Fecha, Estado, Falla, IMEI, Celular y Cliente
                     "IMEI", "Celular", "Cliente"),
            show="headings"  # Muestra solo las columnas anteriormente mencionadas
        )
        # col y text van a recorrer las columnas del tree_trabajo que estan comprimidas, obteniendo asi la posicion donde se encuentra (col) y el texto que contiene dentro (text)
        for col, text in zip(
            self.tree_trabajo["columns"],
            ["id", "Fecha", "Estado", "Falla", "IMEI", "Celular", "Cliente"]
        ):
            # El encabezado de la tabla se ubica en la columna col con el texto text
            self.tree_trabajo.heading(col, text=text)
            # La columna col va a tener un ancho de 200 pixeles y va a estar anclado al centro
            self.tree_trabajo.column(col, width=200, anchor="center")
            # La columna "id" va a tene un ancho de 20 pixeles y va a estar anclado al centro
            self.tree_trabajo.column("id", width=20, anchor="center")
        # Empaqueta el tree_trabajo para que rellene ambos ejes, que se pueda expandir y dejando una separacion de 10 pixeles en ambos ejes
        self.tree_trabajo.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña 2: Gestionar Celulares y Marcas

        # La variable frame2 crea un Frame/marco dentro del notebook
        frame2 = tk.Frame(notebook)
        # La variable notebook agrega una pestania dentro del frame2 y con el texto "Gestionar Celulares y Marcas"
        notebook.add(frame2, text="Gestionar Celulares y Marcas")

        # Labels y Entries de Gestion de celulares

        # Crea un label dentro del frame2 con el texto "GESTION DE CELULARES" y utiliza grid para ubicarlo en la fila 0, columna 2
        tk.Label(frame2, text="GESTIÓN DE CELULARES").grid(row=0, column=2)

        # Crea un label/etiqueta dentro del frame2 con el texto "Modelo:" y utiliza grid/malla para ubicarlo en la fila 1, columna 0
        tk.Label(frame2, text="Modelo:").grid(row=1, column=0)
        # Crea la llave "Modelo" en el entries el cual contiene un Entry/entrada dentro del frame2 y con un ancho de 25 pixeles
        self.entries["Modelo"] = tk.Entry(frame2, width=25)
        # La llave "Modelo" del entries utiliza grid/malla para ubicarlo en la fila 1, columna 1
        self.entries["Modelo"].grid(row=1, column=1)

        # Crea un label/etiqueta dentro del frame2 con el texto "Marca:" Utiliza grid/malla para ubicarlo en la fila 2, columna 0
        tk.Label(frame2, text="Marca:").grid(row=2, column=0)
        self.entries["Marca"] = ttk.Combobox(  # Crea la llave "Marca" en entries el cual contiene un combobox (caja de opciones)
            # Dentro del frame2, con un ancho de 25 pixeles y el estado en readonly (solo lectura)
            frame2, width=25, state="readonly")
        # La llave "Marca" del entriesm utiliza grid/malla para ubicarlo en la fila 2, columna 1
        self.entries["Marca"].grid(row=2, column=1)

        # Botones de gestion de celulares

        tk.Button(  # Crea un boton
            # Dentro del frame2, con el texto "AGREGAR", con el fondo de color #6CFF22 y el color de la fuente en azul
            frame2, text="AGREGAR", bg="#6CFF22", fg="blue",
            # La fuente va a ser Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.agregar_celulares  # Llama a la funcion agregar_celulares
            # Utiliza grid/malla para ubicarlo en la fila 3, columna 0, ocupa 2 columnas y deja un espacio de 5 pixeles en el eje X
        ).grid(row=3, column=0, columnspan=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del frame2, con el texto "ACTUALIZAR", con el fondo de color #227EFF y con la fuente de color naranja
            frame2, text="ACTUALIZAR", bg="#227EFF", fg="orange",
            # La fuente va a ser Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.actualizar_celulares  # Llama a la funcion actualizar_celulares
            # Utiliza grid/malla para ubicarlo en la fila 4, columna 0, ocupa 2 columnas y deja un espacio de 5 pixeles en el eje X
        ).grid(row=4, column=0, columnspan=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del frame2, con el texto "ELIMINAR", con el fondo de color #F80000 y con la fuente de color negro
            frame2, text="ELIMINAR", bg="#F80000", fg="black",
            # La fuente en Arial, de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.eliminar_celulares  # Llama a la funcion eliminar_celulares
            # Utiliza grid/malla para ubicarlo en la fila 5, columna 0, ocupa 2 columnas y deja un espacio de 5 pixeles en el eje X
        ).grid(row=5, column=0, columnspan=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del frame2, con el texto "LIMPIAR", el fondo de color #00F2FF y con la fuente en color verde
            frame2, text="LIMPIAR", bg="#00F2FF", fg="green",
            # La fuente en Arial, de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.limpiar  # Llama a la funcion limpiar
            # Utiliza grid para ubicarlo en la fila 6, columna 0, ocupa 2 columnas y deja un espacio de 5 pixeles en el eje X
        ).grid(row=6, column=0, columnspan=2, padx=5)

        # Tabla de celulares

        self.tree_gesCel = ttk.Treeview(  # La variable tree_gesCel crea un Treeview (tabla)
            frame2,  # Dentro del frame2
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

        # Labels y entries de marcas

        # Crea un label/etiqueta dentro del frame2, con el texto "GESTION DE MARCAS" y utiliza grid/malla para ubicarlo en la fila 0, columna 5
        tk.Label(frame2, text="GESTIÓN DE MARCAS").grid(row=0, column=5)

        # Crea un label/etiqueta en el frame2, con el texto "Marca:" y utiliza grid para ubicarlo en la fila 1, columna 3
        tk.Label(frame2, text="Marca:").grid(row=1, column=3)
        # Crea la llave GesMarca en entries la cual crea un Entry/entrada dentro del frame2 y con un ancho de 25 pixeles
        self.entries["GesMarca"] = tk.Entry(frame2, width=25)
        # La llave GesMarca utiliza grid para ubicarlo en la fila 1, columna 4
        self.entries["GesMarca"].grid(row=1, column=4)

        # Botones de Marcas

        tk.Button(  # Crea un boton
            # Dentro del frame2, con el texto "AGREGAR", con el fondo #6CFF22 y con la fuente de color azul
            frame2, text="AGREGAR", bg="#6CFF22", fg="blue",
            # La fuente va a ser Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.agregar_marcas  # Llama a la funcion agregar_marcas
            # Utiliza grid/malla para ubicarlo en la fila 2, columna 3, ocupa 2 columnas y deja un espacio de 5 pixeles en el eje X
        ).grid(row=2, column=3, columnspan=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del frame2, con el texto "ACTUALIZAR", el fondo de color #2273FF y con la fuente de color naranja
            frame2, text="ACTUALIZAR", bg="#227EFF", fg="orange",
            # La fuente va a ser Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.actualizar_marcas  # Llama a la funcion actualizar_marcas
            # Utiliza grid para ubicarlo en la fila 2, columna 3, ocupa 2 columnas y deja un espacio de 5 pixeles en el eje X
        ).grid(row=3, column=3, columnspan=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del frame2, con el texto "ELIMINAR", con el fondo de color # F80000 y con la fuente de color negro
            frame2, text="ELIMINAR", bg="#F80000", fg="black",
            # La fuente va a ser Arial de tamanio 10 con la propieda bold/negrita
            font=("Arial", 10, "bold"),
            command=self.eliminar_marcas  # Llama a la funcion eliminar_marcas
            # Utiliza grid para ubicarlo en la fila 4, columna 3, ocupa 2 columnas y deja un espacio de 5 pixeles en eje X
        ).grid(row=4, column=3, columnspan=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del frame2, con el texto "LIMPIAR", con el fondo de color #00F2F y con el color de la fuente de color verde
            frame2, text="LIMPIAR", bg="#00F2FF", fg="green",
            # La fuente va a ser Arial de tamanio 10 con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.limpiar  # Llama a la funcion limpiar
            # Utiliza grid/malla para ubicarlo en la fila 5, columna 3, ocupa 2 columnas y deja un espacio de 4 pixeles en el eje X
        ).grid(row=5, column=3, columnspan=2, padx=5)

        # Tabla de Marcas

        self.tree_gesMar = ttk.Treeview(  # La variable tree_gesMar crea un Treeview (tabla)
            frame2,  # Dentro del frame2
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

        self.cargar_celulares()  # Llama a la funcion cargar_celulares
        self.cargar_clientes()  # Llama a la funcion cargar_clientes
        self.cargar_marcas()  # Llama a la funcion cargar_marcas
        # Llama a la funcion cargar_trabajos_celulares_marcas
        self.cargar_trabajos_celulares_marcas()
        # Le bindea al TreeviewSelect del tree_trabajo la funcion seleccionar_trabajos
        self.tree_trabajo.bind("<<TreeviewSelect>>", self.seleccionar_trabajos)
        # Le bindea al TreeviewSelect del tree_gesCel la funcion seleccionar_celulares
        self.tree_gesCel.bind("<<TreeviewSelect>>", self.seleccionar_celulares)
        # Le bindea al treeviewSelect del tree_gesMar la funcion seleccionar_marcas
        self.tree_gesMar.bind("<<TreeviewSelect>>", self.seleccionar_marcas)

    # Crea la funcion cargar_celulares con el atrubuto self
    def cargar_celulares(self):

        conn = conectar()  # La varaible conn hace referencia al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama a la funcion cursor de la variable conn

            # Consulta tabla Celulares

            cursor.execute(  # La variable cursor llama al metodo execute
                """SELECT ce.celular_id, CONCAT(ma.nombre, ' ', ce.modelo)
                    FROM celulares ce
                    JOIN marcas ma ON ce.marca_id = ma.marca_id
                    ORDER BY ce.modelo DESC
                           """)

        self.map_celulares = {}  # Crea el diccionario map_celulares
        lista = []  # Crea el arreglo lista

        # Para celular_id y texto que van a recorrer todo lo que obtenga cursor
        for celular_id, texto in cursor.fetchall():
            # Va a crear una llave texto que va a contener el celular_id
            self.map_celulares[texto] = celular_id
            lista.append(texto)  # Agrega texto al arreglo lista

        # En la llave celular del entries su valor va a ser lista
        self.entries["Celular"]["values"] = lista
        conn.close()  # Cierra la conexion

    # Crea la funcion cargar_clientes con el atributo self
    def cargar_clientes(self):

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Consulta tavla Clientes

            cursor.execute(
                """SELECT cliente_id, CONCAT(nombre, ' ', apellido)
                    FROM clientes                    
                    ORDER BY nombre DESC
                           """)

        self.map_clientes = {}  # Crea el diccionario map_clientes
        lista = []  # Crea el arreglo lista

        # Para cliente_id y texto que van a recorrer todo lo que obtenga la variable cursor
        for cliente_id, texto in cursor.fetchall():
            # La llave texto de map_clientes va a tener el cliente_id
            self.map_clientes[texto] = cliente_id
            lista.append(texto)  # Agrega texto al arreglo lista

        # El valor de la llave Cliente de entries es lista
        self.entries["Cliente"]["values"] = lista
        conn.close()  # Cierra la conexion

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

    # Crea la funcion cargar_trabajos_celulares_marcas con el atributo self

    def cargar_trabajos_celulares_marcas(self):

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si no hay conexion
        if not conn:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se pudo conectar"
            messagebox.showerror("Error", "No se pudo conectar")
            return  # No devuelve nada

        cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

        # Trabajos

        # Para i que va a recorrer los hijos de tree_trabajos
        for i in self.tree_trabajo.get_children():
            # Elimina los hijos que esten en i del tree_trabajo
            self.tree_trabajo.delete(i)

        # Consulta tabla trabajos

        cursor.execute("""
            SELECT t.trabajo_id, t.fecha, t.estado, t.descripcion, t.IMEI, CONCAT(ma.nombre, ' ', ce.modelo) AS celular, CONCAT(c.nombre, ' ', c.apellido) AS cliente
            FROM trabajos t
            JOIN celulares ce ON t.celular_id = ce.celular_id
            JOIN marcas ma ON ce.marca_id = ma.marca_id
            JOIN clientes c ON t.cliente_id = c.cliente_id
            ORDER BY t.fecha DESC
        """)

        # Para row que va a recorrer todo lo que obtenga cursor
        for row in cursor.fetchall():
            # Inserta desde el inicio hasta el final los valores en row dentro del tree_trabajo
            self.tree_trabajo.insert("", "end", values=row)

        # Celulares

        # Para i que va a recorrer los hijos del tree_geCel
        for i in self.tree_gesCel.get_children():
            # Elimina los hijos que esten en i del tree_gesCel
            self.tree_gesCel.delete(i)

        # Consulta tabla Celulares

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

        # Marcas

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

    # Crea la funcion seleccionar_trabajos con los atributos self y event
    def seleccionar_trabajos(self, event):

        # La variable seleccion llama al metodo selection del tree_trabajo
        seleccion = self.tree_trabajo.selection()

        # Si hay seleccion
        if seleccion:
            # La variable valores obtiene todos los valores de la seleccion en la posicion 0 mediante el metodo item del tree_trabajo
            valores = self.tree_trabajo.item(seleccion[0])["values"]
            self.limpiar()  # Llama a la funcion limpiar

            # En la llave "Estado" del entries pone el valor que este en la posicion 2
            self.entries["Estado"].set(valores[2])
            # En la llave "Falla" del entries inserta el valor en la posicion 3 desde el inicio
            self.entries["Falla"].insert("1.0", valores[3])
            # En la llave "IMEI" del entries inserta el valor en la posicion 4 desde el inicio
            self.entries["IMEI"].insert(0, valores[4])
            # En la llave "Celular" del entries pone el valor que este en la posicion 5
            self.entries["Celular"].set(valores[5])
            # En la llave "Cliente" del entries pone el valor que este en la posicion 6
            self.entries["Cliente"].set(valores[6])

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

    # Crea la funcion obtener_datos_trabajos con el atributo self
    def obtener_datos_trabajos(self):

        # La variable estado obtiene su valor de la llave "Estado" del entries
        estado = self.entries["Estado"].get()
        # La variable falla obtiene su valor de la llave "Falla" del entries desde el inicio hasta el final
        falla = self.entries["Falla"].get("1.0", "end").strip()
        # La variable imei obtiene su valor de la llave "IMEI" del entries
        imei = self.entries["IMEI"].get().strip()
        # La variable celular obtiene su valor de la llave "Celular" del entries
        celular = self.entries["Celular"].get()
        # La variable cliente obtiene su valor de la llave "Cliente" del entries
        cliente = self.entries["Cliente"].get()

        # Convertir texto → ID
        # La variable celular_id botiene el id del celular mediante el metodo get de map_celulares
        celular_id = self.map_celulares.get(celular)
        # La variable cliente_id obtiene el id del cliente mediante el metodo get de map_clientes
        cliente_id = self.map_clientes.get(cliente)

        # Devuelve las variables estado, falla, imei, celular_id y cliente_id
        return estado, falla, imei, celular_id, cliente_id

    # Crea la funcion obtener_datos_celulares con el atributo self
    def obtener_datos_celulares(self):

        # La variable modelo obtiene su valor de la llave "Modelo" del entries
        modelo = self.entries["Modelo"].get().strip()
        # La variable marca obtiene su valor de la llave "Marca" del entries
        marca = self.entries["Marca"].get()

        # La variable marca_id obtiene el id de la marca mediante el metodo get del map_marcas
        marca_id = self.map_marcas.get(marca)

        return modelo, marca_id  # Devuelve las variables modelo y marca_id

    # Crea la funcion obtener_datos_marcas con el atributo self
    def obtener_datos_marcas(self):

        # La variable marca obtiene su valor de la llave "GesMarca" del entries
        marca = self.entries["GesMarca"].get().strip()

        return marca  # Devuelve la variable marca

    # Crea la funcion limpiar con el atributo self
    def limpiar(self):

        # Para entry que va a recorrer los valores de entries
        for entry in self.entries.values():

            # Si hay una insancia dentro del entry que sea de tipo Entry
            if isinstance(entry, tk.Entry):
                # Elimina desde el caracter 0 hasta el final
                entry.delete(0, "end")
            # Si no ocurre eso, pero hay una instancia dentro del entry que sea de tipo Text
            elif isinstance(entry, tk.Text):
                # Elimina desde el inicio hasta el final
                entry.delete("1.0", "end")
            # Si no ocurre eso, pero hay una instancia dentro del entry que sea de tipo Combobox
            elif isinstance(entry, ttk.Combobox):
                entry.set("")  # Establece el valor en " " (osea vacio)

    # Crea la funcion agregar_trabajos con el atributo self
    def agregar_trabajos(self):

        # La variable datos llama a la funcion obtener_datos_trabajos
        datos = self.obtener_datos_trabajos()

        # Si no hay datos
        if not datos:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encuentran datos"
            messagebox.showerror("Error", "No se encuentran datos")
            return  # No devuelve nada

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Insertar datos en la tabla Trabajos

            cursor.execute("""
                INSERT INTO trabajos (estado, descripcion, IMEI, celular_id, cliente_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (*datos,))  # Separa lo que tenga la variable datos utilizando una coma al final de cada separacion

            conn.commit()  # Termina de ejecutar el insert
            conn.close()  # Cierra la conexion
            # Llama a la funcion cargar_trabajos_celulares_marcas
            self.cargar_trabajos_celulares_marcas()
            self.limpiar()  # Llama a la funcion limpiar
            # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Trabajo agregado"
            messagebox.showinfo("Éxito", "Trabajo agregado")

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
        # Llama a la funcion cargar_trabajos_celulares_marcas
        self.cargar_trabajos_celulares_marcas()
        self.limpiar()  # Llama a la funcion limpiar
        # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Celular agregado"
        messagebox.showinfo("Éxito", "Celular agregado")

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
        # Llama a la funcion cargar_trabajos_celulares_marcas
        self.cargar_trabajos_celulares_marcas()
        self.limpiar()  # Llama a la funcion limpiar
        # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Marca agregada"
        messagebox.showinfo("Éxito", "Marca agregada")

    # Crea la funcion actualizar_trabajos con el atributo self
    def actualizar_trabajos(self):

        # La variable seleccion llama al metodo selection del tree_trabajo
        seleccion = self.tree_trabajo.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona un trabajo"
            messagebox.showwarning("Selecciona", "Selecciona un trabajo")
            return  # No devuelve nada

        # La variable item va a tomar el item que este en la posicion 0 de la seleccion
        item = self.tree_trabajo.item(seleccion[0])
        # La variable trabajo_id va a tomar los valores de la posicion 0 del item
        trabajo_id = item["values"][0]
        # La variable datos llama a la funcion obtener_datos_trabajos
        datos = self.obtener_datos_trabajos()

        # Si no hay datos
        if not datos:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encontraron datos"
            messagebox.showerror("Error", "No se encontraron datos")
            return  # No devuelve nada

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Actualizar tabla trabajos

            cursor.execute("""
                UPDATE trabajos SET estado=%s, descripcion=%s, IMEI=%s, celular_id=%s, cliente_id=%s
                WHERE trabajo_id=%s
            """, (*datos, trabajo_id))  # Separa los datos de la variable datos con una coma y luego utiliza trabajo_id

            conn.commit()  # Termina de ejecutar la actualizacion de datos
            conn.close()  # Cierra la conexion
            # Llama a la funcion cargar_trabajos_celulares_marcas
            self.cargar_trabajos_celulares_marcas()
            # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Trabajo actualizado"
            messagebox.showinfo("Éxito", "Trabajo actualizado")

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
        # Llama a la funcion cargar_trabajos_celulares_marcas
        self.cargar_trabajos_celulares_marcas()
        # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Celular actualizado"
        messagebox.showinfo("Éxito", "Celular actualizado")

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
        # Llama a la funcion cargar_trabajos_celulares_marcas
        self.cargar_trabajos_celulares_marcas()
        # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Marca actualizada"
        messagebox.showinfo("Éxito", "Marca Actualizada")

    # Crea la funcion eliminar_trabajos con el atributo self
    def eliminar_trabajos(self):

        # La variable seleccion llama al metodo selection del tree_trabajo
        seleccion = self.tree_trabajo.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona un trabajo"
            messagebox.showwarning("Selecciona", "Selecciona un trabajo")
            return  # No devuelve nada

        # Si el usuario responde "Si" en el mensaje con el titulo "Confirmar" y con el mensaje "¿Eliminar trabajo?"
        if messagebox.askyesno("Confirmar", "¿Eliminar trabajo?"):
            # La variable trabajo_id obitene el valor en la posicion 0 de la seleccion en la posicion 0 mediante el metodo item del tree_trabajo
            trabajo_id = self.tree_trabajo.item(seleccion[0])["values"][0]

            conn = conectar()  # La variable conn llama al metodo conectar

            # Si hay conexion
            if conn:
                cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

                # Eliminar datos tabla trabajos

                cursor.execute(
                    "DELETE FROM trabajos WHERE trabajo_id=%s", (
                        trabajo_id,)
                )

                conn.commit()  # Termina de ejecutar la eliminacion de datos
                conn.close()  # Cierra la conexion
                # Llama a la funcion cargar_trabajos_celulares_marcas
                self.cargar_trabajos_celulares_marcas()

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
                # Llama al metodo cargar_trabajos_celulares_marcas
                self.cargar_trabajos_celulares_marcas()

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
                # Llama a la funcion cargar_trabajos_celulares_marcas
                self.cargar_trabajos_celulares_marcas()
