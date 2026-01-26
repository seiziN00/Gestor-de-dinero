import customtkinter as ctk

class TransferenciasFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="transparent")

        # ===== GRID CONTAINERS =====
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.radiobutons_frame = ctk.CTkFrame(self)
        self.radiobutons_frame.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="nwes")
        self.radiobutons_frame.grid_columnconfigure(0, weight=1)

        self.checkboxes_frame = ctk.CTkFrame(self)
        self.checkboxes_frame.grid(row=0, column=1, padx=(5, 10), pady=(10, 5), sticky="nwes")
        self.checkboxes_frame.grid_columnconfigure(1, weight=1)

        self.cambio_frame =ctk.CTkFrame(self)
        self.cambio_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nwes")
        self.cambio_frame.grid_columnconfigure((0, 1), weight=1)
        self.cambio_frame.grid_rowconfigure((0, 1), weight=1)

        self.textbox_frame = ctk.CTkFrame(self)
        self.textbox_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 10), sticky="nwes")
        self.textbox_frame.grid_columnconfigure(0, weight=1)

        # ===== RADIO BUTTONS =====
        self.radio_var = ctk.IntVar(value=1)  # default seleccionado

        ctk.CTkLabel(
        	self.radiobutons_frame, 
        	text="Tipo de movimiento", 
        	font=("Arial", 14, "bold"),
        	fg_color="gray30",
        	corner_radius=6
        ).grid(row=0, column=0, padx=10, pady=12, sticky="we")
        
        for i, text in enumerate(["Ingreso", "Gasto", "Cambio", "Préstamo"], start=1):
            ctk.CTkRadioButton(
                self.radiobutons_frame,
                text=text,
                variable=self.radio_var,
                value=i,
                command=self.radiobutton_event
            ).grid(row=i, column=0, pady=4, padx=20, sticky="w")

        # ===== CHECKBOXES =====
        ctk.CTkLabel(
        	self.checkboxes_frame, 
        	text="Método de pago", 
        	font=("Arial", 14, "bold"),
        	fg_color="gray30",
        	corner_radius=6
        ).grid(row=0, column=1, padx=10, pady=12, sticky="we")

        # Cada checkbox tiene su propia variable
        self.checkbox_vars = {
            "Efectivo": ctk.IntVar(value=0),
            "Scotiabank/Plin": ctk.IntVar(value=0),
            "Yape": ctk.IntVar(value=0)
        }

        c = 1
        for text, var in self.checkbox_vars.items():
            ctk.CTkCheckBox(
                self.checkboxes_frame,
                text=text,
                variable=var,
                command=self.checkbox_event
            ).grid(row=c, column=1, pady=4, padx=20, sticky="w")
            c += 1

        # ===== CAMBIO =====
        ctk.CTkLabel(
        	self.cambio_frame,
        	text="Cambio: S/",
        ).grid(row=0, column=0, padx=10, pady=5)

        ctk.CTkEntry(
        	self.cambio_frame,
        	placeholder_text="Money"
        ).grid(row=0, column=1, padx=10, pady=5)

        self.combobox_1 = ctk.CTkComboBox(
        	self.cambio_frame,
        	values=["Efectivo", "Scotiabank/Plin", "Yape"],
        	command=self.combobox_callback
        )
        self.combobox_1.grid(row=1, column=0, padx=25, pady=10)
        self.combobox_1.set("Efectivo")

        ctk.CTkLabel(
        	self.cambio_frame,
        	text="→",
        	font=("Arial", 36, "bold")
        ).grid(row=1, column=1, padx=5, pady=10, sticky="n")

        self.combobox_2 = ctk.CTkComboBox(
        	self.cambio_frame,
        	values=["Efectivo", "Scotiabank/Plin", "Yape"],
        	command=self.combobox_callback
        )
        self.combobox_2.grid(row=1, column=2, padx=25, pady=10)
        self.combobox_2.set("Efectivo")

        ctk.CTkButton(
        	self.cambio_frame,
        	text="cambiar",
        	command=self.cambio_callback
        ).grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="we")

        # ===== NOTAS =====
        ctk.CTkLabel(
        	self.textbox_frame,
        	text="Notas",
        	font=("Arial", 14, "bold"),
        	fg_color="gray30",
        	corner_radius=6
        ).grid(row=0, column=0, sticky="we")
        self.textbox = ctk.CTkTextbox(
        	self.textbox_frame,
        	height=80
        )
        self.textbox.grid(row=1, column=0, sticky="we")

    # ===== CALLBACKS =====
    def radiobutton_event(self):
        print("RadioButton seleccionado →", self.radio_var.get())

    def checkbox_event(self):
        # Mostrar todos los seleccionados
        selected = [k for k, v in self.checkbox_vars.items() if v.get() == 1]
        print("Checkbox seleccionados →", selected)

    def combobox_callback(self, choice):
    	print("combobox dropdown clicked:", choice)

    def cambio_callback(self):
    	print("Cambio de", self.combobox_1.get(), "a", self.combobox_2.get())