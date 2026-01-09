# modules/reportes.py

import tkinter as tk  # importa ykinter con el alias tk
from tkinter import ttk, messagebox  # Desde tkinter importa ttk y messagebox
# Desde la carpeta Database y el archivo db_connection importa el metodo conectar
from Database.db_connection import conectar

# Crea la clase VentasApp


class VentasApp:
    # Crea la funcion __init__ con los atributos self y root
    def __init__(self, root):
        self.root = root  # La variable root hace referencia al parametro root
        self.root.title("Ventas")  # El titulo del root es "Ventanas"

        # La variable notebook crea un Notebook dentro del root
        notebook = ttk.Notebook(root)
        # Empaqueta el notebook dejando un espacio de 10 pixeles en el eje Y y 20 pixeles en el eje X, rellena ambos ejes y permite expandirse
        notebook.pack(pady=10, padx=20, fill="both", expand=True)

        # Pestaña 1: Ventas Trabajos

        # La variable frame1 crea un Frame/Marco dentro del notebook
        frame1 = tk.Frame(notebook)
        # La variable notebook agrega una pestania con el frame1 con el texto "Ventas Trabajos"
        notebook.add(frame1, text="Ventas Trabajos")

        # Tabla de ventas

        self.tree_venta = ttk.Treeview(  # La variable tree_venta crea un Treeview
            frame1,  # Dentro del frame1
            # Con las columnas "Fecha", "Monto", "Celular", "Trabajo", "Cliente" y "Tipo de Pago"
            columns=("Fecha", "Monto", "Celular",
                     "Trabajo", "Cliente", "Tipo de Pago"),
            show="headings"  # Muestra solo las columnas mencionadas anteriormente
        )
        # Para col y texto que van a recorrer el zip
        for col, text in zip(
            self.tree_venta["columns"],  # De las columnas del tree_venta
            # Las cuales son "Fecha", "Monto", "Celular", "Trabajo", "Cliente" y "Tipo de Pago"
            ["Fecha", "Monto", "Celular", "Trabajo", "Cliente", "Tipo de Pago"]
        ):
            # En el encabezado del tree_venta en la posicion de col pone el texto que tenga text
            self.tree_venta.heading(col, text=text)
            # En la columna del tree_venta en la posicion de col tiene un ancho de 120 pixeles y ancla el texto al centro
            self.tree_venta.column(col, width=120, anchor="center")
        # Empaqueta el tree_venta rellenando ambos ejes, permite expandirse y deja un espacio de 10 pixeles en ambos ejes
        self.tree_venta.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña 2: Gestionar Trabajos

        # La variable frame2 crea un Frame/Marco dentro del notebook
        frame2 = tk.Frame(notebook)
        # Agrega una pestania del notebook con el frame2 y con el texto "Gestionar Trabajos"
        notebook.add(frame2, text="Gestionar Trabajos")
        # La variable form_frame crea un Frame/Marco dentro del frame2
        form_frame = tk.Frame(frame2)
        # Empaqueta el form_frame dejando un espacio de 20 pixeles en ambos ejes
        form_frame.pack(padx=20, pady=20)

        self.entries = {}  # Crea el diccionario entries

        # Labels y Entrys

        tk.Label(form_frame, text="Monto:").grid(  # Crea un Label/Etiqueta dentro del form_frame con el texto "Monto:"
            # Utiliza grid para ubicarlo en la fila 0, columna 0, lo posicion lo mas al west/oeste (izquierda) posible y deja un espacio de 2 pixeles en el eje Y
            row=0, column=0, sticky="w", pady=2)
        self.entries["Monto"] = tk.Entry(  # Crea la llave "Monto" en entries la cual contiene un Entry
            form_frame, width=25)  # Dentro del form_frame y con un ancho de 25 pixeles
        self.entries["Monto"].grid(  # La llave "Monto" del entries utiliza grid/malla
            # Para ubicarlo en la fila 0, columna 1, dejando un espacio de 2 pixeles en el eje Y y 5 pixeles en el eje X
            row=0, column=1, pady=2, padx=5)

        tk.Label(form_frame, text="Trabajo:").grid(  # Crea un Label/Etiqueta dentro del form_frame con el texto "Trabajo:"
            # Utiliza grid/malla para ubicarlo en la fila 0, columna 2, lo posiciona lo mas al west/oeste (izquierda) posible y deja un espacio de 2 pixeles en el eje Y
            row=0, column=2, sticky="w", pady=2)
        self.entries["Trabajo"] = ttk.Combobox(  # Crea la llave "Trabajo" en entries la cual contiene un Combobox
            # Dentro del form_frame, con un ancho de 75 pixeles y el estado en solo lectura
            form_frame, width=55, state="readonly")
        self.entries["Trabajo"].grid(  # La llave "Trabajo" del entries utiliza grid/malla
            # Para ubicarlo en la fila 0, columna 3, deja un espacio de 2 pixeles en el eje Y y 5 pixeles en el eje X
            row=0, column=3, pady=2, padx=5)

        tk.Label(form_frame, text="Tipo de Pago:").grid(  # Crea un Label/Etiqueta dentro del form_frame con el texto "Tipo de Pago:"
            # Utiliza grid para ubicarlo en la fila 0, columna 4, deja un espacio de 2 pixeles en el eje Y y 5 pixeles en el eje X
            row=0, column=4, pady=2, padx=5)

        # Botones

        # La variable button_frmae crea un Frame/Marco dentro del frame2
        button_frame = tk.Frame(frame2)
        # Empaqueta la variable button_frame dejando un espacio de 2 pixeles en ambos ejes
        button_frame.pack(pady=2, padx=2)
        # La variable tipo_pago crea un StringVar con el valor "Efectivo" para crear un grupo en los Radiobutton
        self.tipo_pago = tk.StringVar(value="Efectivo")

        tk.Button(  # Crea un boton dentro del button_frame con el texto "Agregar", el fondo de color #6CFF22 y la fuente de color azul
            button_frame, text="AGREGAR", bg="#6CFF22", fg="blue",
            # La fuente en Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.agregar_ventas  # Ejecuta la funcion agregar_ventas
            # Utiliza grid para ubicarlo en la fila 0, columna 0 y dejando un espacio de 5 pixeles en el eje X
        ).grid(row=0, column=0, padx=5)

        tk.Button(  # Crea un boton dentro del button_frame con el texto "ACTUALIZAR", el fondo de color #227EFF y la fuente de color naranja
            button_frame, text="ACTUALIZAR", bg="#227EFF", fg="orange",
            # La fuente en Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.actualizar_ventas  # Ejecuta la funcion actualizar_ventas
            # Utiliza grid para ubicarlo en la fila 0, columna 1 y dejando un espacio de 5 pixeles en el eje X
        ).grid(row=0, column=1, padx=5)

        tk.Button(  # Crea un boton dentro del button_frame con el texto "ELIMINAR", el fondo de color #F80000 y la fuente de color negro
            button_frame, text="ELIMINAR", bg="#F80000", fg="black",
            # Utiliza la fuente Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.eliminar_ventas  # Ejecuta la funcion eliminar_ventas
            # Utiliza grid para ubicarlo en la fila 0, columna 2 y dejando un espacio de 5 pixeles en el eje X
        ).grid(row=0, column=2, padx=5)

        tk.Button(  # Crea un boton dentro del button_frame con el texto "LIMPIAR", con el fondo de color #00F2FF y con la fuente de color verde
            button_frame, text="LIMPIAR", bg="#00F2FF", fg="green",
            # La fuente es Arial de tamanio 10 y con la propiedad bold/negrita
            font=("Arial", 10, "bold"),
            command=self.limpiar  # Ejecuta la funfion limpiar
            # Utiliza grid para ubicarlo en la fila 0, columna 3 y dejando un espacio de 5 pixeles en el eje X
        ).grid(row=0, column=3, padx=5)

        tk.Radiobutton(form_frame, text="Efectivo", variable=self.tipo_pago,  # Crea un Radiobutton dentro del form_frame con el texto "Efectivo", la variable que utiliza es tipo_pago y el valor es "Efectivo"
                       # Utiliza grid para ubicarlo en la fila 0, columna 5, deja un espacio de 2 pixeles en el eje Y y 5 pixeles en el eje X
                       value="Efectivo").grid(row=0, column=5, pady=2, padx=5)

        tk.Radiobutton(form_frame, text="Transferencia", variable=self.tipo_pago,  # Crea un Radiobutton dentro del form_frame con el texto "Transferencia", la variable que utiliza es tipo_pago y el valor es "Transferencia"
                       # Utiliza grid para ubicarlo en la fila 0, columna 6, deja un espacio de 2 pixeles en el eje Y y 5 pixeles en el eje X
                       value="Transferencia").grid(row=0, column=6, pady=2, padx=5)

        # Tabla de trabajos

        self.tree_gesVen = ttk.Treeview(  # La variable tree_gesVen crea un Treeview
            frame2,  # Dentro del frame2
            # Con las columnas "Id", "Fecha", "Monto", "Celular", "Trabajo", "Cliente" y "Tipo de Pago"
            columns=("Id", "Fecha", "Monto", "Celular",
                     "Trabajo", "Cliente", "Tipo de Pago"),
            show="headings"  # Muestra solo las columnas mencionadas anteriormente
        )
        # Para col y text que van a recorrer el zip
        for col, text in zip(
            self.tree_gesVen["columns"],  # De las columnas del tree_gesVen
            # Las cuales son "Id", "Fecha", "Monto", "Celular", "Trabajo", "Cliente" y "Tipo de Pago"
            ["Id", "Fecha", "Monto", "Celular",
                "Trabajo", "Cliente", "Tipo de Pago"]
        ):
            # Muestra en el encabezado del tree_gesVen en la posicion de col el texto que obtenga text
            self.tree_gesVen.heading(col, text=text)
            # En la columna del tree_gesVen la posicion de ocl tiene un ancho de 120 pixeles y ancla el texto al centro
            self.tree_gesVen.column(col, width=120, anchor="center")
        # Empaqueta el tree_gesVen rellenando ambos ejes, permitiendo expandir y dejando un espacio de 10 pixeles en ambos ejes
        self.tree_gesVen.pack(fill="both", expand=True, padx=10, pady=10)

        self.cargar_ventas()  # Llama a la funcion cargar_ventas
        self.cargar_trabajos()  # Llama a la funcion cargar_trabajos
        # Le bindea la funcion seleccionar_ventas al TreeviewSelect del tree_gesVen
        self.tree_gesVen.bind("<<TreeviewSelect>>", self.seleccionar_ventas)

    # Crea la funcion cargar_ventas
    def cargar_ventas(self):

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si no hay conexion
        if not conn:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se pudo conectar"
            messagebox.showerror("Error", "No se pudo conectar")
            return  # No devuelve nada

        cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

        # Ventas

        # Para i que va a recorrer los hijos del tree_venta
        for i in self.tree_venta.get_children():
            self.tree_venta.delete(i)  # Elimina el hijo que este en i

        # Para i que va a recorrer los hijos del tree_gesVen
        for i in self.tree_gesVen.get_children():
            # Elimina el hijo del tree_gesVen que este en i
            self.tree_gesVen.delete(i)

        # Consulta tabla ventas

        cursor.execute("""
            SELECT v.venta_id, v.fecha, v.monto, CONCAT(ma.nombre, " ", ce.modelo), t.descripcion, CONCAT(c.nombre, " ", c.apellido), v.tipo_pago
            FROM ventas v
            JOIN trabajos t ON t.trabajo_id = v.trabajo_id
            JOIN celulares ce ON ce.celular_id = t.celular_id
            JOIN marcas ma ON ma.marca_id = ce.marca_id
            JOIN clientes c ON c.cliente_id = v.cliente_id
            ORDER BY v.fecha DESC
        """)

        # Para row que reccorre todo lo que obtenga cursor
        for row in cursor.fetchall():
            # Inserta el en tree_venta los datos que obtenga row desde el indice 1 hasta el final
            self.tree_venta.insert("", "end", values=row[1:])
            # Inserta los valores de row desde el inicio hasta el final en el tree_gesVen
            self.tree_gesVen.insert("", "end", values=row)

        conn.close()  # Cierra la conexion

    # Crea la funcion cargar_trabajos con el atributo self
    def cargar_trabajos(self):

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Consulta tabla trabajos

            cursor.execute(
                """SELECT t.trabajo_id, t.cliente_id, CONCAT(ma.nombre, " ", ce.modelo, ", ", t.descripcion, ", ", c.nombre, " ", c.apellido)
                    FROM trabajos t
                    JOIN celulares ce ON ce.celular_id = t.celular_id
                    JOIN marcas ma ON ma.marca_id = ce.marca_id
                    JOIN clientes c ON c.cliente_id = t.cliente_id
                    ORDER BY trabajo_id DESC
                           """)

        self.map_trabajos = {}  # Crea el diccionario map_trabajos
        lista = []  # Crea el arreglo lista

        # Para trabajo_id, cliente_id y texto que van a recorrer todo lo que obtenga cursor
        for trabajo_id, cliente_id, texto in cursor.fetchall():
            self.map_trabajos[texto] = (  # En la llave texto del diccionario map_trabajos
                trabajo_id, cliente_id)  # Pone los valores de trabajo_id y cliente_id
            lista.append(texto)  # Agrega texto al arreglo lista

        # En los valores de la llave "Trabajo" del entries pone el valor de lista
        self.entries["Trabajo"]["values"] = lista
        conn.close()  # Cierra la conexion

    # Crea la funcion seleccionar_ventas con los atributos self y event
    def seleccionar_ventas(self, event):

        # La variable seleccion llama al metodo selection del tree_geesVen
        seleccion = self.tree_gesVen.selection()

        # Si hay seleccion
        if seleccion:
            # La variable valores guarda el valor de la seleccion que este en la posicion 0 utilizando el metodo item del tree_gesVen
            valores = self.tree_gesVen.item(seleccion[0])["values"]
            self.limpiar()  # Llama a la funcion limpiar

            # En la llave "Monto" de entries inserta al inicio el valor en la posicion 2 del arreglo valores
            self.entries["Monto"].insert(0, valores[2])

            # La variable texto_trabajo guarda un texto con la informacion de cada trabajo
            texto_trabajo = f"{valores[3]}, {valores[4]}, {valores[5]}"
            # En la llave "Trabajo" del entries pone la variable texto_trabajo
            self.entries["Trabajo"].set(texto_trabajo)

            # La variable texto_pago convierte el valor de la posicion 6 de la variable valores en capital para que devuelva "Efectivo" en vez de "efectivo"
            texto_pago = valores[6].capitalize()
            # Se establece el valor de la variable tipo_pago en lo que contenga texto_pago
            self.tipo_pago.set(texto_pago)

    # Crea la funcion obtener_datos con al tributo self
    def obtener_datos(self):
        # La variable monto obtiene su valor de la llave "Monto" del diccionario entries
        monto = self.entries["Monto"].get()
        # La variable trabajo obtiene su valor de la llave "Trabajo" del diccionario entries
        trabajo = self.entries["Trabajo"].get()
        # La variable pago obtiene su valor de la variable tipo_pago
        pago = self.tipo_pago.get()

        # Convertir texto → ID

        # La variable trabajo_id y cliente_id obtienen su valor de la llave trabajo del diccionario map_trabajos
        trabajo_id, cliente_id = self.map_trabajos.get(trabajo, (None, None))

        # Devuelve monto, trabajo_id, cliente_id y pago
        return monto, trabajo_id, cliente_id, pago

    # Crea la funcion limpiar del atributo self
    def limpiar(self):
        # Para entry que recorre los valores del entries
        for entry in self.entries.values():
            # Si hay una instancia dentro de entry que sea de tipo Entry
            if isinstance(entry, tk.Entry):
                # Elimina el valor que tenga desde el inicio hasta el final
                entry.delete(0, "end")
            # Si hay una instancia dentro de entry que sea de tipo Text
            if isinstance(entry, tk.Text):
                # Elimina desde el inicio hasta el final el valor que contenga
                entry.delete("1.0", "end")
            # Si hay una instancia dentro de entry que sea de tipo Combobox
            if isinstance(entry, ttk.Combobox):
                entry.set("")  # Establece el valor en "" (osea vacio)

    # Crea la funcion agregar_ventas con al tributo self
    def agregar_ventas(self):

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

            # Insertar datos en la tabla ventas

            cursor.execute("""
                INSERT INTO ventas (monto, trabajo_id, cliente_id, tipo_pago)
                VALUES (%s, %s, %s, %s)
            """, (*datos,))  # Separa los valores de la variable datos utilizando coma

            conn.commit()  # Termina de ejcutar el insert
            conn.close()  # Cierra la conexion
            self.cargar_ventas()  # Llama a la funcion cargar_ventas
            self.limpiar()  # Llama a la funcion limpiar
            # Muestra un mensaje de informacion con el texti "Exito" y con el mensaje "Venta agregada"
            messagebox.showinfo("Éxito", "Venta agregado")

    # Crea una funcion actualizar_ventas con el atributo self
    def actualizar_ventas(self):

        # La variable seleccion llama al metodo selection del tree_gesVen
        seleccion = self.tree_gesVen.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona una venta"
            messagebox.showwarning("Selecciona", "Selecciona una venta")
            return  # No devuelve nada

        # La variable item obtiene su valor de la seleccion en la posicion 0 mediante el metodo item del tree_gesVen
        item = self.tree_gesVen.item(seleccion[0])
        # La variable venta_id obtiene su valor de la posicion 0 de la variable item
        venta_id = item["values"][0]
        datos = self.obtener_datos()  # La variable datos llama a la funcion obtener_datos

        # Si no hay datos
        if not datos:
            # Muestra un mensaje de error con el titulo "Error" y con el mensaje "No se encuentran datos"
            messagebox.showerror("Error", "No se encontraron datos")
            return  # No devuelve nada

        conn = conectar()  # La variable conn llama al metodo conectar

        # Si hay conexion
        if conn:
            cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

            # Actualizar datos tabla ventas

            cursor.execute("""
                UPDATE ventas SET monto=%s, trabajo_id=%s, cliente_id=%s, tipo_pago=%s
                WHERE venta_id=%s
            """, (*datos, venta_id))  # Separa la variable datos y luego utiliza venta_id

            conn.commit()  # Termina de ejecutar el update
            conn.close()  # Cierra la conexion
            self.cargar_ventas()  # Llama a la funcino cargar_ventas
            # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Venta actualizada"
            messagebox.showinfo("Éxito", "Venta actualizada")

    # Crea la funcion eliminar_ventas con el atributo self
    def eliminar_ventas(self):

        # La variable seleccion llama al metodo selection del tree_gesVen
        seleccion = self.tree_gesVen.selection()

        # Si no hay seleccion
        if not seleccion:
            # Muestra un mensaje de advertencia con el titulo "Selecciona" y con el mensaje "Selecciona una venta"
            messagebox.showwarning("Selecciona", "Selecciona una venta")
            return  # No devuelve nada

        # Muestra un mensaje de si o no con el titulo "Confirmar" y con el mensaje "¿Eliminar venta?", en el caso de responder si
        if messagebox.askyesno("Confirmar", "¿Eliminar venta?"):
            # La variable venta_id obtiene el valor de la posicion 0 de la seleccion en la posicion 0 mediante el metodo item del tree_gesVen
            venta_id = self.tree_gesVen.item(seleccion[0])["values"][0]

            conn = conectar()  # La variable conn llama al metodo conectar

            # Si hay conexion
            if conn:
                cursor = conn.cursor()  # La variable cursor llama al metodo cursor de la variable conn

                # Eliminar datos de la tabla ventas

                cursor.execute(
                    "DELETE FROM ventas WHERE venta_id=%s", (
                        venta_id,))  # Utiliza venta_id como dato

                conn.commit()  # Termina de ejecutar el delete
                conn.close()  # Cierra la conexion
                self.cargar_ventas()  # Llama a la funcion cargar_ventas
