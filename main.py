import customtkinter as ctk
from ui.sidebar import Sidebar
from ui.dashboard import DashboardFrame
from ui.movimientos import MovimientosFrame
from ui.transferencias.TransferenciasFrame import TransferenciasFrame
from db.init_db import init_db

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestor de Dinero")
        self.geometry("700x500")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Layout en grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self, self.show_view)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Área principal
        self.main_area = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color=ctk.ThemeManager.theme["CTk"]["fg_color"]
        )
        self.main_area.grid(row=0, column=1, sticky="nsew")

        # Vistas
        self.views = {
            "dashboard": DashboardFrame(self.main_area),
            "movimientos": MovimientosFrame(self.main_area),
            "transferencias": TransferenciasFrame(self.main_area)
        }

        for view in self.views.values():
            view.pack(fill="both", expand=True)
            view.pack_forget()

        # Mostrar dashboard by default
        self.show_view("transferencias")


    def show_view(self, name):
        for view in self.views.values():
            view.pack_forget()

        self.views[name].pack(fill="both", expand=True)


if __name__ == "__main__":
    init_db()
    app = App()
    app.mainloop()
