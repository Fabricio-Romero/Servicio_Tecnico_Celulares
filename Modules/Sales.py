# modules/reportes.py

import tkinter as tk
from tkinter import ttk, messagebox
from Database.db_connection import conectar


class VentasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventas")

        notebook = ttk.Notebook(root)
        notebook.pack(pady=10, padx=20, fill="both", expand=True)

        # Pestaña 1: Ventas Trabajos
        frame1 = tk.Frame(notebook)
        notebook.add(frame1, text="Ventas Trabajos")

        self.tree_venta = ttk.Treeview(
            frame1,
            columns=("Fecha", "Monto", "Celular", "Trabajo", "Cliente"),
            show="headings"
        )
        for col, text in zip(
            self.tree_venta["columns"],
            ["Fecha", "Monto", "Celular", "Trabajo", "Cliente"]
        ):
            self.tree_venta.heading(col, text=text)
            self.tree_venta.column(col, width=120, anchor="center")
        self.tree_venta.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña 2: Gestionar Trabajos
        frame2 = tk.Frame(notebook)
        notebook.add(frame2, text="Gestionar Trabajos")
        form_frame = tk.Frame(frame2)
        form_frame.pack(padx=20, pady=20)

        self.entries = {}

        tk.Label(form_frame, text="Monto:").grid(
            row=0, column=0, sticky="w", pady=2)
        self.entries["Monto"] = tk.Entry(
            form_frame, width=25)
        self.entries["Monto"].grid(
            row=0, column=1, pady=2, padx=5)

        tk.Label(form_frame, text="Trabajo:").grid(
            row=0, column=2, sticky="w", pady=2)
        self.entries["Trabajo"] = ttk.Combobox(
            form_frame, width=75, state="readonly")
        self.entries["Trabajo"].grid(
            row=0, column=3, pady=2, padx=5)

        # Botones

        button_frame = tk.Frame(frame2)
        button_frame.pack(pady=2, padx=2)

        tk.Button(
            button_frame, text="AGREGAR", bg="#6CFF22", fg="blue",
            font=("Arial", 10, "bold"),
            command=self.agregar_ventas
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            button_frame, text="ACTUALIZAR", bg="#227EFF", fg="orange",
            font=("Arial", 10, "bold"),
            command=self.actualizar_ventas
        ).grid(row=0, column=1, padx=5)
        tk.Button(
            button_frame, text="ELIMINAR", bg="#F80000", fg="black",
            font=("Arial", 10, "bold"),
            command=self.eliminar_ventas
        ).grid(row=0, column=2, padx=5)
        tk.Button(
            button_frame, text="LIMPIAR", bg="#00F2FF", fg="green",
            font=("Arial", 10, "bold"),
            command=self.limpiar
        ).grid(row=0, column=3, padx=5)

        self.tree_gesVen = ttk.Treeview(
            frame2,
            columns=("Id", "Fecha", "Monto", "Celular", "Trabajo", "Cliente"),
            show="headings"
        )
        for col, text in zip(
            self.tree_gesVen["columns"],
            ["Id", "Fecha", "Monto", "Celular", "Trabajo", "Cliente"]
        ):
            self.tree_gesVen.heading(col, text=text)
            self.tree_gesVen.column(col, width=120, anchor="center")
        self.tree_gesVen.pack(fill="both", expand=True, padx=10, pady=10)

        self.cargar_ventas()
        self.cargar_trabajos()
        self.tree_gesVen.bind("<<TreeviewSelect>>", self.seleccionar_ventas)

    def cargar_ventas(self):
        conn = conectar()
        if not conn:
            return

        cursor = conn.cursor()

        # Ventas
        for i in self.tree_venta.get_children():
            self.tree_venta.delete(i)

        cursor.execute("""
            SELECT v.fecha, v.monto, CONCAT(ma.nombre, " ", ce.modelo), t.descripcion, CONCAT(c.nombre, " ", c.apellido)
            FROM ventas v
            JOIN trabajos t ON t.trabajo_id = v.trabajo_id
            JOIN celulares ce ON ce.celular_id = t.celular_id
            JOIN marcas ma ON ma.marca_id = ce.marca_id
            JOIN clientes c ON c.cliente_id = v.cliente_id
            ORDER BY v.fecha DESC
        """)

        for row in cursor.fetchall():
            self.tree_venta.insert("", "end", values=row)

        # Gestionar Ventas

        for i in self.tree_gesVen.get_children():
            self.tree_gesVen.delete(i)

        cursor.execute("""
            SELECT v.venta_id, v.fecha, v.monto, CONCAT(ma.nombre, " ", ce.modelo), t.descripcion, CONCAT(c.nombre, " ", c.apellido)
            FROM ventas v
            JOIN trabajos t ON t.trabajo_id = v.trabajo_id
            JOIN celulares ce ON ce.celular_id = t.celular_id
            JOIN marcas ma ON ma.marca_id = ce.marca_id
            JOIN clientes c ON c.cliente_id = v.cliente_id
            ORDER BY v.fecha DESC
        """)

        for row in cursor.fetchall():
            self.tree_gesVen.insert("", "end", values=row)

        conn.close()

    def cargar_trabajos(self):
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute(
                """SELECT t.trabajo_id, t.cliente_id, CONCAT(ma.nombre, " ", ce.modelo, ", ", t.descripcion, ", ", c.nombre, " ", c.apellido)
                    FROM trabajos t
                    JOIN celulares ce ON ce.celular_id = t.celular_id
                    JOIN marcas ma ON ma.marca_id = ce.marca_id
                    JOIN clientes c ON c.cliente_id = t.cliente_id
                    ORDER BY trabajo_id DESC
                           """)

        self.map_trabajos = {}  # ← Guardamos mapping texto -> ID
        lista = []

        for trabajo_id, cliente_id, texto in cursor.fetchall():
            self.map_trabajos[texto] = (
                trabajo_id, cliente_id)  # "Samsung A52" → 17
            lista.append(texto)

        self.entries["Trabajo"]["values"] = lista
        conn.close()

    def seleccionar_ventas(self, event):
        seleccion = self.tree_gesVen.selection()

        if seleccion:
            valores = self.tree_gesVen.item(seleccion[0])["values"]
            self.limpiar()

            self.entries["Monto"].insert(0, valores[2])

            texto_trabajo = f"{valores[3]}, {valores[4]}, {valores[5]}"
            self.entries["Trabajo"].set(texto_trabajo)

    def limpiar(self):
        for entry in self.entries.values():
            if isinstance(entry, tk.Entry):
                entry.delete(0, "end")
            elif isinstance(entry, tk.Text):
                entry.delete("1.0", "end")
            elif isinstance(entry, ttk.Combobox):
                entry.set("")

    def agregar_ventas(self):
        datos = self.obtener_datos()
        if not datos:
            return

        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO ventas (monto, trabajo_id, cliente_id)
                VALUES (%s, %s, %s)
            """, (*datos,))  # ← Usa *datos y coma final

            conn.commit()
            conn.close()
            self.cargar_ventas()
            self.limpiar()
            messagebox.showinfo("Éxito", "Venta agregado")

    def actualizar_ventas(self):
        seleccion = self.tree_gesVen.selection()
        if not seleccion:
            messagebox.showwarning("Selecciona", "Selecciona una venta")
            return

        item = self.tree_gesVen.item(seleccion[0])
        venta_id = item["values"][0]
        datos = self.obtener_datos()
        if not datos:
            return

        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE ventas SET monto=%s, trabajo_id=%s, cliente_id=%s
                WHERE venta_id=%s
            """, (*datos, venta_id))

            conn.commit()
            conn.close()
            self.cargar_ventas()
            messagebox.showinfo("Éxito", "Venta actualizada")

    def eliminar_ventas(self):
        seleccion = self.tree_gesVen.selection()
        if not seleccion:
            messagebox.showwarning("Selecciona", "Selecciona una venta")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar venta?"):
            venta_id = self.tree_gesVen.item(seleccion[0])["values"][0]

            conn = conectar()
            if conn:
                cursor = conn.cursor()
                cursor.execute(
                    "DELETE FROM ventas WHERE venta_id=%s", (
                        venta_id,)
                )
                conn.commit()
                conn.close()
                self.cargar_ventas()

    def obtener_datos(self):
        monto = self.entries["Monto"].get()
        trabajo = self.entries["Trabajo"].get()

        # Convertir texto → ID
        trabajo_id, cliente_id = self.map_trabajos.get(trabajo, (None, None))

        return monto, trabajo_id, cliente_id
