# modules/Customers.py

import tkinter as tk
from tkinter import ttk, messagebox
from Database.db_connection import conectar


class ClientesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clientes")

        notebook = ttk.Notebook(root)
        notebook.pack(pady=10, padx=20, fill="both", expand=True)

        # Pestaña 1: Clientes
        frame1 = tk.Frame(notebook)
        notebook.add(frame1, text="Clientes")

        self.tree_cliente = ttk.Treeview(
            frame1,
            columns=("Nombre", "Apellido", "Contacto"),
            show="headings"
        )
        for col, text in zip(
            self.tree_cliente["columns"],
            ["Nombre", "Apellido", "Contacto"]
        ):
            self.tree_cliente.heading(col, text=text)
            self.tree_cliente.column(col, width=200, anchor="center")
        self.tree_cliente.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña 2: Gestionar Clientes
        frame2 = tk.Frame(notebook)
        notebook.add(frame2, text="Gestionar Clientes")
        form_frame = tk.Frame(frame2)
        form_frame.pack(padx=20, pady=15)

        self.entries = {}

        tk.Label(form_frame, text="Nombre:").grid(
            row=0, column=2, sticky="w", pady=2)
        self.entries["Nombre"] = tk.Entry(form_frame, width=25)
        self.entries["Nombre"].grid(
            row=0, column=3, pady=2, padx=5)

        tk.Label(form_frame, text="Apellido:").grid(
            row=0, column=4, sticky="w", pady=2)
        self.entries["Apellido"] = tk.Entry(form_frame, width=25)
        self.entries["Apellido"].grid(
            row=0, column=5, pady=2, padx=5)

        tk.Label(form_frame, text="Contacto:").grid(
            row=0, column=6, sticky="w", pady=2)
        self.entries["Contacto"] = tk.Entry(form_frame, width=25)
        self.entries["Contacto"].grid(
            row=0, column=7, pady=2, padx=5)

        # Botones

        button_frame = tk.Frame(frame2)
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

        # Tabla de Clientes

        self.tree_gesCli = ttk.Treeview(
            frame2,
            columns=("id", "Nombre", "Apellido", "Contacto"),
            show="headings"
        )
        for col in self.tree_gesCli["columns"]:
            self.tree_gesCli.heading(col, text=col)
            self.tree_gesCli.column(col, width=150, anchor="center")
        self.tree_gesCli.pack(fill="both", expand=True, padx=10, pady=10)

        self.cargar_clientes()
        self.tree_gesCli.bind("<<TreeviewSelect>>", self.seleccionar)

    def cargar_clientes(self):
        conn = conectar()
        if not conn:
            return

        cursor = conn.cursor()

        # Clientes
        for i in self.tree_cliente.get_children():
            self.tree_cliente.delete(i)

        cursor.execute("""
            SELECT nombre, apellido, contacto
            FROM clientes
            ORDER BY nombre DESC
        """)

        for row in cursor.fetchall():
            self.tree_cliente.insert("", "end", values=row)

        # Gestionar Clientes
        for i in self.tree_gesCli.get_children():
            self.tree_gesCli.delete(i)

        cursor.execute("""
            SELECT *
            FROM clientes
            ORDER BY nombre DESC
        """)

        for row in cursor.fetchall():
            self.tree_gesCli.insert("", "end", values=row)

        conn.close()

    def agregar(self):
        datos = self.obtener_datos()
        if not datos:
            return

        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO clientes (nombre, apellido, contacto)
                VALUES (%s, %s, %s)
            """, (*datos,))  # ← Usa *datos y coma final

            conn.commit()
            conn.close()
            self.cargar_clientes()
            self.limpiar()
            messagebox.showinfo("Éxito", "Cliente agregado")

    def actualizar(self):
        seleccion = self.tree_gesCli.selection()
        if not seleccion:
            messagebox.showwarning("Selecciona", "Selecciona un cliente")
            return

        item = self.tree_gesCli.item(seleccion[0])
        cliente_id = item["values"][0]
        datos = self.obtener_datos()
        if not datos:
            return

        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE clientes SET nombre=%s, apellido=%s, contacto=%s
                WHERE cliente_id=%s
            """, (*datos, cliente_id))

            conn.commit()
            conn.close()
            self.cargar_clientes()
            messagebox.showinfo("Éxito", "Cliente actualizado")

    def eliminar(self):
        seleccion = self.tree_gesCli.selection()
        if not seleccion:
            messagebox.showwarning("Selecciona", "Selecciona un cliente")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar cliente?"):
            cliente_id = self.tree_gesCli.item(seleccion[0])["values"][0]

            conn = conectar()
            if conn:
                cursor = conn.cursor()
                cursor.execute(
                    "DELETE FROM clientes WHERE cliente_id=%s", (
                        cliente_id,)
                )
                conn.commit()
                conn.close()
                self.cargar_clientes()

    def limpiar(self):
        for entry in self.entries.values():
            if isinstance(entry, tk.Entry):
                entry.delete(0, "end")
            elif isinstance(entry, ttk.Combobox):
                entry.set("")

    def seleccionar(self, event):
        seleccion = self.tree_gesCli.selection()

        if seleccion:
            valores = self.tree_gesCli.item(seleccion[0])["values"]
            self.limpiar()

            self.entries["Nombre"].insert(0, valores[1])
            self.entries["Apellido"].insert(0, valores[2])
            self.entries["Contacto"].insert(0, valores[3])

    def obtener_datos(self):
        nombre = self.entries["Nombre"].get().strip()
        apellido = self.entries["Apellido"].get().strip()
        contacto = self.entries["Contacto"].get().strip()
        return nombre, apellido, contacto
