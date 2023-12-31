# --------------- Gerênciador de Tarefas - Tag Task --------------- #
# --------------- Dev - Lucas Duarte Batista --------------- #

# Instalar dependências => pip install -r requirements.txt

import tkinter as tk
from tkinter import messagebox, ttk, PhotoImage
import customtkinter as ctk
import openpyxl
from PIL import ImageTk, Image
from idlelib.tooltip import Hovertip

# -------- Cores ---------
azul = "#0f22a2"
fundo = "#e8eaf5"
select = "#bbc4e8"
fundo_sec = "#659ac6"

# ------------------------------------------------------------------------------------------

class TagTask:
    def __init__(self):
        self.home = tk.Tk()
        self.home.title("Tag Task")
        self.home.state('zoomed')
        self.home.configure(bg= fundo)

        icon_path = "tagtask/images/box.ico"  # Icone
        icon_image = Image.open(icon_path)
        self.home.iconphoto(True, ImageTk.PhotoImage(icon_image))

        # self.home.protocol("WM_DELETE_WINDOW", self.on_closing)


        # ----- Frame Sidebar
        screen_width = self.home.winfo_screenwidth()
        screen_height = self.home.winfo_screenheight()
        self.Frame_Sidebar = ctk.CTkFrame(self.home, width = 80, height= screen_width / 2, fg_color=select, corner_radius=25)
        self.Frame_Sidebar.grid(column = 0, row = 0, padx=10, pady=10)

        # ---------- Itens Menu Sidebar -----------

        # Adicionar
        add_image = PhotoImage(file="tagtask/images/adicionar.png") # Icone
        self.btn_adicionar = ctk.CTkButton(self.Frame_Sidebar, text="", cursor="hand2", image= add_image,width=30,height=50, fg_color="transparent", hover_color=fundo_sec,corner_radius= 8)
        self.btn_adicionar.place(x= 15, y= 80)
        nota = Hovertip(self.btn_adicionar, "Adicionar Tarefa", hover_delay=500)

        # Atualizar


        # Excluir
        # Listagem de Tarefas

        # --- Componentes Tela Home
        self.Frame_Home = ctk.CTkFrame(self.home, width= screen_width - 110, height= screen_height - 90, fg_color=select, corner_radius= 8)
        self.Frame_Home.grid(column = 1, row = 0, sticky="n", pady= 10)







        self.home.mainloop()

        













    #verificação de fechamento de Página
    # def on_closing(self):
    #     if messagebox.askokcancel("Fechar", "Deseja realmente sair?"):
    #         self.home.destroy()


Home = TagTask()






