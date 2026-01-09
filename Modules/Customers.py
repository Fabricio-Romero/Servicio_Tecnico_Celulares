# modules/Customers.py

# Importa tkinter como tk
import tkinter as tk
# Desde tkinter importa ttk y messagebox
from tkinter import ttk, messagebox
# Desde la carpeta Database y el archivo db_connection importa el metodo conectar
from Database.db_connection import conectar

# Crea la clase ClientesApp


class ClientesApp:
    # Crea la funcion __init__ con el atributo self y root
    def __init__(self, root):

        self.root = root  # La variable root hace referencia al parametro root
        self.root.title("Clientes")  # El titulo del root es "Clientes"

        # La variable notebook crea un Notebook en el root
        notebook = ttk.Notebook(root)
        # Empaqueta el notebook dejando un espacio de 10 pixeles en el eje Y, 20 pixeles en el eje X, rellena en ambos ejes y puede exepandirse
        notebook.pack(pady=10, padx=20, fill="both", expand=True)

        # Pestaña 1: Clientes

        # La variable frame1 crea un frame en el notebook
        frame1 = tk.Frame(notebook)
        # agrega frame1 al notebook con el texto "Clientes"
        notebook.add(frame1, text="Clientes")

        # Tabla Clientes

        self.tree_cliente = ttk.Treeview(  # La variable tree_cliente crea un Treeview
            frame1,  # Se ubica en el frame1
            # Con las columnas "Nombre", "Apellido", "Contacto"
            columns=("Nombre", "Apellido", "Contacto"),
            show="headings"  # Muestra las columnas en el encabezado
        )

        # col y text van a recorrer las posiciones y los datos del tree_cliente
        for col, text in zip(
            self.tree_cliente["columns"],
            ["Nombre", "Apellido", "Contacto"]
        ):
            # El encabezado en la posicion col va a tener el texto text
            self.tree_cliente.heading(col, text=text)
            # La columna en la posicion col va a tener un ancho de 200 pixeles y se va a centrar
            self.tree_cliente.column(col, width=200, anchor="center")
        # Empaqueta el tree_cliente llenando ambos ejes, permitiendo expandirse, separado 10 pixeles en el eje X e Y
        self.tree_cliente.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña 2: Gestionar Clientes

        # La variable frame2 crea un frame dentro del notebook
        frame2 = tk.Frame(notebook)
        # La variable notebook agrega una pestania con el texto "Gestionar Clientes"
        notebook.add(frame2, text="Gestionar Clientes")
        # La variable form_frame crea un frame/marco dentro del frame2
        form_frame = tk.Frame(frame2)
        # Empaqueta el form_frame con una separacion de 20 pixeles en el eje X y 15 pixeles en el eje Y
        form_frame.pack(padx=20, pady=15)

        # Labels y Entries

        self.entries = {}  # Crea el diccionario entries

        # El arreglo campos guarda el nombre de los labels y entries
        campos = ["Nombre", "Apellido", "Contacto"]

        # Para i y campo que van a recorrer la enumeracion de campos
        for i, campo in enumerate(campos):
            # La variable i va a guardar numeros impares (la posicion de las columnas Labels)
            i += i + 1
            # La variable j va a guardar numero pares (la posicion de las columnas de los Entries)
            j = i + 1
            # Crea un Label/Etiqueta dentro del form_frame con el texto campo mas ":", Utiliza grid para ubicarlo en la fila 0, columna i, lo posiciona lo mas al west/oeste (izquierda) posible y deja un espacio de 2 pixeles en el eje Y
            tk.Label(form_frame, text=campo + ":").grid(row=0,
                                                        column=i, sticky="w", pady=2)
            # La llave campo del entries crea un Entry dentro del form_frame con un ancho de 25 pixeles
            self.entries[campo] = tk.Entry(form_frame, width=25)
            # Utiliza grid para ubicarlo en la fila 0, columna j, deja un espacio de 2 pixeles en el eje Y y 5 pixeles en el eje X
            self.entries[campo].grid(row=0, column=j, pady=2, padx=5)

        # Botones

        # La variable button_frame crea un Frame/marco dentro del frame2
        button_frame = tk.Frame(frame2)
        # Empaqueta el button_frame dejando una separacion de 2 pixeles en ambos ejes
        button_frame.pack(pady=2, padx=2)

        tk.Button(  # Crea un boton
            # Dentro del button_frame, con el texto "AGREGAR", el fondo de color "#6CFF22", el color de la fuente en azul
            button_frame, text="AGREGAR", bg="#6CFF22", fg="blue",
            # La fuente en Arial, de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.agregar  # Ejecuta el metodo agregar
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 0 y con una separacion de 5 pixeles en el eje X
        ).grid(row=0, column=0, padx=5)
        tk.Button(  # Crea un boton
            # Dentro del button_frame, con el texto "ACTUALIZAR", el fondo de color #227EFF y la fuente de color naranja
            button_frame, text="ACTUALIZAR", bg="#227EFF", fg="orange",
            # La fuente es Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.actualizar  # Ejecita el metodo actualizar
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 1 y con una separacion de 5 pixeles en el eje X
        ).grid(row=0, column=1, padx=5)
        tk.Button(  # Crea un boton
            # Dentro del button_frame, con el texto "ELIMINAR", el fondo de color #F80000 y con la fuente de color negro
            button_frame, text="ELIMINAR", bg="#F80000", fg="black",
            # La fuente es Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.eliminar  # Ejecuta el metodo eliminar
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 2 y con una separacion de 5 pixeles en el eje X
        ).grid(row=0, column=2, padx=5)
        tk.Button(  # Crea un boton
            # Dentro del button_frame, con el texto "LIMPIAR", con el fondo de color #00F2FF y con la fuente de color verde
            button_frame, text="LIMPIAR", bg="#00F2FF", fg="green",
            # La fuente es Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.limpiar  # Ejecuta el metodo limpiar
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 3 y con una separacion de 5 pixeles en el eje X
        ).grid(row=0, column=3, padx=5)

        # Tabla de Clientes

        self.tree_gesCli = ttk.Treeview(  # La variable tree_gesCli crea un Treeview
            frame2,  # Dentro del frame2
            # Con las columnas "id", "Nombre", "Apellido", "Contacto"
            columns=("id", "Nombre", "Apellido", "Contacto"),
            show="headings"  # Muestra solo las columnas mencionadas
        )
        # col va a recorrer las columnas del tree_gesCli
        for col in self.tree_gesCli["columns"]:
            # El encabezado del tree_gesCli va a estar en la posicion col y con el texto de col
            self.tree_gesCli.heading(col, text=col)
            # La columna del tree_gesCli va a estar en la posicion col, con un ancho de 150 pixeles y posicionado en el centro
            self.tree_gesCli.column(col, width=150, anchor="center")
        # Empaqueta el tree_gesCli para que ocupe ambos ejes, se pueda expandir y con una separacion de 10 pixeles en ambos ejes
        self.tree_gesCli.pack(fill="both", expand=True, padx=10, pady=10)

        self.cargar_clientes()  # Llama al metodo cargar_clientes
        # Le bindea al TreeviewSelect del tree_gesCli el metodo seleccionar
        self.tree_gesCli.bind("<<TreeviewSelect>>", self.seleccionar)

    # Crea la funcion cargar_clientes con el atributo self
    def cargar_clientes(self):

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si no hay conexion
        if not conn:
            # Muestra un mensaje de erro con el titulo "Error" y con el mensaje "No se pudo conectar"
            messagebox.showerror("Error", "No se pudo conectar")
            return  # No devuelve nada

        cursor = conn.cursor()  # La variable cursor llama al metodo conectar de la variable conn

        # i va a recorrer los hijos del tree_cliente mediante el metodo get_children
        for i in self.tree_cliente.get_children():
            # Elimina el hijo del tree_cliente que este en la posicion i
            self.tree_cliente.delete(i)

        # i va a recorrer los hijos del tree_gesCli mediante el metodo get_children
        for i in self.tree_gesCli.get_children():
            # elimina el hijo que este en la posicion i del tree_gesCli
            self.tree_gesCli.delete(i)

        # Consulta tabla Clientes

        cursor.execute("""
            SELECT *
            FROM clientes
            ORDER BY nombre DESC
        """)

        # row va a recorrer todo lo que cursor obtenga mediante el metodo fetchall
        for row in cursor.fetchall():
            # Inserta en el tree_cliente desde el indice 1 hasta el final el valor que este en row
            self.tree_cliente.insert("", "end", values=row[1:])
            # Inserta en el tree_gescli desde el inicio hasat el final los valores que esten en row
            self.tree_gesCli.insert("", "end", values=row)

        conn.close()  # Cierra la conexion

    # Crea la funcion seleccionar con los atributos self y event
    def seleccionar(self, event):

        # La variable seleccion llama al metodo selection del tree_gesCli
        seleccion = self.tree_gesCli.selection()

        # Si hay seleccion
        if seleccion:
            # La variable valores va a obtener los valores de la seleccion mediante el metodo item del tree_gesCli
            valores = self.tree_gesCli.item(seleccion[0])["values"]
            self.limpiar()  # Llama a la funcion limpiar

            # En la llave "Nombre" de entries inserta al inicio los valores en la posicion 1
            self.entries["Nombre"].insert(0, valores[1])
            # En la llave "Apellido" de entries inserta al inicio los valores en la posicion 2
            self.entries["Apellido"].insert(0, valores[2])
            # En la llave "Contacto" de entries inserta al inicio los valores en la posicion 3
            self.entries["Contacto"].insert(0, valores[3])

    # Crea la funcion obtener_datos con el atributo self
    def obtener_datos(self):

        # Crea la variable nombre el cual obtiene los datos que esten dentro de la llave "Nombre" del entries
        nombre = self.entries["Nombre"].get().strip()
        # Crea la variable apellido el cual obtiene los datos que esten dentro de la llave "Apellido" del entries
        apellido = self.entries["Apellido"].get().strip()
        # Crea la variable contacto el cual obtiene los datos que esten dentro de la llave "Contacto" del entries
        contacto = self.entries["Contacto"].get().strip()
        return nombre, apellido, contacto  # Devuelve nombre, apellido y contacto

    # Crea la funcion limpiar con el atributo self
    def limpiar(self):

        # entry va a recorrer los valores del diccionario entries
        for entry in self.entries.values():

            # Si hay una instancia dentro de entry que sea de tipo Entry
            if isinstance(entry, tk.Entry):
                # Elimina el valor desde el principio hasta el final
                entry.delete(0, "end")

    # Crea la funcion agregar con el atributo self
    def agregar(self):

        datos = self.obtener_datos()  # La variable datos llama a la funcion obtener_datos

        # Si no hay datos
        if not datos:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encontraron datos"
            messagebox.showerror("Error", "No se encontraron datos")
            return  # No devuelve nada

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Consulta de la tabla clientes

            cursor.execute("""
                INSERT INTO clientes (nombre, apellido, contacto)
                VALUES (%s, %s, %s)
            """, (*datos,))  # Divide los datos que esten en la variable datos separados por coma

            conn.commit()  # Termina de ejecutar la consulta
            conn.close()  # Cierra la conexion
            self.cargar_clientes()  # Llama a la funcion cargar_clientes
            self.limpiar()  # Llama a la funcion limpiar
            # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Cliente agregado"
            messagebox.showinfo("Éxito", "Cliente agregado")

    # Crea la funcion actualizar con el atributo self
    def actualizar(self):

        # La variable seleccion llama al metodo selection del tree_gesCli
        seleccion = self.tree_gesCli.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona un cliente"
            messagebox.showwarning("Selecciona", "Selecciona un cliente")
            return  # No devuelve nada

        # La variable item va a ser la seleccion en la posicion 0 del tree_gesCli
        item = self.tree_gesCli.item(seleccion[0])
        # La variable cliente_id va a ser el valor del item en la posicion 0
        cliente_id = item["values"][0]
        datos = self.obtener_datos()  # La variable datos llama a la funcion obtener_datos

        # Si no hay datos
        if not datos:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encontraron datos"
            messagebox.showerror("Error", "No se encontraron datos")
            return  # No devuelve nada

        conn = conectar()  # La variable conn llama a la funcion conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Actualizar datos de la tabla clientes

            cursor.execute("""
                UPDATE clientes SET nombre=%s, apellido=%s, contacto=%s
                WHERE cliente_id=%s
            """, (*datos, cliente_id))  # Separa los datos de la variable datos con una coma y luego cuando se acaben los datos usa cliente_id

            conn.commit()  # Termina de ejecutar la actualizacion de los datos
            conn.close()  # Cierra la conexion
            self.cargar_clientes()  # Llama a la funcion cargar_clientes
            # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Cliente actualizado"
            messagebox.showinfo("Éxito", "Cliente actualizado")

    # Crea la funcion eliminar con el atributo self
    def eliminar(self):

        # La variable seleccion llama al metodo selection del tree_gesCli
        seleccion = self.tree_gesCli.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y muestra el mensaje "Selecciona un cliente"
            messagebox.showwarning("Selecciona", "Selecciona un cliente")
            return  # No devuelve nada

        # Muestra un mensaje de si o no con el titulo "Confirmar" y con el mensaje "¿Eliminar cliente?"
        if messagebox.askyesno("Confirmar", "¿Eliminar cliente?"):
            # La variable cliente_id llama a la funcion item para obtener el valor en la posicion 0 de la seleccion en la posicion 0
            cliente_id = self.tree_gesCli.item(seleccion[0])["values"][0]

            conn = conectar()  # La variable conn llama al metodo conectar

            # Si hay conexion
            if conn:
                cursor = conn.cursor()  # La variable cursror llama al metodo cursor de la variable conn

                # Eliminar datos de la tabla clientes

                cursor.execute(
                    "DELETE FROM clientes WHERE cliente_id=%s", (
                        cliente_id,))  # Utiliza la variable cliente_id como dato

                conn.commit()  # Termina de ejecutar el delete
                conn.close()  # Cierra la conexion
                self.cargar_clientes()  # Llama a la funcion cargar_clientes
