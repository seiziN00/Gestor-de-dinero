import customtkinter as ctk

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, parent):  #Es mejor "self, parent" en lugar de "app"
        super().__init__(parent, corner_radius=0, fg_color="transparent") #El componente es reutilizable

        ctk.CTkLabel(
            self,
            text="Bienvenido al Gestor de Dinero",
            font=("Arial", 22)
        ).pack(pady=40)
