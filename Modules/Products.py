import tkinter as tk  # Importa tkinter con el alias tk
from tkinter import ttk, messagebox  # Desde tkinter importa ttk y messagebox
# Desde la carpeta Database y el archivo db_connection importa el metodo conectar
from Database.db_connection import conectar
# Desde la carpeta Modules y el archivo Categories importa la clase CategoriasApp
from Modules.Categories import CategoriasApp

# Crea la clase ProductosApp


class ProductosApp:
    # Crea la funcion __init__ con el atributo self, root y es_admin como falso
    def __init__(self, root, es_admin=False):
        self.root = root  # La variable root hace referencia al parametro root
        self.es_admin = es_admin  # La variable es_admin hace referencia al parametro es_admin
        # El titulo del root es "Gestion de Productos"
        self.root.title("Gestión de Productos")

        # Frame superior: formulario

        # La variable frame_from crea un Frame/Marco dentro del root
        frame_form = tk.Frame(root)
        # Empaqueta el frame_form dejando un espacio de 10 pixeles en el eje Y, rellena el eje X y deja un espacio de 20 pixeles en el eje X
        frame_form.pack(pady=10, fill="x", padx=20)

        # Campos

        # El arreglo campos tiene los valores "Nombre", "Cantidad", "Precio", "Categoria" y "Proveedor"
        campos = ["Nombre", "Cantidad", "Precio", "Categoría", "Proveedor"]
        self.entries = {}  # Crea el diccionario entries

        # Labels y Entrys

        # Para i y campo que van a recorrer la enumeracion de la variable campos
        for i, campo in enumerate(campos):
            tk.Label(frame_form, text=campo + ":").grid(  # Crea un Label/Etiqueta dentro del frame_form, con el texto campo + ":"
                # Utiliza grid para ubicarlo en la fila i, columna 0, lo posiciona lo mas al west/oeste (izquierda) posible y deja un espacio de 2 pixeles en el eje Y
                row=i, column=0, sticky="w", pady=2
            )

            # Si el campo es "Categoria" o "Proveedor"
            if campo in ["Categoría", "Proveedor"]:
                self.entries[campo] = ttk.Combobox(  # El entries en campo crea un Combobox dentro del frame_form, con un ancho de 30 pixeles y el estado en solo lectura
                    frame_form, width=30, state="readonly")
            # Si no pasa eso
            else:
                # El entries en campo crea un Entry/Entrada dentro del frame_form con un ancho de 33 pixeles
                self.entries[campo] = tk.Entry(frame_form, width=33)

            # El entries en campo utiliza grid para ubicarlo en la fila i, columna 1, dejando un espacio de 2 pixeles en el eje Y y 5 pixeles en el eje X
            self.entries[campo].grid(row=i, column=1, pady=2, padx=5)

        # Botones

        tk.Button(frame_form, text="GESTIONAR CATEGORIAS",  # Crea un boton dentro del frame_form, con el texto "GESTIONAR CATEGORIAS", el fondo de color #BE2828, con la fuente de color blanco, ejecuta la funcion abrir_categorias
                  # Utiliza grid para ubicarlo en la fila 3, columna 2
                  bg="#BE2828", fg="white", command=self.abrir_categorias).grid(row=3, column=2)

        # Si no es_admin
        if not self.es_admin:
            tk.Button(btn_frame, text="Agregar", state="disabled",  # Crea un boton dentro del btn_frame con el texto "Agregar" y el estado deshabilitado con el fondo en gris
                      # Lo empaqueta del lado izquierdo dejando un espacio de 5 pixeles en el eje X
                      bg="gray").pack(side="left", padx=5)
            tk.Button(btn_frame, text="Actualizar", state="disabled",  # Crea un boton dentro del btn_frame con el texto "Actualizar" y el estado deshabilitado con el fondo en gris
                      # Lo empaqueta del lado izquierdo dejando un espacio de 5 pixeles en el eje X
                      bg="gray").pack(side="left", padx=5)
            tk.Button(btn_frame, text="Eliminar", state="disabled",  # Crea un boton dentro del btn_frame con el texto "Eliminar" y el estado deshabilitado con el fondo en gris
                      # Lo empaqueta del lado izquierdo dejando un espacio de 5 pixeles en el eje X
                      bg="gray").pack(side="left", padx=5)
        # Si no pasa eso
        else:
            # La variable btn_frame crea un Frame/Marco dentro del frame_form
            btn_frame = tk.Frame(frame_form)
            # Utiliza grid para ubicarlo en la fila 5, columna 0, ocupa 2 columnas y deja un espacio de 10 pixeles en el eje Y
            btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

            tk.Button(btn_frame, text="Agregar", bg="#4CAF50", fg="green",  # Crea un boton dentro del btn_frame, con el texto "Agregar", con el fondo de color #4CAF50, con la fuente de color verde y ejecuta la funcion agregar
                      # Lo empaqueta del lado izquierdo dejando un espacio de 5 pixeles en el eje X
                      command=self.agregar).pack(side="left", padx=5)
            tk.Button(btn_frame, text="Actualizar", bg="#2196F3", fg="blue",  # Crea un boton dentro del btn_frame, con el texto "Actualizar", con el fondo de color #2196F3, con la fuente de color azul y ejecuta la funcion actualizar
                      # Lo empaqueta del lado izquierdo dejando un espacio de 5 pixeles en el eje X
                      command=self.actualizar).pack(side="left", padx=5)
            tk.Button(btn_frame, text="Eliminar", bg="#F44336", fg="red",  # Crea un boton dentro del btn_frame, con el texto "Eliminar", con el fondo de color #F44336, con la fuente de color rojo y ejecuta la funcion eliminar
                      # Lo empaqueta del lado izquierdo dejando un espacio de 5 pixeles en el eje X
                      command=self.eliminar).pack(side="left", padx=5)
            tk.Button(btn_frame, text="Limpiar",  # Crea un boton dentro del btn_frame, con el texto "Limpiar", y ejecuta la funcion limpiar
                      # Lo empaqueta del lado izquierdo dejando un espacio de 5 pixeles en el eje X
                      command=self.limpiar).pack(side="left", padx=5)

        # Tabla

        self.tree = ttk.Treeview(  # El tree crea un Treeview (tabla)
            root,  # Dentro del root
            columns=("ID", "Nombre", "Cantidad",
                     # Con las columnas "ID", "Nombre", "Cantidad", "Precio", "Categoria" y "Proveedor"
                     "Precio", "Categoria", "Proveedor"),
            show="headings",  # Muestra solo las columnas mencionadas anteriormente
            height=15  # Con una altura de 15 pixeles
        )
        # Para col que va a recorrer las columnas del tree
        for col in self.tree["columns"]:
            # El encabezado del tree se ubica en la posicion col y el texto col
            self.tree.heading(col, text=col)
            # La columna "Nombre" del tree tiene un ancho de 200 pixeles y esta anclado al centro
            self.tree.column("Nombre", width=200, anchor="center")
            # Las columnas del tree col tienen un ancho de 120 pixeles y esta anclado al centro
            self.tree.column(col, width=120, anchor="center")

        # Empaqueta el tree dejando un espacio de 10 pixeles en el eje Y y 20 pixeles en el eje X, rellena ambos ejes y permite expandirse
        self.tree.pack(pady=10, padx=20, fill="both", expand=True)

        # Cargar datos

        self.cargar_categorias()  # Llama a la funcion cargar_categorias
        self.cargar_proveedores()  # Llama a la funcion cargar_proveedores
        self.cargar_productos()  # Llama a la funcion cargar_productos
        # Al TreeviewSelect del tree le bindea la funcion seleccionar
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar)

    # Crea la funcion cargar_categorias con el atributo self
    def cargar_categorias(self):

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Consulta tabla categorias

            cursor.execute("SELECT nombre FROM categorias")

            # El arreglo cats tiene la posicion 0 del row, para row que va a recorrer todo lo que obtenga cursor
            cats = [row[0] for row in cursor.fetchall()]
            # Los valores del entries categorias es la variable cats
            self.entries["Categoría"]["values"] = cats
            conn.close()  # Cierra la conexion

    # Crea la funcion cargar_proveedores con el atributo self
    def cargar_proveedores(self):

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Consulta tabla proveedores

            cursor.execute("SELECT comercio FROM proveedores")

            # El arreglo provs tiene la posicion 0 de row, para row que va a recorrer todo lo que obtenga cursor
            provs = [row[0] for row in cursor.fetchall()]
            # Los valores del entries Proveedor tiene el valor de la variable provs
            self.entries["Proveedor"]["values"] = provs
            conn.close()  # Cierra la conexion

    # Crea la funcion cargar_productos con el atributo self
    def cargar_productos(self):

        # para item que va a recorrer los hijos del tree
        for item in self.tree.get_children():
            self.tree.delete(item)  # Elimina el hijo que este en item

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Consutla tabla productos

            cursor.execute("""
                SELECT p.producto_id, p.nombre, p.cantidad, p.precio, c.nombre, pr.comercio
                FROM productos p
                LEFT JOIN categorias c ON p.categoria_id = c.categoria_id
                LEFT JOIN proveedores pr ON p.proveedor_id = pr.proveedor_id
            """)

            # Para row que va a recorrer todo lo que obtenga cursor
            for row in cursor.fetchall():
                # Inserta en el tree deslde el inicio hasta el final los valores de row
                self.tree.insert("", "end", values=row)

            conn.close()  # Cierra la conexion

    # Crea la funcion seleccionar con los atributos self y event
    def seleccionar(self, event):

        # La variable seleccion llama al metodo selection del tree
        seleccion = self.tree.selection()

        # SI hay seleccion
        if seleccion:

            # La variable valores obtiene los valores de la posicion 0 de la seleccion utilizando el metodo item del tree
            valores = self.tree.item(seleccion[0])["values"]
            self.limpiar()  # Llama a la funcion limpiar

            # En el entries "Nombre" inserta al inicio los valores en la posicion 1
            self.entries["Nombre"].insert(0, valores[1])
            # En el entries "Cantidad" inserta al inicio los valores en la posicion 2
            self.entries["Cantidad"].insert(0, valores[2])
            # En el entries "Precio" inserta al inicio los valores en la posicion 3
            self.entries["Precio"].insert(0, valores[3])
            # En el entries "Categoria" pone el valor que este en la posicion 4
            self.entries["Categoría"].set(valores[4])
            # En el entries "Proveedor" pone el valor que este en la posicion 5
            self.entries["Proveedor"].set(valores[5])

    # Crea la funcion nueva_ventana con los atributos self, titulo, clase y size
    def nueva_ventana(self, titulo, clase, size):
        # La variable ventana crea un toplevel del root (Crea una ventana hijo del root)
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)  # El titulo de la ventana es el parametro titulo
        ventana.geometry(size)  # El tamanio de la ventana es el parametro size
        clase(ventana)  # El parametro clase le pasa la variable ventana

    # Crea la funcion abrir_categorias con el atributo self
    def abrir_categorias(self):
        # Llama a la funcion nueva_ventana pasando los parametros "Gestionar Categorias", crea una funcion temporal llamada root para llamar a la clase CategoriasApp y pasarlo los parametros root y es_admin como verdadero, luego pasa el parametro "800x500"
        self.nueva_ventana("Gestionar Categorias", lambda root: CategoriasApp(
            root, es_admin=True), "800x500")

    # Crea la funcion obtener_datos del atributo self
    def obtener_datos(self):

        # La variable nombre obtiene su valor del entries "Nombre"
        nombre = self.entries["Nombre"].get().strip()
        # La precio nombre obtiene su valor del entries "Precio"
        precio = self.entries["Precio"].get().strip()
        # La cantidad nombre obtiene su valor del entries "Cantidad"
        cantidad = self.entries["Cantidad"].get().strip()
        # La variable cat obtiene su valor del entries "Categoria"
        cat = self.entries["Categoría"].get()
        # La variable prov obtiene su valor del entries "Proveedor"
        prov = self.entries["Proveedor"].get()

        # Si no estan todos los datos nombre, cantidad, precio, cat y prov
        if not all([nombre, cantidad, precio, cat, prov]):
            # Muestra un mensaje de advertencia con el titulo "Faltan datos" y con el mensaje "Completa todos los campos"
            messagebox.showwarning("Faltan datos", "Completa todos los campos")
            return None  # Devuelve None

        # Intenta
        try:
            # La variable precio pasa a float la variable precio
            precio = float(precio)
            # La variable cantidad pasa a int la variable cantidad
            cantidad = int(cantidad)
            # Si el precio es menor o igual a 0 o la cantidad es menor a 0
            if precio <= 0 or cantidad < 0:
                raise ValueError  # Pasa a la excepcion
        # Excepcion
        except:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "Precio > 0 y cantidad >= 0"
            messagebox.showerror("Error", "Precio > 0 y cantidad ≥ 0")
            return None  # Devuelve None

        # Devuelve nombre, cantidad, precio, cat y prov
        return (nombre, cantidad, precio, cat, prov)

    # Crea la funcion limpiar con el atributo self
    def limpiar(self):

        # Para entry que va a recorrer los valores de entries
        for entry in self.entries.values():
            # Si hay una instancia en el entry que sea de tipo Entry
            if isinstance(entry, tk.Entry):
                # Elimina lo que tenga ese entry desde el inicio hasta el final
                entry.delete(0, "end")
            # Si no pasa eso pero hay un instancia dentro del entry que se de tipo Combobox
            elif isinstance(entry, ttk.Combobox):
                entry.set("")  # Establece ese valor en "" (osea vacio)

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

            # Insert tabla productos

            cursor.execute("""
                INSERT INTO productos (nombre, cantidad, precio, categoria_id, proveedor_id)
                VALUES (%s, %s, %s,
                    (SELECT categoria_id FROM categorias WHERE nombre=%s),
                    (SELECT proveedor_id FROM proveedores WHERE comercio=%s))
            """, (*datos,))  # Separa los valores de la variable datos separandolos con coma

            conn.commit()  # Termina de ejecutar el insert
            conn.close()  # Cierra la conexion
            self.cargar_productos()  # Llama a la funcion cargar_productos
            self.limpiar()  # Llama a la funcion limpiar
            # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Producto agregado"
            messagebox.showinfo("Éxito", "Producto agregado")

    # Crea la funcion actualizar con el atributo self
    def actualizar(self):

        # La variable selection llama a la funcion selection del tree
        seleccion = self.tree.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona un producto"
            messagebox.showwarning("Selecciona", "Selecciona un producto")
            return  # No devuelve nada

        # La variable item obtiene el valor de la posicion 0 de seleccion utilizando el metodo item del tree
        item = self.tree.item(seleccion[0])
        # La variable product_id obtiene el valor de la posicion 0 de los valores de la variable item
        product_id = item["values"][0]
        datos = self.obtener_datos()  # La variable datos llama a la funcion obtener_datos

        # Si no hay datps
        if not datos:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encontraron datos"
            messagebox.showerror("Error", "No se encontraron datos")
            return  # No devuelve nada

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Actualizar datos de la tabla productos

            cursor.execute("""
                UPDATE productos SET nombre=%s, cantidad=%s, precio=%s,
                categoria_id=(SELECT categoria_id FROM categorias WHERE nombre=%s),
                proveedor_id=(SELECT proveedor_id FROM proveedores WHERE comercio=%s)
                WHERE producto_id=%s
            """, (*datos, product_id))  # Separa los datos de la variable datos y luego utiliza product _id

            conn.commit()  # Termina de ejecutar la actualizacion
            conn.close()  # Cierra la conexion
            self.cargar_productos()  # Llama a la funcion cargar_productos
            # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Producto actualizado"
            messagebox.showinfo("Éxito", "Producto actualizado")

    # Crea la variable eliminar con el atributo self
    def eliminar(self):

        # La variable selection llama al metodo selection del tree
        seleccion = self.tree.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona un producto"
            messagebox.showwarning("Selecciona", "Selecciona un producto")
            return  # No devuelve nada

        # Muestra un mensaje de si o no con el titulo "Confirmar" y con el mensaje "¿Eliminar producto?", en caso de responder si
        if messagebox.askyesno("Confirmar", "¿Eliminar producto?"):

            # La variable product_id obtiene su valor de la posicion 0 de los valores que se obtengan de la posicion 0 de la seleccion utilizando el metodo item del tree
            product_id = self.tree.item(seleccion[0])["values"][0]

            conn = conectar()  # La variable conn llama al metodo conectar

            # Si hay conexion
            if conn:
                cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

                # Eliminar datos de la tabla productos

                cursor.execute(
                    "DELETE FROM productos WHERE producto_id=%s", (product_id,)
                )

                conn.commit()  # Termina de ejecutar la eliminacion de datos
                conn.close()  # Cierra la conexion
                self.cargar_productos()  # Llama a la funcion cargar_productos
