import customtkinter as ctk

TIPOS_MOVIMIENTO = {
    1: "Ingreso",
    2: "Gasto",
    3: "Cambio",
    4: "Préstamo"
}

class TransferenciasFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="transparent")

        # ===== GRID CONTAINERS =====
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.radiobutons_frame = ctk.CTkFrame(self)
        self.radiobutons_frame.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky="nwes")
        self.radiobutons_frame.grid_columnconfigure(0, weight=1)

        self.checkboxes_frame = ctk.CTkFrame(self)
        self.checkboxes_frame.grid(row=0, column=1, padx=(5, 10), pady=(10, 5), sticky="nwes")
        self.checkboxes_frame.grid_columnconfigure(1, weight=1)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nwes")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.action_frame = ctk.CTkFrame(self)
        self.action_frame.grid(
            row=2, column=0, columnspan=2,
            padx=10, pady=(0, 5), sticky="we"
        )
        self.action_frame.grid_columnconfigure(0, weight=1)
        self.action_frame.grid_remove()
        self.ingresar_btn = ctk.CTkButton(
            self.action_frame,
            text="Ingresar",
            height=40,
            command=self.ingresar_callback
        )
        self.ingresar_btn.grid(row=0, column=0, sticky="we")

        self.cambio_frame = ctk.CTkFrame(self)
        self.cambio_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nwes")
        self.cambio_frame.grid_columnconfigure((0, 1), weight=1)
        self.cambio_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.textbox_frame = ctk.CTkFrame(self)
        self.textbox_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=(5, 10), sticky="nwes")
        self.textbox_frame.grid_columnconfigure(0, weight=1)

        self.main_frame.grid_remove()
        self.cambio_frame.grid_remove()

        # ===== RADIO BUTTONS =====
        self.radio_var = ctk.IntVar(value=1)  # default seleccionado

        ctk.CTkLabel(
        	self.radiobutons_frame, 
        	text="Tipo de movimiento", 
        	font=("Arial", 14, "bold"),
        	fg_color="gray30",
        	corner_radius=6
        ).grid(row=0, column=0, padx=10, pady=12, sticky="we")
        
        

        for k, v in TIPOS_MOVIMIENTO.items():
            ctk.CTkRadioButton(
                self.radiobutons_frame,
                text=v,
                variable=self.radio_var,
                value=k,
                command=self.radiobutton_event
            ).grid(row=k, column=0, pady=4, padx=20, sticky="w")

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
            "Yape": ctk.IntVar(value=0),
            "Scotiabank/Plin": ctk.IntVar(value=0)
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

        self.cambio_moneda = ctk.CTkEntry(
        	self.cambio_frame,
        	placeholder_text="Money"
        )
        self.cambio_moneda.grid(row=0, column=1, padx=10, pady=5)

        self.combobox_1 = ctk.CTkComboBox(
        	self.cambio_frame,
        	values=["Efectivo", "Yape", "Scotiabank/Plin"],
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
        	values=["Efectivo", "Yape", "Scotiabank/Plin"],
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
        	text="Nota",
        	font=("Arial", 14, "bold"),
        	fg_color="gray30",
        	corner_radius=6
        ).grid(row=0, column=0, sticky="we")
        self.textbox = ctk.CTkTextbox(
        	self.textbox_frame,
        	height=40
        )
        self.textbox.grid(row=1, column=0, sticky="we")

        self.no_pago_label = ctk.CTkLabel(
            self.main_frame,
            text="<Seleccione un método de pago>",
            font=("Arial", 22, "italic"),
            text_color="gray70"
        )

        self.entries_por_metodo = {}

        self.radiobutton_event()

        
    # ===== GETters =====
    def get_cambio(self):
        return {
            "monto": self.cambio_moneda.get(),
            "origen": self.combobox_1.get(),
            "destino": self.combobox_2.get()
        }

    def get_tipo_movimiento(self):
        return TIPOS_MOVIMIENTO.get(self.radio_var.get())

    # ===== CALLBACKS =====
    def radiobutton_event(self):
        tipo_id = self.radio_var.get()
        tipo_texto = TIPOS_MOVIMIENTO[tipo_id]

        print("Tipo movimiento →", tipo_texto)

        if tipo_id in (1, 2):
            self.show_main_frame()
            self.update_main_frame()
        else:
            self.show_cambio_frame()
            self.action_frame.grid_remove()


    def checkbox_event(self):
        selected = [k for k, v in self.checkbox_vars.items() if v.get() == 1]
        print("Checkbox seleccionados →", selected)
        self.update_main_frame()

    def combobox_callback(self, choice):
    	print("combobox dropdown clicked:", choice)

    def cambio_callback(self):
    	print("Cambio de", self.combobox_1.get(), "a", self.combobox_2.get(), self.cambio_moneda.get())

    def ingresar_callback(self):
        print("Tipo", self.get_tipo_movimiento())
        print("Monto(s)", self.get_montos_por_metodo())
        print("Nota", self.textbox.get("1.0", "end").strip())

    # Para mostrar / ocultar los frames
    def show_main_frame(self):
        self.cambio_frame.grid_remove()
        self.main_frame.grid() 

    def show_cambio_frame(self):
        self.main_frame.grid_remove()
        self.cambio_frame.grid()

    # Limpiar el mainframe
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.grid_remove()

    # Updatear el mainframe
    def update_main_frame(self):
        self.clear_main_frame()
        self.entries_por_metodo.clear()

        seleccionados = [
            k for k, v in self.checkbox_vars.items() if v.get() == 1
        ]

        if not seleccionados:
            self.no_pago_label.grid(row=0, column=0, pady=20)
            self.action_frame.grid_remove()
            return

        self.action_frame.grid()

        for i, metodo in enumerate(seleccionados):
            frame = ctk.CTkFrame(self.main_frame)
            frame.grid(row=i, column=0, padx=10, pady=6, sticky="we")

            ctk.CTkLabel(
                frame,
                text=metodo,
                font=("Arial", 13, "bold")
            ).pack(side="left", padx=10)

            entry = ctk.CTkEntry(
                frame,
                placeholder_text="Monto"
            )
            entry.pack(side="right", padx=10)

            # Guardar referencias en el dict
            self.entries_por_metodo[metodo] = entry

    # Helper para ver por cmd el output
    def get_montos_por_metodo(self):
        datos = {}

        for metodo, entry in self.entries_por_metodo.items():
            valor = entry.get().strip()

            if valor == "":
                datos[metodo] = 0
            else:
                datos[metodo] = float(valor)

        return datos