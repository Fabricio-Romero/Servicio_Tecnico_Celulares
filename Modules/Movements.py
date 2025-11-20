import tkinter as tk
from tkinter import ttk, messagebox
from Database.db_connection import conectar
from Modules.Products import ProductosApp


class MovimientosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Movimientos")

        frame_gesProd = tk.Frame(root)
        frame_gesProd.pack(fill="x")

        tk.Button(
            frame_gesProd, text="GESTIONAR PRODUCTOS", bg="#2196F3", fg="white",
            font=("Arial", 10, "bold"),
            command=self.abrir_productos
        ).pack(side="right", padx=10, pady=10)

        frame = tk.Frame(root)
        frame.pack(padx=20)

        tk.Label(frame, text="Producto:").grid(row=0, column=0, sticky="w")
        self.producto_cb = ttk.Combobox(frame, width=40)
        self.producto_cb.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Tipo:").grid(row=1, column=0, sticky="w", pady=5)
        self.tipo_var = tk.StringVar(value="salida")

        ttk.Radiobutton(
            frame, text="Entrada", variable=self.tipo_var, value="entrada"
        ).grid(row=1, column=1, sticky="w")

        ttk.Radiobutton(
            frame, text="Salida (Venta)", variable=self.tipo_var, value="salida"
        ).grid(row=1, column=1, sticky="e")

        tk.Label(frame, text="Cantidad:").grid(
            row=2, column=0, sticky="w", pady=5)
        self.cantidad_entry = tk.Entry(frame, width=20)
        self.cantidad_entry.grid(row=2, column=1, sticky="w")

        tk.Button(
            frame, text="REGISTRAR", bg="#FF5722", fg="blue",
            font=("Arial", 10, "bold"),
            command=self.registrar
        ).grid(row=3, column=0, columnspan=2)

        # Tabla de movimientos recientes
        self.tree = ttk.Treeview(
            root,
            columns=("Fecha", "Cantidad", "Tipo", "Producto"),
            show="headings"
        )
        for col, text in zip(
            self.tree["columns"],
            ["Fecha", "Cantidad", "Tipo", "Producto"]
        ):
            self.tree.heading(col, text=text)
            self.tree.column(col, width=140, anchor="center")

        self.tree.pack(pady=10, padx=20, fill="both", expand=True)

        self.cargar_productos()
        self.cargar_movimientos()

    def abrir_productos(self):
        self.nueva_ventana("Productos", lambda root: ProductosApp(
            root, es_admin=True), "850x500")

    def cargar_productos(self):
        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT producto_id, nombre FROM productos")
            productos = {row[1]: row[0] for row in cursor.fetchall()}
            self.producto_cb["values"] = list(productos.keys())
            self.productos_dict = productos
            conn.close()

    def cargar_movimientos(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        conn = conectar()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT m.fecha, m.cantidad, m.tipo, p.nombre
                FROM movimientos_productos m
                JOIN productos p ON m.producto_id = p.producto_id
                ORDER BY m.fecha DESC LIMIT 20
            """)

            for row in cursor.fetchall():
                tipo = "ENTRADA" if row[3] == "entrada" else "SALIDA"
                self.tree.insert(
                    "", 0,
                    values=(row[0], row[1], row[2], row[3])
                )
            conn.close()

    def registrar(self):
        producto_nombre = self.producto_cb.get()
        tipo = self.tipo_var.get()
        cantidad_str = self.cantidad_entry.get()

        if not all([producto_nombre, cantidad_str]):
            messagebox.showwarning(
                "Faltan datos", "Selecciona producto y cantidad")
            return

        try:
            cantidad = int(cantidad_str)
            if cantidad <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Cantidad debe ser número > 0")
            return

        producto_id = self.productos_dict.get(producto_nombre)
        if not producto_id:
            return

        conn = conectar()
        if not conn:
            return

        cursor = conn.cursor()

        # Verificar stock en salida
        if tipo == "salida":
            cursor.execute(
                "SELECT cantidad FROM productos WHERE producto_id = %s",
                (producto_id,)
            )
            stock = cursor.fetchone()[0]
            if cantidad > stock:
                messagebox.showerror(
                    "Stock insuficiente",
                    f"Solo hay {stock} unidades"
                )
                conn.close()
                return

        # Registrar movimiento
        cursor.execute("""
            INSERT INTO movimientos_productos (cantidad, tipo, producto_id)
            VALUES (%s, %s, %s)
        """, (cantidad, tipo, producto_id))

        # Actualizar stock
        op = "+" if tipo == "entrada" else "-"
        cursor.execute(
            f"UPDATE productos SET cantidad = cantidad {op} %s WHERE producto_id = %s",
            (cantidad, producto_id)
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Éxito",
            f"Movimiento registrado: {tipo.upper()} de {cantidad} unidad(es)"
        )

        self.cargar_movimientos()
        self.cantidad_entry.delete(0, "end")

    def nueva_ventana(self, titulo, clase, size):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.geometry(size)
        clase(ventana)
