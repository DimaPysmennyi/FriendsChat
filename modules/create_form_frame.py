import customtkinter as ctk

class MessageFrame(ctk.CTkFrame):
    def __init__(self, text, font, username, master, width, height, border_width, **kwargs):
        super().__init__(master= master, width= width, height= height, border_width= border_width, **kwargs)
        self.MESSAGE = text
        self.FONT = font
        self.USERNAME = username

    def place_right(self):
        self.MESSAGE = ctk.CTkLabel(self, text= self.MESSAGE)
        self.MESSAGE.place(x = 10, y = 30)
        self.NICKNAME = ctk.CTkLabel(master= self, text= self.USERNAME, font= self.FONT)
        self.NICKNAME.place(x = 120, y = 2)
    
    def place_left(self):
        self.MESSAGE = ctk.CTkLabel(self, text= self.MESSAGE)
        self.MESSAGE.place(x = 10, y = 30)
        self.NICKNAME = ctk.CTkLabel(master= self, text= self.USERNAME, font= self.FONT)
        self.NICKNAME.place(x = 10, y = 2, anchor= ctk.NW)