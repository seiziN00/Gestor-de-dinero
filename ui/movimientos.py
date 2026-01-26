import customtkinter as ctk

class MovimientosFrame(ctk.CTkFrame):
	def __init__(self, parent):  #Este frame vive dentro de "parent"
		super().__init__(parent, corner_radius=0, fg_color="transparent") #Y parent es main_area
		 
		title = ctk.CTkLabel(
			self,
			text="Movimientos",
			font=("Arial", 22, "bold"),
			fg_color="blue",
			text_color="white"
		)
		title.pack(pady=20, fill="both")

		ctk.CTkLabel(self, text="Movimientos aquí... algún día.").pack()