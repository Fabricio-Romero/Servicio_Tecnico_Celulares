from ctypes.macholib import framework
import tkinter as tk
from tkinter import ttk, messagebox
from Modules.AdminUser import AdminUserApp
from Modules.Customers import ClientesApp
from Modules.Jobs import TrabajosApp
from Modules.Movements import MovimientosApp
# from Modules.Phones import CelularesApp
from Modules.Products import ProductosApp
# from Modules.Sales import VentasApp
from Modules.Suppliers import ProveedoresApp


class MenuApp:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario
        self.root.title(f"Servicio Técnico - {usuario[3].title()}")
        self.root.geometry("800x600")
        tk.Label(root, text=f"Usuario: {usuario[1]} {usuario[2]} ({usuario[3]})", font=(
            "Arial", 10,)).pack(anchor="ne", padx=20, pady=10)
        tk.Label(root, text=f"SERVICIO TÉCNICO {usuario[1]} {usuario[2]}".upper(),
                 font=("Arial", 18, "bold")).pack(pady=20)

        # Definir estilo de botones grandes
        btn_style = {"width": 30, "height": 2, "font": ("Arial", 11, "bold")}

        frame = tk.Frame(root)
        frame.pack(pady=20, padx=20)

        # Botones
        tk.Button(frame, text="CONTROL DE TRABAJOS", bg="#2196F3", fg="white",
                  **btn_style, command=self.abrir_trabajos).grid(row=1, column=0, pady=15)
        tk.Button(frame, text="REGISTRAR MOVIMIENTOS", bg="#FF9800", fg="white",
                  **btn_style, command=self.abrir_movimientos).grid(row=2, column=0, pady=15)
        tk.Button(frame, text="VER CLIENTES", bg="#9C27B0", fg="white",
                  **btn_style, command=self.abrir_clientes).grid(row=3, column=0, pady=15)

        # tk.Button(frame, text="GESTIÓN DE CATEGORIAS", bg="#216EF3", fg="white",
        #           **btn_style, command=self.abrir_categorias).grid(row=1, column=1, padx=15)
        tk.Button(frame, text="ADMINISTRAR PROVEEDORES", bg="#F32159", fg="white",
                  **btn_style, command=self.abrir_proveedores).grid(row=2, column=1, padx=15)
        tk.Button(frame, text="ADMINISTRAR USUARIOS", bg="#40B027", fg="white",
                  **btn_style, command=self.abrir_admin_usuarios).grid(row=3, column=1, pady=15)

        tk.Button(root, text="CERRAR SESIÓN", bg="#F44336", fg="white",
                  **btn_style, command=root.destroy).pack(pady=15)

    def abrir_trabajos(self):
        self.nueva_ventana("Trabajos", TrabajosApp, "1366x720")

    # Lo dejo para ver como es para los usuarios admin y super_usuario
    # def abrir_categorias(self):
    #     if self.usuario[4] == "admin" or self.usuario[4] == "super_usuario":  # usuario[4] = rol
    #         self.nueva_ventana(
    #             "Categorias", lambda root: CategoriasApp(root, es_admin=True))
    #     else:
    #         messagebox.showwarning(
    #             "Acceso denegado", "Solo el admin puede gestionar productos")

    def abrir_proveedores(self):
        if self.usuario[4] == "admin" or self.usuario[4] == "super_usuario":  # usuario[4] = rol
            self.nueva_ventana(
                "Proveedores", lambda root: ProveedoresApp(root, es_admin=True), "1024x500")

        else:
            messagebox.showwarning(
                "Acceso denegado", "Solo el admin puede gestionar productos")

    def abrir_movimientos(self):
        self.nueva_ventana("Movimientos", MovimientosApp, "800x500")

    def abrir_clientes(self):
        self.nueva_ventana("Reportes", ClientesApp, "800x500")

    def abrir_admin_usuarios(self):
        if self.usuario[4] == "super_usuario":
            self.nueva_ventana("AdministrarUsuarios", lambda root: AdminUserApp(
                root, es_super_user=True), "800x500")
        else:
            messagebox.showwarning(
                "Acceso denegado", "Solo el super usuario puede administrar los usuarios")

    def nueva_ventana(self, titulo, clase, size):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.geometry(size)
        clase(ventana)
