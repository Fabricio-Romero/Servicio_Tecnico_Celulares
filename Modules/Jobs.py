# modules/Customers.py

import tkinter as tk
from tkinter import ttk, messagebox
from Database.db_connection import conectar


class TrabajosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trabajos")

        notebook = ttk.Notebook(root)
        notebook.pack(pady=10, padx=20, fill="both", expand=True)

        # Pestaña 1: Trabajos
        frame1 = tk.Frame(notebook)
        notebook.add(frame1, text="Trabajos")
        form_frame = tk.Frame(frame1)
        form_frame.pack(padx=20, pady=20)

        self.entries = {}

        tk.Label(form_frame, text="Estado:").grid(
            row=0, column=2, sticky="w", pady=2)
        self.entries["Estado"] = ttk.Combobox(form_frame, width=25, values=[
                                              "listo", "pendiente", "en proceso"], state="readonly")
        self.entries["Estado"].grid(
            row=0, column=3, pady=2, padx=5)
        self.entries["Estado"].set("pendiente")

        tk.Label(form_frame, text="Falla:").grid(
            row=0, column=4, sticky="w", pady=2)
        self.entries["Falla"] = tk.Text(
            form_frame, width=25, height=3)
        self.entries["Falla"].grid(
            row=0, column=5, pady=2, padx=5, rowspan=3)

        tk.Label(form_frame, text="IMEI:").grid(
            row=0, column=6, sticky="w", pady=2)
        self.entries["IMEI"] = tk.Entry(form_frame, width=25)
        self.entries["IMEI"].grid(
            row=0, column=7, pady=2, padx=5)

        tk.Label(form_frame, text="Celular:").grid(
            row=0, column=8, sticky="w", pady=2)
        self.entries["Celular"] = ttk.Combobox(
            form_frame, width=25, state="readonly")
        self.entries["Celular"].grid(
            row=0, column=9, pady=2, padx=5)

        tk.Label(form_frame, text="Cliente:").grid(
            row=0, column=10, sticky="w", pady=2)
        self.entries["Cliente"] = ttk.Combobox(
            form_frame, width=25, state="readonly")
        self.entries["Cliente"].grid(
            row=0, column=11, pady=2, padx=5)

        # Botones

        button_frame = tk.Frame(frame1)
        button_frame.pack(pady=2, padx=2)

        tk.Button(
            button_frame, text="AGREGAR", bg="#6CFF22", fg="blue",
            font=("Arial", 10, "bold"),
            command=self.agregar
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            button_frame, text="ACTUALIZAR", bg="#227EFF", fg="orange",
            font=("Arial", 10, "bold"),
            command=self.actualizar
        ).grid(row=0, column=1, padx=5)
        tk.Button(
            button_frame, text="ELIMINAR", bg="#F80000", fg="black",
            font=("Arial", 10, "bold"),
            command=self.eliminar
        ).grid(row=0, column=2, padx=5)
        tk.Button(
            button_frame, text="LIMPIAR", bg="#00F2FF", fg="green",
            font=("Arial", 10, "bold"),
            command=self.limpiar
        ).grid(row=0, column=3, padx=5)

        self.tree_trabajo = ttk.Treeview(
            frame1,
            columns=("id", "Fecha", "Estado", "Falla",
                     "IMEI", "Celular", "Cliente"),
            show="headings"
        )
        for col, text in zip(
            self.tree_trabajo["columns"],
            ["id", "Fecha", "Estado", "Falla", "IMEI", "Celular", "Cliente"]
        ):
            self.tree_trabajo.heading(col, text=text)
            self.tree_trabajo.column(col, width=200, anchor="center")
            self.tree_trabajo.column("id", width=20, anchor="center")
        self.tree_trabajo.pack(fill="both", expand=True, padx=10, pady=10)

        # # Pestaña 2: Gestionar Celulares
        # frame2 = tk.Frame(notebook)
        # notebook.add(frame2, text="Gestionar Celulares")

        # # Tabla de Clientes

        # self.tree_gesCli = ttk.Treeview(
        #     frame2,
        #     columns=("id", "Nombre", "Apellido", "Contacto"),
        #     show="headings"
        # )
        # for col in self.tree_gesCli["columns"]:
        #     self.tree_gesCli.heading(col, text=col)
        #     self.tree_gesCli.column(col, width=150, anchor="center")
        # self.tree_gesCli.pack(fill="both", expand=True, padx=10, pady=10)

        self.cargar_celulares()
        self.cargar_clientes()
        self.cargar_trabajos()
        self.tree_trabajo.bind("<<TreeviewSelect>>", self.seleccionar)

    def cargar_celulares(self):
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT ce.celular_id, CONCAT(ma.nombre, ' ', ce.modelo)
                    FROM celulares ce
                    JOIN marcas ma ON ce.marca_id = ma.marca_id
                    ORDER BY ce.modelo DESC
                           """)

        self.map_celulares = {}  # ← Guardamos mapping texto -> ID
        lista = []

        for celular_id, texto in cursor.fetchall():
            self.map_celulares[texto] = celular_id  # "Samsung A52" → 17
            lista.append(texto)

        self.entries["Celular"]["values"] = lista
        conn.close()

    def cargar_clientes(self):
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT cliente_id, CONCAT(nombre, ' ', apellido)
                    FROM clientes                    
                    ORDER BY nombre DESC
                           """)

        self.map_clientes = {}  # ← Guardamos mapping texto -> ID
        lista = []

        for cliente_id, texto in cursor.fetchall():
            self.map_clientes[texto] = cliente_id
            lista.append(texto)

        self.entries["Cliente"]["values"] = lista
        conn.close()

    def cargar_trabajos(self):
        conn = conectar()
        if not conn:
            return

        cursor = conn.cursor()

        # Trabajos
        for i in self.tree_trabajo.get_children():
            self.tree_trabajo.delete(i)

        cursor.execute("""
            SELECT t.trabajo_id, t.fecha, t.estado, t.descripcion, t.IMEI, CONCAT(ma.nombre, ' ', ce.modelo) AS celular, CONCAT(c.nombre, ' ', c.apellido) AS cliente
            FROM trabajos t
            JOIN celulares ce ON t.celular_id = ce.celular_id
            JOIN marcas ma ON ce.marca_id = ma.marca_id
            JOIN clientes c ON t.cliente_id = c.cliente_id
            ORDER BY t.fecha DESC
        """)

        for row in cursor.fetchall():
            self.tree_trabajo.insert("", "end", values=row)

        # # Gestionar Clientes
        # for i in self.tree_gesCli.get_children():
        #     self.tree_gesCli.delete(i)

        # cursor.execute("""
        #     SELECT *
        #     FROM clientes
        #     ORDER BY nombre DESC
        # """)

        # for row in cursor.fetchall():
        #     self.tree_gesCli.insert("", "end", values=row)

        # conn.close()

    def agregar(self):
        datos = self.obtener_datos()
        if not datos:
            return

        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO trabajos (estado, descripcion, IMEI, celular_id, cliente_id)
                VALUES (%s, %s, %s, %s, %s)
            """, (*datos,))  # ← Usa *datos y coma final

            conn.commit()
            conn.close()
            self.cargar_trabajos()
            self.limpiar()
            messagebox.showinfo("Éxito", "Trabajo agregado")

    def actualizar(self):
        seleccion = self.tree_trabajo.selection()
        if not seleccion:
            messagebox.showwarning("Selecciona", "Selecciona un trabajo")
            return

        item = self.tree_trabajo.item(seleccion[0])
        trabajo_id = item["values"][0]
        datos = self.obtener_datos()
        if not datos:
            return

        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE trabajos SET estado=%s, descripcion=%s, IMEI=%s, celular_id=%s, cliente_id=%s
                WHERE trabajo_id=%s
            """, (*datos, trabajo_id))

            conn.commit()
            conn.close()
            self.cargar_trabajos()
            messagebox.showinfo("Éxito", "Trabajo actualizado")

    def eliminar(self):
        seleccion = self.tree_trabajo.selection()
        if not seleccion:
            messagebox.showwarning("Selecciona", "Selecciona un trabajo")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar trabajo?"):
            trabajo_id = self.tree_trabajo.item(seleccion[0])["values"][0]

            conn = conectar()
            if conn:
                cursor = conn.cursor()
                cursor.execute(
                    "DELETE FROM trabajos WHERE trabajo_id=%s", (
                        trabajo_id,)
                )
                conn.commit()
                conn.close()
                self.cargar_trabajos()

    def limpiar(self):
        for entry in self.entries.values():
            if isinstance(entry, tk.Entry):
                entry.delete(0, "end")
            elif isinstance(entry, tk.Text):
                entry.delete("1.0", "end")
            elif isinstance(entry, ttk.Combobox):
                entry.set("")

    def seleccionar(self, event):
        seleccion = self.tree_trabajo.selection()

        if seleccion:
            valores = self.tree_trabajo.item(seleccion[0])["values"]
            self.limpiar()

            self.entries["Estado"].set(valores[2])
            self.entries["Falla"].insert("1.0", valores[3])
            self.entries["IMEI"].insert(0, valores[4])
            self.entries["Celular"].set(valores[5])
            self.entries["Cliente"].set(valores[6])

    def obtener_datos(self):
        estado = self.entries["Estado"].get()
        falla = self.entries["Falla"].get("1.0", "end").strip()
        imei = self.entries["IMEI"].get().strip()
        celular = self.entries["Celular"].get()
        cliente = self.entries["Cliente"].get()

        # Convertir texto → ID
        celular_id = self.map_celulares.get(celular)
        cliente_id = self.map_clientes.get(cliente)

        return estado, falla, imei, celular_id, cliente_id
