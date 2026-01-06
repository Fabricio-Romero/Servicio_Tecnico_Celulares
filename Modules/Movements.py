import tkinter as tk  # Importa tkinter con el alias tk
from tkinter import ttk, messagebox  # Desde tkinter importa ttk y messagebox
# Desde la carpeta Database y el archivo db_connection importa el metodo conectar
from Database.db_connection import conectar
# Desde la carpeta Modules y el archivo products importa la clase ProductosApp
from Modules.Products import ProductosApp

# Crea la clase MovimientosApp


class MovimientosApp:

    # Crea la funcion __init__ con los atributos self y root
    def __init__(self, root):
        self.root = root  # Crea la variable root que hace referencia al parametro root
        # El titulo del root es "Registro de Movimientos"
        self.root.title("Registro de Movimientos")

        # La variable frame_gesProd crea un frame dentro del root
        frame_gesProd = tk.Frame(root)
        # Empaqueta el frame_gesProd rellenando en el eje X
        frame_gesProd.pack(fill="x")
        # La variable frame crea un frame dentro del root
        frame = tk.Frame(root)
        # Empaqueta el frame dejando un espacio de 20 pixeles en el eje X
        frame.pack(padx=20)

        # Labels y Entrys

        # Crea un Label/Etiqueta dentro del frame con el texto "Producto:"
        # Utiliza grid para ubicarlo en la fila 0, columna 0 y lo posiciona lo mas al west/oeste (izquierda) posible
        tk.Label(frame, text="Producto:").grid(row=0, column=0, sticky="w")
        # Crea la variable producto_cb la cual crea un combobox dentro del frame con un ancho de 40 pixeles
        self.producto_cb = ttk.Combobox(frame, width=40)
        # Utiliza grid para ubicarlo en la fila 0, columna 1 y dejando un espacio de 5 pixeles en el eje X
        self.producto_cb.grid(row=0, column=1, padx=5)

        # Crea un Label/Etiqueta dentro del frame con el texto "Tipo:"
        # Utiliza grid para ubicarlo en la fila 1, columna 0, lo posiciona lo mas al west/oeste (izquierda) posible y deja un espacio de 5 pixeles en el eje Y
        tk.Label(frame, text="Tipo:").grid(row=1, column=0, sticky="w", pady=5)
        # Crea la variable tipo_var la cual crea un StringVar (un strin con un valor) y con el valor "salida"
        self.tipo_var = tk.StringVar(value="salida")

        # Crea un Label/Etiqueta dentro del frame con el texto "Cantidad:"
        tk.Label(frame, text="Cantidad:").grid(
            # Utiliza grid para ubicarlo en la fila 2, columna 0, lo posiciona lo mas al west/oeste (izquierda) posible y deja un espacio de 5 pixeles en el eje Y
            row=2, column=0, sticky="w", pady=5)
        # Crea la variable cantidad_entry la cual crea un Entry/Entrada dentro del frame con un ancho de 20 pixeles
        self.cantidad_entry = tk.Entry(frame, width=20)
        # Utiliza grid para ubicarlo en la fila 2, columna 1 y lo posiciona lo mas al west/oeste (izquierda) posible
        self.cantidad_entry.grid(row=2, column=1, sticky="w")

        # Botones

        tk.Button(  # Crea un boton dentro del frame_gesProd, con el texto "GESTIONAR PRODUCTOS", con el fondo de color #2196F3, la fuente de color blanco
            frame_gesProd, text="GESTIONAR PRODUCTOS", bg="#2196F3", fg="white",
            # La fuente en Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.abrir_productos  # Ejecuta la funcion abrir_productos
            # Lo empaqueta del lado derecho y deja un espacio de 10 pixeles en ambos ejes
        ).pack(side="right", padx=10, pady=10)

        tk.Button(  # Crea un boton dentro del frame con el texto "REGISTRAR" Con el fondo de color #FF5722 y con la fuente de color azul
            frame, text="REGISTRAR", bg="#FF5722", fg="blue",
            # La fuente es Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.registrar  # Ejecuta la funcion registrar
            # Utiliza grid para ubicarlo en la fila 3, columna 0 y ocupa 2 columnas
        ).grid(row=3, column=0, columnspan=2)

        ttk.Radiobutton(  # Crea un Radiobutton dentro del frame con el texto "Entrada", utiliza la variable tipo_var para guardar el valor "entrada" si es seleccionado
            frame, text="Entrada", variable=self.tipo_var, value="entrada"
            # Utiliza grid para ubicarlo en la fila 1, columna 1 y lo posiciona lo mas al west/oeste (izquierda) posible
        ).grid(row=1, column=1, sticky="w")

        ttk.Radiobutton(  # Crea un Radiobutton dentro del frame con el texto "Salida (Venta)", utiliza la variable tipo_var para guardar el valor "salida" si es seleccionado
            frame, text="Salida (Venta)", variable=self.tipo_var, value="salida"
            # Utiliza grid para ubicarlo en la fila 1, columna 1 y lo posiciona lo mas el east/este (derecha) posible
        ).grid(row=1, column=1, sticky="e")

        # Tabla de movimientos recientes

        self.tree = ttk.Treeview(  # La variable tree crea un Treeview
            root,  # Dentro del root
            # Con las columnas "Fecha", "Cantidad", "Tipo" y "Producto"
            columns=("Fecha", "Cantidad", "Tipo", "Producto"),
            show="headings"  # Muestra solo las columnas mencionadas
        )
        # Para col y text que van a obtener el numero y el texto del zip
        for col, text in zip(
            self.tree["columns"],  # De las columnas del tree
            # "Fecha", "Cantidad", "Tipo" y "Producto"
            ["Fecha", "Cantidad", "Tipo", "Producto"]
        ):
            # El encabezado del tree se ubica en la posicion de col y con el texto text
            self.tree.heading(col, text=text)
            # Las columnas del tree se ubica en la posicion col, con un ancho de 140 pixeles y anclado al centro
            self.tree.column(col, width=140, anchor="center")

        # Empaqueta el tree dejando un espacio de 10 pixeles en el eje Y y 20 pixeles en el eje X, rellenando ambos ejes y permitiendo expandirse
        self.tree.pack(pady=10, padx=20, fill="both", expand=True)

        self.cargar_productos()  # Llama a la funcion cargar_productos
        self.cargar_movimientos()  # Llama a la funcion cargar_movimientos

    # Crea la funcion cargar_productos con el atributo self
    def cargar_productos(self):

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            # La variable cursor hace referencia al metodo cursor de la variable conn
            cursor = conn.cursor()

            # Consulta tabla productos

            cursor.execute("SELECT producto_id, nombre FROM productos")

            # Crea un diccionario llamado productos la cual tiene como llave lo que este en la posicion 1 del arreglo row y el valor en la posicion 0 del row, para row que va a obtener todo lo que obtenga cursor
            productos = {row[1]: row[0] for row in cursor.fetchall()}
            # Los valores de la variable producto_cb obtiene una lista con las llaves de productos
            self.producto_cb["values"] = list(productos.keys())
            # la variable productos_dict hace referencia a productos
            self.productos_dict = productos
            conn.close()  # Cierra la conexion

    # Crea la funcion cargar_movimientos con el atributp self
    def cargar_movimientos(self):

        # para i que va a recorrer los hijos del tree
        for i in self.tree.get_children():
            self.tree.delete(i)  # Elimina el hijo que este en i

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Consulta tabla movimientos

            cursor.execute("""
                SELECT m.fecha, m.cantidad, m.tipo, p.nombre
                FROM movimientos_productos m
                JOIN productos p ON m.producto_id = p.producto_id
                ORDER BY m.fecha DESC LIMIT 20
            """)

            # Para row que va a recorrer lo que consiga cursor
            for row in cursor.fetchall():
                # La variable tipo tiene el valor "ENTRADA" si la posicion 3 del row es igual a "entrada" sino se establece el valor "SALIDA"
                tipo = "ENTRADA" if row[3] == "entrada" else "SALIDA"
                self.tree.insert(  # Inserta en el tree
                    "", 0,  # Desde el inicio y al inicio
                    # Los valores en la posicion 0, 1, 2, 3 de row
                    values=(row[0], row[1], row[2], row[3])
                )
            conn.close()  # Cierra la conexion

    # Crea la funcion nueva ventana con los atributos self, titulo, clase y size
    def nueva_ventana(self, titulo, clase, size):
        # La variable ventana crea un Toplevel del root (crea una ventana hijo del root)
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)  # El titulo de la ventana es el parametro titulo
        ventana.geometry(size)  # El tamanio de la ventana es el parametro size
        clase(ventana)  # Al parametro clase le pasa la variable ventana

    # Crea la funcion abrir_productos con el atributo self
    def abrir_productos(self):

        # Llama a la funcion nueva_ventana y le pasa los parametros "Productos", crea una funcion temporal llamada root para llamar a la clase ProductosApp y pasarle los parametros, root, es_admin como verdadero y luego termina de pasarle el tamanio a nueva_ventana
        self.nueva_ventana("Productos", lambda root: ProductosApp(
            root, es_admin=True), "850x500")

    # Crea la funcion registrar con el atributo self
    def registrar(self):
        # La variable producto_nombre obtiene la lista de producto_cb
        producto_nombre = self.producto_cb.get()
        tipo = self.tipo_var.get()  # La variable tipo obtiene el valor de tipo_var
        # La variable cantidad_str obtiene el string de cantidad_entry
        cantidad_str = self.cantidad_entry.get()

        # Si no esta todo producto_nombre y cantidad_str
        if not all([producto_nombre, cantidad_str]):
            messagebox.showwarning(
                # Muestra un mensaje de advertencia con el titulo "Faltan datos" y con el mensaje "Selecciona producto y cantidad"
                "Faltan datos", "Selecciona producto y cantidad")
            return  # No devuelve nada

        # Intenta
        try:
            # La variable cantidad transforma en int el string cantidad_str
            cantidad = int(cantidad_str)
            # Si la cantidad es menor o igual a 0
            if cantidad <= 0:
                raise ValueError  # Va directo a la excpecion

        # La excepcion
        except:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "Cantidad debe ser numero mayor a 0"
            messagebox.showerror("Error", "Cantidad debe ser número > 0")
            return  # No devuelve nada

        # La variable producto_id obtiene el producto_nombre del productos_dict
        producto_id = self.productos_dict.get(producto_nombre)

        # Si no hay producto_id
        if not producto_id:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encuentra el id"
            messagebox.showerror("Error", "No se encuentra el id")
            return  # No devuelve nada

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si no hay conexion
        if not conn:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se pudo conectar"
            messagebox.showerror("Error", "No se pudo conectar")
            return  # No devuelve nada

        cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

        # Verificar stock en salida
        if tipo == "salida":

            # Consulta tabla productos

            cursor.execute(
                "SELECT cantidad FROM productos WHERE producto_id = %s",
                (producto_id,)  # Utiliza la variable producto_id con una coma al final
            )

            # La variable stock obtiene lo que obtenga cursor en la posicion 0
            stock = cursor.fetchone()[0]

            # Si la cantidad es mayor al stock
            if cantidad > stock:
                # Muestra un mensaje de error con el titulo "Stock insuficiente" y con el mensaje "solo hay {cantidad de stock} unidades"
                messagebox.showerror(
                    "Stock insuficiente",
                    f"Solo hay {stock} unidades"
                )
                conn.close()  # Cierra la conexion
                return  # No devuelve nada

        # Inserta datos en la tabla movimientos_productos

        cursor.execute("""
            INSERT INTO movimientos_productos (cantidad, tipo, producto_id)
            VALUES (%s, %s, %s)
        """, (cantidad, tipo, producto_id))  # Utiliza cantidad, tipo y producto_id separados por coma

        # Actualizar datos tabla productos

        # La variable op tiene el valor "+" si la variable tipo == "esntrada" sino se establece en "-"
        op = "+" if tipo == "entrada" else "-"

        cursor.execute(
            f"UPDATE productos SET cantidad = cantidad {op} %s WHERE producto_id = %s",
            (cantidad, producto_id)
        )

        conn.commit()  # Termina de ejecutar los inserts y updates
        conn.close()  # Cierra la conexion

        # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Movimiento registrado: {el tipoe de movimiento en mayusculas} de {la cantidad} unidad/es"
        messagebox.showinfo(
            "Éxito",
            f"Movimiento registrado: {tipo.upper()} de {cantidad} unidad/es"
        )

        self.cargar_movimientos()  # Llama a la funcion cargar_movimientos
        # Elimina lo que este en cantidad_entry
        self.cantidad_entry.delete(0, "end")
