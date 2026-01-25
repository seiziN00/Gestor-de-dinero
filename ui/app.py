import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestor de Dinero")
        self.geometry("900x500")

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Layout en grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Área principal
        self.main_area = ctk.CTkFrame(self)
        self.main_area.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self._build_sidebar()
        self._build_main_area()

    def _build_sidebar(self):
        title = ctk.CTkLabel(
            self.sidebar,
            text="Menú",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=20)

        ctk.CTkButton(self.sidebar, text="Cuentas").pack(fill="x", padx=20, pady=5)
        ctk.CTkButton(self.sidebar, text="Movimientos").pack(fill="x", padx=20, pady=5)
        ctk.CTkButton(self.sidebar, text="Transferencias").pack(fill="x", padx=20, pady=5)

    def _build_main_area(self):
        label = ctk.CTkLabel(
            self.main_area,
            text="Bienvenido al Gestor de Dinero",
            font=("Arial", 22)
        )
        label.pack(pady=40)
