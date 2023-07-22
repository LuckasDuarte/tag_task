# --------------- Gerênciador de Tarefas - Tag Task --------------- #
# --------------- Dev - Lucas Duarte Batista --------------- #

# Instalar dependências => pip install -r requirements.txt

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import openpyxl
from PIL import ImageTk, Image

# ------------------------------------------------------------------------------------------

class TagTask:
    def __init__(self):
        self.home = tk.Tk()
        self.home.title("Tag Task")
        self.home.state('zoomed')

        icon_path = "tagtask/images/box.ico"  # Icone
        icon_image = Image.open(icon_path)
        self.home.iconphoto(True, ImageTk.PhotoImage(icon_image))

        self.home.protocol("WM_DELETE_WINDOW", self.on_closing)


        # ----- Frame Sidebar
        screen_width = self.home.winfo_screenwidth()
        self.Frame_Sidebar = ctk.CTkFrame(self.home, width = 80, height= screen_width, fg_color="#069", corner_radius=0)
        self.Frame_Sidebar.grid(column = 0, row = 0)

        # ---------- Itens Menu Sidebar -----------
        







        self.home.mainloop()

        













    #verificação de fechamento de Página
    def on_closing(self):
        if messagebox.askokcancel("Fechar", "Deseja realmente sair?"):
            self.home.destroy()


Home = TagTask()






