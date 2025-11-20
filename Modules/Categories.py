import tkinter as tk
from tkinter import ttk, messagebox
from turtle import st
from typing import Self
from Database.db_connection import conectar
from datetime import datetime


class CategoriasApp:
    def __init__(self, root, es_admin=False):
        self.root = root
        self.es_admin = es_admin
        self.root.title("Categorias")

        frame = tk.Frame(root)
        frame.pack(padx=20, pady=20)

        self.entries = {}

        # Tabla de categorias
        self.tree = ttk.Treeview(
            frame,
            columns=("id", "nombre"),
            show="headings",
            height=15
        )
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        self.tree.grid(row=0, column=1, rowspan=10,
                       columnspan=2, sticky="e", padx=15, ipadx=150, ipady=55)

        tk.Label(frame, text="Nombre:").grid(
            row=0, column=0, sticky="n")
        self.entries["Nombre"] = tk.Entry(
            frame, width=33)
        self.entries["Nombre"].grid(row=1, column=0, sticky="w")

        tk.Button(
            frame, text="AGREGAR", bg="#6CFF22", fg="blue",
            font=("Arial", 10, "bold"),
            command=self.agregar
        ).grid(row=3, column=0, sticky="n")
        tk.Button(
            frame, text="ACTUALIZAR", bg="#227EFF", fg="orange",
            font=("Arial", 10, "bold"),
            command=self.actualizar
        ).grid(row=4, column=0, sticky="n")
        tk.Button(
            frame, text="ELIMINAR", bg="#F80000", fg="black",
            font=("Arial", 10, "bold"),
            command=self.eliminar
        ).grid(row=5, column=0, sticky="n")
        tk.Button(
            frame, text="LIMPIAR", bg="#00F2FF", fg="green",
            font=("Arial", 10, "bold"),
            command=self.limpiar
        ).grid(row=6, column=0, sticky="n")

        self.cargar_categorias()
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar)

    def agregar(self):
        datos = self.obtener_datos()
        if not datos:
            return

        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO categorias(nombre)
                VALUES (%s)
            """, (datos,))  # ← Usa *datos y coma final

            conn.commit()
            conn.close()
            self.cargar_categorias()
            self.limpiar()
            messagebox.showinfo("Éxito", "Categoria agregada")

    def actualizar(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selecciona", "Selecciona una categoria")
            return

        item = self.tree.item(seleccion[0])
        categoria_id = item["values"][0]
        datos = self.obtener_datos()
        if not datos:
            return

        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE categorias SET nombre=%s
                WHERE categoria_id=%s
            """, (datos, categoria_id))

            conn.commit()
            conn.close()
            self.cargar_categorias()
            messagebox.showinfo("Éxito", "Categoria actualizada")

    def eliminar(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selecciona", "Selecciona una categoria")
            return

        if messagebox.askyesno("Confirmar", "¿Eliminar categoria?"):
            categoria_id = self.tree.item(seleccion[0])["values"][0]

            conn = conectar()
            if conn:
                cursor = conn.cursor()
                cursor.execute(
                    "DELETE FROM categorias WHERE categoria_id=%s", (
                        categoria_id,)
                )
                conn.commit()
                conn.close()
                self.cargar_categorias()

    def limpiar(self):
        for entry in self.entries.values():
            if isinstance(entry, tk.Entry):
                entry.delete(0, "end")
            elif isinstance(entry, ttk.Combobox):
                entry.set("")

    def cargar_categorias(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT *
                FROM categorias
            """)

            for row in cursor.fetchall():
                self.tree.insert("", "end", values=row)
            conn.close()

    def seleccionar(self, event):
        seleccion = self.tree.selection()

        if seleccion:
            valores = self.tree.item(seleccion[0])["values"]
            self.limpiar()

            self.entries["Nombre"].insert(0, valores[1])

    def obtener_datos(self):
        nombre = self.entries["Nombre"].get().strip()
        return nombre
