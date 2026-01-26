import customtkinter as ctk


class Sidebar(ctk.CTkFrame):               
    def __init__(self, parent, on_select): 
        super().__init__(parent, width=200, corner_radius=0)
        #on_select es una función que alguien le pasa a la sidebar
        #El on_select avisa 'el usuario hizo click aquí'

        ctk.CTkLabel(
            self, 
            text="Menú", 
            font=("Arial", 18, "bold")
        ).pack(pady=20)

        ctk.CTkButton(
            self, 
            text="Dashboard", 
            command=lambda: on_select("dashboard")
        ).pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(
            self, 
            text="Movimientos", 
            command=lambda: on_select("movimientos")
        ).pack(fill="x", padx=20, pady=5)

        ctk.CTkButton(
            self, 
            text="Transferencias", 
            command=lambda: on_select("transferencias")
        ).pack(fill="x", padx=20, pady=5)
