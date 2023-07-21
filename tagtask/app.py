# --------------- Gerênciador de Tarefas - Tag Task --------------- #
# --------------- Dev - Lucas Duarte Batista --------------- #

# Instalar dependências => pip install -r requirements.txt

import tkinter as tk
from tkinter import messagebox
import customtkinter
import openpyxl
from PIL import ImageTk, Image

# ------------------------------------------------------------------------------------------

class TagTask:
    def __init__(self):
        self.home = tk.Tk()
        self.home.title("Tag Task")
        self.home.state('zoomed')


        self.home.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.home.mainloop()



    #verificação de fechamento de Página
    def on_closing(self):
        if messagebox.askokcancel("Fechar", "Deseja realmente sair?"):
            self.home.destroy()


Home = TagTask()






