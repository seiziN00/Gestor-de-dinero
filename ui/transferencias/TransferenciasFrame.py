import customtkinter as ctk
from config.constants import TIPOS_MOVIMIENTO, METODOS_PAGO
from .TransferenciasState import TransferenciasState


class TransferenciasFrame(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, corner_radius=0, fg_color="transparent")

        # ===== STATE =====
        self.state = TransferenciasState()

        # ===== LAYOUT BASE =====
        self._build_layout()
        self._build_radiobuttons()
        self._build_checkboxes()
        self._build_cambio()
        self._build_notas()
        self._build_action()

        self.entries_por_metodo = {}

        self.render()

    # =========================================================
    # BUILDERS
    # =========================================================

    def _build_layout(self):
        self.grid_columnconfigure((0, 1), weight=1)

        self.radiobutons_frame = ctk.CTkFrame(self)
        self.radiobutons_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nwes")

        self.checkboxes_frame = ctk.CTkFrame(self)
        self.checkboxes_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nwes")

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nwes")

        self.action_frame = ctk.CTkFrame(self)
        self.action_frame.grid(row=2, column=0, columnspan=2, padx=10, sticky="nwes")

        self.cambio_frame = ctk.CTkFrame(self)
        self.cambio_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nwes")

        self.textbox_frame = ctk.CTkFrame(self)
        self.textbox_frame.grid(row=4, column=0, columnspan=2, padx=10, pady=(5, 10), sticky="nwes")

    def get_tipo_dato(self):
        print(self.radio_var.get())
        print(type(self.radio_var.get()))

    def _build_radiobuttons(self):
        self.radio_var = ctk.IntVar(value=1)

        ctk.CTkLabel(
            self.radiobutons_frame,
            text="Tipo de movimiento",
            font=("Arial", 14, "bold")
        ).pack(fill="x", padx=10, pady=10)

        for k, v in TIPOS_MOVIMIENTO.items():
            ctk.CTkRadioButton(
                self.radiobutons_frame,
                text=v,
                variable=self.radio_var,
                value=k,
                command=self.on_tipo_change
            ).pack(anchor="w", padx=20, pady=2)

    def _build_checkboxes(self):
        ctk.CTkLabel(
            self.checkboxes_frame,
            text="Método de pago",
            font=("Arial", 14, "bold")
        ).pack(fill="x", padx=10, pady=10)

        self.checkbox_vars = {
            metodo: ctk.IntVar()
            for metodo in METODOS_PAGO
        }

        for metodo, var in self.checkbox_vars.items():
            ctk.CTkCheckBox(
                self.checkboxes_frame,
                text=metodo,
                variable=var,
                command=self.on_metodos_change
            ).pack(anchor="w", padx=20, pady=2)

    def _build_cambio(self):
        ctk.CTkLabel(self.cambio_frame, text="Cambio: S/").grid(row=0, column=0, padx=10)

        self.cambio_moneda = ctk.CTkEntry(self.cambio_frame)
        self.cambio_moneda.grid(row=0, column=1, padx=10)

        self.combobox_1 = ctk.CTkComboBox(
            self.cambio_frame,
            values=METODOS_PAGO
        )
        self.combobox_1.grid(row=1, column=0, padx=10, pady=10)

        ctk.CTkLabel(self.cambio_frame, text="→", font=("Arial", 30)).grid(row=1, column=1)

        self.combobox_2 = ctk.CTkComboBox(
            self.cambio_frame,
            values=METODOS_PAGO
        )
        self.combobox_2.grid(row=1, column=2, padx=10, pady=10)

    def _build_notas(self):
        ctk.CTkLabel(
            self.textbox_frame,
            text="Nota",
            font=("Arial", 14, "bold")
        ).pack(fill="x")

        self.textbox = ctk.CTkTextbox(self.textbox_frame, height=50)
        self.textbox.pack(fill="x", pady=5)

    def _build_action(self):
        self.ingresar_btn = ctk.CTkButton(
            self.action_frame,
            text="Ingresar",
            height=40,
            command=self.ingresar_callback
        )
        self.ingresar_btn.pack(fill="x")

    # =========================================================
    # CALLBACKS (solo estado)
    # =========================================================

    def on_tipo_change(self):
        self.state.tipo_movimiento = self.radio_var.get()
        self.get_tipo_dato()
        self.render()

    def on_metodos_change(self):
        self.state.metodos_pago = {
            k for k, v in self.checkbox_vars.items() if v.get()
        }
        self.render()

    # =========================================================
    # RENDER
    # =========================================================

    def render(self):
        self._hide_all()

        if self.state.tipo_movimiento in (1, 2):
            self._render_ingreso_gasto()
        else:
            self._render_cambio()

    def _render_ingreso_gasto(self):
        self.main_frame.grid()
        self.textbox_frame.grid()

        self._render_metodos_pago()

    def _render_cambio(self):
        self.cambio_frame.grid()
        self.textbox_frame.grid()

    def _render_metodos_pago(self):
        self._clear_main_frame()
        self.entries_por_metodo.clear()

        if not self.state.metodos_pago:
            self._show_no_pago()
            return

        self.action_frame.grid()

        for i, metodo in enumerate(self.state.metodos_pago):
            self._create_entry_row(i, metodo)

    # =========================================================
    # HELPERS
    # =========================================================

    def _hide_all(self):
        for frame in (
            self.main_frame,
            self.cambio_frame,
            self.action_frame,
            self.textbox_frame
        ):
            frame.grid_remove()

    def _clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def _show_no_pago(self):
        ctk.CTkLabel(
            self.main_frame,
            text="<Seleccione un método de pago>",
            font=("Arial", 18, "italic"),
            text_color="gray"
        ).pack(pady=20)

    def _create_entry_row(self, row, metodo):
        frame = ctk.CTkFrame(self.main_frame)
        frame.pack(fill="x", padx=10, pady=5)

        ctk.CTkLabel(frame, text=metodo, font=("Arial", 13, "bold")).pack(side="left")

        entry = ctk.CTkEntry(frame, placeholder_text="Monto")
        entry.pack(side="right")

        self.entries_por_metodo[metodo] = entry

    # =========================================================
    # DATA ACCESS
    # =========================================================

    def get_montos_por_metodo(self):
        return {
            metodo: float(entry.get() or 0)
            for metodo, entry in self.entries_por_metodo.items()
        }

    def ingresar_callback(self):
        print("Tipo:", TIPOS_MOVIMIENTO[self.state.tipo_movimiento])
        print("Montos:", self.get_montos_por_metodo())
        print("Nota:", self.textbox.get("1.0", "end").strip())
