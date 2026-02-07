import customtkinter as ctk
import tkinter.ttk as ttk
from services.movimientos_service import listar_movimientos

class MovimientosFrame(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(parent, corner_radius=0, fg_color="transparent")
		 
		ctk.CTkLabel(
			self,
			text="Movimientos",
			font=("Arial", 22, "bold"),
			fg_color="blue",
			text_color="white"
		).pack(pady=20, fill="both")

		self.table_frame = ctk.CTkFrame(self)
		self.table_frame.pack(fill="both", expand=True, padx=20, pady=10)
		self._create_table(self.table_frame)
		#self._build_header()
		self._load_data()
		self.debug()

		style = ttk.Style()
		style.theme_use("default")
		style.configure(
			"Treeview",
			background="#2b2b2b",
			foreground="#00ff00",
			rowheight=25,
			fieldbackground="#343638",
			bordercolor="#09f",
			borderwidth=0
		)
		style.map("Treeview", background=[("selected", "#22559b")])
		style.configure(
			"Treeview.Heading",
			font=('Calibri', 14, 'bold'),
			background="#1f1f1f",
			foreground="#0ff",
			relief="flat",
		)
		style.map("Treeview.Heading", background=[("active", "#3484F0")])

	def _create_table(self, parent):
		columns = ("tipo", "metodo", "monto")

		self.tree = ttk.Treeview(
		    parent,
		    columns=columns,
		    show="headings",
		    height=15
		)

		self.tree.heading("tipo", text="Tipo")
		self.tree.heading("metodo", text="Método")
		self.tree.heading("monto", text="Monto")

		self.tree.column("tipo", width=150, anchor="center")
		self.tree.column("metodo", width=150, anchor="center")
		self.tree.column("monto", width=100, anchor="e")

		self.tree.pack(fill="both", expand=True)

	def _build_header(self):
	    header = ctk.CTkFrame(self.table_frame)
	    header.pack(fill="x", pady=5)

	    for text in ("Tipo", "Método", "Monto"):
	        ctk.CTkLabel(
	            header,
	            text=text,
	            font=("Arial", 14, "bold"),
	            width=150
	        ).pack(side="left", padx=10)

	def _load_data(self):
		for tipo, metodo, monto in listar_movimientos():
			self.tree.insert(
				"",
				"end",
				values=(tipo, metodo, f"S/ {monto:.2f}")
			)


	def debug(self):
		print(listar_movimientos())