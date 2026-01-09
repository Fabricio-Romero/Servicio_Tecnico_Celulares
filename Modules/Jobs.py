# modules/Customers.py

# Importa tkinter como tk
import tkinter as tk
# Desde tkinter importa ttk y messagebox
from tkinter import ttk, messagebox
# Desde la carpeta Database y el archivo db_connection importa el metodo conectar
from Database.db_connection import conectar
# Desde la carpeta Modules importa el archivo Phones se importa la clase CelularesApp
from Modules.Phones import CelularesApp

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

        # Pestaña 1: Ver Trabajos

        # La variable frame1 crea un Frame/Marco dentro del notebook
        frame1 = tk.Frame(notebook)
        # La variable notebook agrega una pagina que va a contener el frame1 y con el texto "Ver Trabajos"
        notebook.add(frame1, text="Ver Trabajos")

        # Botones

        # La variable btn_frame crea un Frame/Marcp dentro del frame1
        btn_frame = tk.Frame(frame1)
        # Empaqueta la variable btn_frame dejando un espacio de 20 pixeles en ambos ejes
        btn_frame.pack(padx=20, pady=20)
        # La variable opcion crea un StringVar con el valor "Todos" para controlar la opcion que esta seleccionada en los Radiobuttons
        self.opcion = tk.StringVar(value="Todos")

        # Crea un Label/Etiqueta dentro del btn_frame con el texto "Filtrar por:", con la fuente en Arial, de tamanio 10 y con la propiedad bold/negrita y utiliza grid para ubicarlo en la fila 0, columna 0
        tk.Label(btn_frame, text="Filtrar Estado por:", font=(
            "Arial", 10, "bold")).grid(row=0, column=0, padx=15)

        # Crea un Radiobutton dentro del btn_frame, con el texto "Todos", utiliza la variable opcion para controlar el grupo de Radiobuttons, el valor de este Radiobutton es "Todos", ejecuta la funcion cargar_verTrabajos y luego utiliza grid para ubicarlo en la fila 0, columna 1
        tk.Radiobutton(btn_frame, text="Todos", variable=self.opcion,
                       value="Todos", command=self.cargar_verTrabajos).grid(row=0, column=1, padx=15)

        # Crea un Radiobutton dentro del btn_frame con el texto "Pendientes", utiliza la variable opcion para controlar el grupo de Radiobuttons, el valor de este Radiobutton es "Pendiente", ejecuta la funcion cargar_verTrabajos y luego utiliza grid para ubicarlo en la fila 0, columna 2
        tk.Radiobutton(btn_frame, text="Pendiente", variable=self.opcion, value="Pendiente", command=self.cargar_verTrabajos).grid(
            row=0, column=2, padx=15)

        # Crea un Radiobutton dentro del btn_frame con el texto "En proceso", utiliza la variable opcion para controlar el grupo de Radiobuttons, el valor de este Radiobutton es "En proceso", ejecuta la funcion cargar_verTrabajos y luego utiliza grid para ubicarlo en la fila 0, columna 3
        tk.Radiobutton(btn_frame, text="En proceso", variable=self.opcion, value="En proceso", command=self.cargar_verTrabajos).grid(
            row=0, column=3, padx=15)

        # Crea un Radiobutton dentro del btn_frame con el texto "Listo", utiliza la variable opcion para controlar el grupo de Radiobuttons, el valor de este Radiobutton es "Listo", ejecuta la funcion cargar_verTrabajos y luego utiliza grid para ubicarlo en la fila 0, columna 4
        tk.Radiobutton(btn_frame, text="Listo", variable=self.opcion,
                       value="Listo", command=self.cargar_verTrabajos).grid(row=0, column=4, padx=15)

        # Tabla

        self.tree_verTrabajos = ttk.Treeview(  # La variable tree_verTrabajos crea un Treeview
            frame1,  # Dentro del frame1
            columns=("Fecha", "Estado", "Falla",  # Con las columnas Fecha, Estado, Falla, IMEI, Celular y Cliente
                     "IMEI", "Celular", "Cliente"),
            show="headings"  # Muestra solo las columnas anteriormente mencionadas
        )
        # Para col que va a recorrer las columnas del tree_verTrabajos
        for col in self.tree_verTrabajos["columns"]:
            # El encabezado del tree_verTrabajos en la columna col se pone el texto col
            self.tree_verTrabajos.heading(col, text=col)
            # La columna del tree_verTrabajos en la columna col, tiene un ancho de 200 pixeles y se ancla al centro
            self.tree_verTrabajos.column(col, width=200, anchor="center")

        # Empaqueta el tree_verTrabajos rellenando ambos ejes, permite expandirse y deja un espacio de 10 pixeles en ambos ejes
        self.tree_verTrabajos.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña 2: Gestion de Trabajos

        # La variable frame2 Crea un frame dentro del notebook
        frame2 = tk.Frame(notebook)
        # La variable notebook agrega una pagina que va a contener el frame2 y el texto "Gestion de Trabajos"
        notebook.add(frame2, text="Gestion de Trabajos")
        # La variable form_frame crea un frame/marco dentro del frame2
        form_frame = tk.Frame(frame2)
        # Empaqueta el form_fame con una separacion de 20 pixeles en ambos ejes
        form_frame.pack(padx=20, pady=20)

        # Labels y Entries

        self.entries = {}  # Crea el diccionario entries
        # Crea el arreglo campos que guarda el texto y las llaves de los labels y entries
        campos = ["Estado", "Falla", "IMEI", "Celular", "Cliente"]

        # i y campo que van a recorrer la enumeracion del arreglo campos
        for i, campo in enumerate(campos):
            # i contiene numeros impares (donde van a ir los Labels)
            i += i + 1
            j = i + 1  # j tiene los numeros pares (donde van a ir los Entries)

            # Crea un Label/Etiqueta dentro del form_frame con el texto que contenga campo mas ":"
            tk.Label(form_frame, text=campo + ":").grid(row=0,
                                                        # Utiliza grid para ubicarlo en la fila 0, columna i, lo posiciona lo mas al west/oeste (izquierda) posible, deja un espacio de 2 pixeles en el eje Y
                                                        column=i, sticky="w", pady=2)

            # en "Falla" de campo
            if campo in ["Falla"]:
                # La llave campo del entries contiene un Text/Texto dentro del from_frame con un ancho de 25 pixeles y una altura de 3 caracteres
                self.entries[campo] = tk.Text(form_frame, width=25, height=3)
                self.entries[campo].grid(
                    # Utiliza grid para ubicarlo en la fila 0, columna j, deja un espacio de 2 pixeles en el eje Y y 5 pixeles en el eje X, ocupa 3 filas
                    row=0, column=j, pady=2, padx=5, rowspan=3)
            # Si no pasa eso, pero en "IMEI" de campo
            elif campo in ["IMEI"]:
                # La llave campo del entries crea un Entry dentro del form_frame con un ancho de 25 pixeles
                self.entries[campo] = tk.Entry(form_frame, width=25)
                # Utiliza grid para ubicarlo en la fila 0, columna j, deja un espacio de 2 pixeles en el eje Y y 5 pixeles en el eje X
                self.entries[campo].grid(row=0, column=j, pady=2, padx=5)
            # Si no
            else:
                # En la llave campo del entries crea un Combobox dentro del form_frame, con un ancho de 25 pixeles y el estado en solo lectura
                self.entries[campo] = ttk.Combobox(
                    form_frame, width=25, state="readonly")
                # Utiliza grid para ubicarlo en la fila 0, columna j, deja un espacio de 2 pixeles en el eje Y Y 5 pixeles en el eje X
                self.entries[campo].grid(row=0, column=j, pady=2, padx=5)

        # Los valores del entries "Estado" son "listo", "pendiente" y "en proceso"
        self.entries["Estado"]["values"] = ["listo", "pendiente", "en proceso"]
        # Establece el valor por defecto en "pendiente"
        self.entries["Estado"].set("pendiente")

        # Botones

        # La variable button_frame crea un frame/marco dentro del frame2
        button_frame = tk.Frame(frame2)
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
            frame2,  # Dentro del frame2
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

        # Pestaña 3: Gestionar Celulares y Marcas

        # Llama a la clase CelularesApp y le pasa el parametro notebook
        CelularesApp(notebook)

        self.cargar_verTrabajos()  # Llama a la funcion cargar_verTrabajos
        self.cargar_celulares()  # Llama a la funcion cargar_celulares
        self.cargar_clientes()  # Llama a la funcion cargar_clientes
        # Llama a la funcion cargar_trabajos
        self.cargar_trabajos()
        # Le bindea al TreeviewSelect del tree_trabajo la funcion seleccionar_trabajos
        self.tree_trabajo.bind("<<TreeviewSelect>>", self.seleccionar_trabajos)

    # Crea la funcion cargar_verTrabajos con el atributo self
    def cargar_verTrabajos(self):

        # Para i que va a recorrer los hijos del tree_verTrabajos
        for i in self.tree_verTrabajos.get_children():
            # Elimina le hijo que este en i
            self.tree_verTrabajos.delete(i)

        # La variable tipo obtiene su valor de la opcion que se seleccione en los Radiobutton y los pone en minusculas
        tipo = self.opcion.get().lower()

        # La variable conn llama al metodo conectar
        conn = conectar()

        # Si hay conexion
        if conn:
            # La variable cursor llama al metodo cursor de la variable conn
            cursor = conn.cursor()

            # Si la variable tipo es igual a "todos"
            if tipo == "todos":
                # Consulta tabla trabajos

                cursor.execute("""
                    SELECT t.trabajo_id, t.fecha, t.estado, t.descripcion, t.IMEI, CONCAT(ma.nombre, ' ', ce.modelo) AS celular, CONCAT(c.nombre, ' ', c.apellido) AS cliente
                    FROM trabajos t
                    JOIN celulares ce ON t.celular_id = ce.celular_id
                    JOIN marcas ma ON ce.marca_id = ma.marca_id
                    JOIN clientes c ON t.cliente_id = c.cliente_id
                    ORDER BY t.fecha DESC
                """)
            # Si no
            else:

                # Consulta tabla trabajos con where
                cursor.execute("""
                        SELECT t.trabajo_id, t.fecha, t.estado, t.descripcion, t.IMEI, CONCAT(ma.nombre, ' ', ce.modelo) AS celular, CONCAT(c.nombre, ' ', c.apellido) AS cliente
                        FROM trabajos t
                        JOIN celulares ce ON t.celular_id = ce.celular_id
                        JOIN marcas ma ON ce.marca_id = ma.marca_id
                        JOIN clientes c ON t.cliente_id = c.cliente_id
                        WHERE t.estado = %s
                        ORDER BY t.fecha DESC
                    """, (tipo,))  # Utiliza la variable tipo para comprobar en el where y luego utiliza coma

            # Para row que va a recorrer todo lo que obtenga cursor
            for row in cursor.fetchall():
                # Inserta desde el inicio hasta el final los valores de row en el tree_verTrabajos
                self.tree_verTrabajos.insert("", "end", values=row)

            conn.close()  # Cierra la conexion

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

    # # Crea la funcion cargar_trabajos_celulares_marcas con el atributo self

    def cargar_trabajos(self):

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

    # Crea la funcion limpiar con el atributo self
    def limpiar(self):

        # Para entry que va a recorrer los valores de entries
        for entry in self.entries.values():

            # Si hay una insancia dentro del entry que sea de tipo Entry
            if isinstance(entry, tk.Entry):
                # Elimina desde el caracter 0 hasta el final
                entry.delete(0, "end")
            # Si no ocurre eso, pero hay una instancia dentro del entry que sea de tipo Text
            if isinstance(entry, tk.Text):
                # Elimina desde el inicio hasta el final
                entry.delete("1.0", "end")
            # Si no ocurre eso, pero hay una instancia dentro del entry que sea de tipo Combobox
            if isinstance(entry, ttk.Combobox):
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
            # Llama a la funcion cargar_trabajos
            self.cargar_trabajos()
            self.limpiar()  # Llama a la funcion limpiar
            # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Trabajo agregado"
            messagebox.showinfo("Éxito", "Trabajo agregado")

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
            # Llama a la funcion cargar_trabajos
            self.cargar_trabajos()
            # Muestra un mensaje de informacion con el titulo "Exito" y con el mensaje "Trabajo actualizado"
            messagebox.showinfo("Éxito", "Trabajo actualizado")

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
                # Llama a la funcion cargar_trabajos
                self.cargar_trabajos()
