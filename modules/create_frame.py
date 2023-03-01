import customtkinter as ctk 

class My_Frame(ctk.CTkFrame):
    def __init__(self, text, font, master, width, height, border_width, **kwargs):
        super().__init__(master = master,width = width, height = height, border_width = border_width, **kwargs)
        self.LABEL = ctk.CTkLabel(self, text= text, font=font)
        self.LABEL.place(x = 10, y = 30)