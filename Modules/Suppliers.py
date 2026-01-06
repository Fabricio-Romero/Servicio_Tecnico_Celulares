# Importa tkinter con el alias tk
import tkinter as tk
# Desde tkinter importa ttk y messagebox
from tkinter import ttk, messagebox
# Desde la carpeta Database y el archivo db_connection importa el metodo conectar
from Database.db_connection import conectar

# Crea la clase ProveedoresApp


class ProveedoresApp:
    # Crea la funcion __init__ con los atributos self, root y es_admin inicialmente como false
    def __init__(self, root, es_admin=False):
        self.root = root  # Crea la variable root que hace referencia al parametro root
        # Crea la variable es_admin que hace referencia al parametro es_admin
        self.es_admin = es_admin
        self.root.title("Proveedores")  # El titulo del root es "Proveedores"

        # La variable frame crea un Frame/Marco dentro del root
        frame = tk.Frame(root)
        # Empaqueta la variable frame dejando un espacio de 15 pixeles en el eje Y y 20 pixeles en el eje X
        frame.pack(pady=15, padx=20)

        self.entries = {}  # Crea el diccionario entries

        # Labels y Entrys

        tk.Label(frame, text="Comercio:").grid(  # Crea un Label/Etiqueta dentro del frame con el texto "Comercio:"
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 0, lo posiciona lo mas al west/oeste (izquierda) posible y dejando un espacio de 2 pixeles en el eje Y
            row=0, column=0, sticky="w", pady=2)
        # La llave "Comercio" del entries crea un Entry/Entrada dentro del frame con un ancho de 25 pixeles
        self.entries["Comercio"] = tk.Entry(frame, width=25)
        self.entries["Comercio"].grid(  # Utiliza grid/malla para ubicarlo en la fila 0, columna 1, deja un espacio de 2 pixeles en el eje Y y 5 pixeles en el eje X
            row=0, column=1, pady=2, padx=5)

        tk.Label(frame, text="Nombre:").grid(  # Crea un Lable/Etiqueta dentro del frame con el texto "Nombre:"
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 2, lo posiciona lo mas al west/oeste (izquierda) posible y dejando un espacio de 2 pixeles en el eje Y
            row=0, column=2, sticky="w", pady=2)
        # La llave "Nombre" del entries crea un Entry/Entrada dentro del frame con un ancho de 25 pixeles
        self.entries["Nombre"] = tk.Entry(frame, width=25)
        self.entries["Nombre"].grid(  # Utiliza grid/malla para ubicarlo en la fila 0, columna 3, deja un espacio de 2 pixeles en el eje Y y 5 pixeles en el eje X
            row=0, column=3, pady=2, padx=5)

        tk.Label(frame, text="Apellido:").grid(  # Crea un Label/Etiqueta dentrp del frame con el texto "Apellido:"
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 4, lo posiciona lo mas al west/oeste (izquierda) posible y dejando un espacio de 2 pixeles en el eje Y
            row=0, column=4, sticky="w", pady=2)
        # La llave "Apellido" crea un Entry/Entrada dentro del frame con un ancho de 25 pixeles
        self.entries["Apellido"] = tk.Entry(frame, width=25)
        self.entries["Apellido"].grid(  # Utiliza grid/malla para ubicarlo en la fila 0, columna 5, deja un espacio de 2 pixeles en el eje Y y 5 pixeles en el eje X
            row=0, column=5, pady=2, padx=5)

        tk.Label(frame, text="Teléfono:").grid(  # Crea un Label/Etiqueta dentro del frame con el texto "Telefono:"
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 6, lo posiciona lo mas al west/oeste (izquierda) posible y dejando un espacio de 2 pixeles en el eje Y
            row=0, column=6, sticky="w", pady=2)
        # La llave "Telefono" Crea un Entry dentro del frame con un ancho de 25 pixeles
        self.entries["Telefono"] = tk.Entry(frame, width=25)
        self.entries["Telefono"].grid(  # Utiliza grid/malla para ubicarlo en la fila 0, columna 7, dejando un espacio de 2 pixeles en el eje Y y 5 pixeles en el eje X
            row=0, column=7, pady=2, padx=5)

        # Botones

        # La variable button_frame crea un Frame/Marco dentro del root
        button_frame = tk.Frame(root)
        # Empaqueta la variable button_frame dejando un espacio de 2 pixeles en ambos ejes
        button_frame.pack(pady=2, padx=2)

        tk.Button(  # Crea un boton
            # Dentro del button_frame con el texto "AGREGAR", el fondo de color # 6CFF22 y la fuente de color azul
            button_frame, text="AGREGAR", bg="#6CFF22", fg="blue",
            # La fuente en "Arial" de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.agregar  # Ejecuta la funcion agregar
            # Utiliza grid para ubicarlo en la fila 0, columna 0 y dejando un espacio de 5 pixeles en el eje X
        ).grid(row=0, column=0, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del button_frame con el texto "ACTUALIZAR", el fondo de color #227EFF y la fuente de color naranja
            button_frame, text="ACTUALIZAR", bg="#227EFF", fg="orange",
            # La fuente es "Arial", de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.actualizar  # Ejecuta la funcion actualizat
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 1 y dejando un espacio de 5 pixeles en el eje X
        ).grid(row=0, column=1, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del button_frame con el texto "ELIMINAR", el fondo de color #F80000 y con la fuente de color negro
            button_frame, text="ELIMINAR", bg="#F80000", fg="black",
            # La fuente de color "Arial" de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.eliminar  # Ejecuta la funcion eliminar
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 2 y dejando un espacio de 5 pixeles en el eje X
        ).grid(row=0, column=2, padx=5)

        tk.Button(  # Crea un boton
            # Dentro del button_frame con el texto "LIMPIAR", el fondo de color #00F2FF y la fuente de color verde
            button_frame, text="LIMPIAR", bg="#00F2FF", fg="green",
            # La fuente en "Arial" de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.limpiar  # Ejecuta la funcion limpiar
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 3 y deja un espacio de 5 pixeles en el eje X
        ).grid(row=0, column=3, padx=5)

        # Tabla de proveedores

        self.tree = ttk.Treeview(  # La variable tree crea un Treeview
            root,  # Dentro del root
            columns=("id", "comercio", "nombre",  # Con las columnas "id", "comercio", "nombre", "apellido" y "telefono"
                     "apellido", "telefono"),
            show="headings",  # Muestra solo las columnas mencionadas anteriormente
            height=15  # La altura es de 15 pixeles
        )
        # Para col que va a recorrer las columnas del tree
        for col in self.tree["columns"]:
            # El encabezado del tree va a estar en la posicion col y con el texto col
            self.tree.heading(col, text=col)
            # Las columnas del tree en la posicion col va a tener un ancho de 125 pixeles y va a estar anclada al centro
            self.tree.column(col, width=125, anchor="center")

        # Empaqueta el tree dejando un espacio de 10 pixeles en el eje Y y con 20 pixeles en el eje X, rellena ambos ejes y permite expandirse
        self.tree.pack(pady=10, padx=20, fill="both", expand=True)

        self.cargar_proveedores()  # Llama a la funcion cargar_proveedores
        # Le bindea la funcion seleccionar al TreeviewSelect del tree
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar)

    # Crea la funcion cargar_proveedores con el atributo self
    def cargar_proveedores(self):

        # Para item que va a recorrer los hijos del tree
        for item in self.tree.get_children():
            # Elimina el hijo que este en item
            self.tree.delete(item)

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Consulta tabla proveedores

            cursor.execute("""
                SELECT *
                FROM proveedores
            """)

            # Para row que va a recorrer todo lo que obtenga cursor
            for row in cursor.fetchall():
                # Inserta en el tree desde el inicio al final los valores de row
                self.tree.insert("", "end", values=row)

            conn.close()  # Cierra la conexion

    # Crea la funcion seleccionar con los atributos self y event
    def seleccionar(self, event):

        # La variable seleccion llama al metodo selection del tree
        seleccion = self.tree.selection()

        # Si hay seleccion
        if seleccion:
            # La variable valores  obtiene su valor de los valores de la seleccion en la posicion 0 utilizando el metodo item del tree
            valores = self.tree.item(seleccion[0])["values"]
            self.limpiar()  # Llama a la funcion limpiar

            # En la llave "Comercio" del entries inserta al inicio el valor en la posicion 1 del arreglo valores
            self.entries["Comercio"].insert(0, valores[1])
            # En la llave "Nombre" del entries inserta al inicio el valor en la posicion 2 del arreglo valores
            self.entries["Nombre"].insert(0, valores[2])
            # En la llave "Apellido" del entries inserta al inicio el valor en la posicion 3 del arreglo valores
            self.entries["Apellido"].insert(0, valores[3])
            # En la llave "Telefono" del entries inserta al inicio el valor en la posicion 4 del arreglo valores
            self.entries["Telefono"].insert(0, valores[4])

    # Crea la funcion obtener_datos con el atributo self
    def obtener_datos(self):

        # La variable comercio obtiene su valor de la llave "Comercio" del entries
        comercio = self.entries["Comercio"].get().strip()
        # La variable nombre obtiene su valor de la llave "Nombre" del entries
        nombre = self.entries["Nombre"].get().strip()
        # La variable apellido obtiene su valor de la llave "Apellido" del entries
        apellido = self.entries["Apellido"].get().strip()
        # La variable telefono obtiene su valor de la llave "Telefono" del entries
        telefono = self.entries["Telefono"].get().strip()

        # Devuelve las variables comercio, nombre, apellido y telefono
        return comercio, nombre, apellido, telefono

    # Crea la funcion limpiar con el atributo self
    def limpiar(self):

        # Para entry que recorre los valores de entries
        for entry in self.entries.values():
            # Si hay una instancia dentro de entry que sea de tipo Entry
            if isinstance(entry, tk.Entry):
                # Elimina su valor desde el inicio al final
                entry.delete(0, "end")
            # Si no pasa eso pero hay una instancia dentro de entry que sea de tipo Combobox
            elif isinstance(entry, ttk.Combobox):
                entry.set("")  # Establece su valor en "" (osea vacio)

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

            # Insertar datos en la tabla proveedores

            cursor.execute("""
                INSERT INTO proveedores (comercio, nombre, apellido, telefono)
                VALUES (%s, %s, %s, %s)
            """, (*datos,))  # Separa los valores de la variable datos utilizando coma

            conn.commit()  # Termina de ejecutar el insert
            conn.close()  # Cierra la conexion
            self.cargar_proveedores()  # Llama a la funcion cargar_proveedores
            self.limpiar()  # Llama a la funcion limpiar
            # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Proveedor agregado"
            messagebox.showinfo("Éxito", "Proveedor agregado")

    # Crea la funcion actualizar con el atributo self
    def actualizar(self):

        # La variable seleccion llama al metodo selection del tree
        seleccion = self.tree.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona un proveedor"
            messagebox.showwarning("Selecciona", "Selecciona un proveedor")
            return  # No devuelve nada

        # La variable item obtiene su valor de la posicion 0 de la seleccion mediante el metodo item del tree
        item = self.tree.item(seleccion[0])
        # La variable proveedor_id obtiene su valor de la posicion 0 de los valores de itm
        proveedor_id = item["values"][0]
        datos = self.obtener_datos()  # La variable datos llama a la funcino obtener_datos

        # Si no hay datos
        if not datos:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encontraron datos"
            messagebox.showerror("Error", "No se encontraron datos")
            return  # No devuelve nada

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursro de la variable conn

            # Actualizar datos tabla proveedores

            cursor.execute("""
                UPDATE proveedores SET comercio=%s, nombre=%s, apellido=%s, telefono=%s
                WHERE proveedor_id=%s
            """, (*datos, proveedor_id))  # Separa la variable datos y luego utiliza proveedor_id

            conn.commit()  # Termina de ejecutar el update
            conn.close()  # Cierra la conexion
            self.cargar_proveedores()  # Llama a la funcion cargar_proveedores
            # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Proveedor actualizado"
            messagebox.showinfo("Éxito", "Proveedor actualizado")

    # Crea la funcion eliminar con el atributo self
    def eliminar(self):

        # La variable seleccion llama al metodo selection del tree
        seleccion = self.tree.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona un proveedor"
            messagebox.showwarning("Selecciona", "Selecciona un proveedor")
            return  # No devuelve nada

        # Muestra un mensaje de si o no con el titulo "Confirmar" y con el mensaje "¿Eliminar proveedor?", en caso de responder si
        if messagebox.askyesno("Confirmar", "¿Eliminar proveedor?"):

            # La variable proveedor_id obtiene su valor de la posicion 0 de los valores de la seleccion en la posicion 0 mediante el metodo item del tree
            proveedor_id = self.tree.item(seleccion[0])["values"][0]

            conn = conectar()  # La variable conn llama al metodo conectar

            # Si hay conexion
            if conn:
                cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

                # Eliminar datos de la tabla proveedores

                cursor.execute(
                    "DELETE FROM proveedores WHERE proveedor_id=%s", (
                        proveedor_id,)  # Utiliza la variable proveedor_id
                )

                conn.commit()  # Termina de ejecutar el delete
                conn.close()  # Cierra la conexion
                self.cargar_proveedores()  # Llama a la funcion cargar_proveedores
