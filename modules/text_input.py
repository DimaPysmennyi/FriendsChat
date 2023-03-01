import customtkinter as ctk
import modules.screen_app as m_app

width_input = 250
height_input = 50

font_size = ctk.CTkFont(
    family= "Arial",
    size= 20,
    weight= "bold"
)

text = ctk.StringVar()

text_input = ctk.CTkEntry(
    master= m_app.main_app.FRAME3,
    width= width_input,
    height= height_input,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text
)

text_input.place(x = 200, y = 540, anchor = ctk.CENTER)