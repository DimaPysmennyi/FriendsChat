import customtkinter as ctk
import modules.screen_app as m_app
# import modules.create_frame as m_frame

def create_button(master, text, width = 120, height= 50, border_width= 2, corner_radius = 5, border_color = "purple", bg_color = "orange"):
    button = ctk.CTkButton(master = master,
                           width = width,
                           height = height,
                           border_width = border_width,
                           corner_radius = corner_radius,
                           border_color = border_color,
                           text = text,
                           bg_color = bg_color
    )
    return button

bt1 = create_button(master=m_app.main_app.FRAME,
                    text='Чати'
                )
bt1.place(relx = 0.02, rely= 0.12, anchor=ctk.NW)

bt2 = create_button(master = m_app.main_app.FRAME,
                    text = "Контакти"
                )
bt2.place(relx = 0.02, rely=0.21, anchor=ctk.NW)

bt3 = create_button(master = m_app.main_app.FRAME,
                    text = "Налаштування"   
                )
bt3.place(relx = 0.02, rely = 0.3, anchor = ctk.NW)

bt4 = create_button(master = m_app.main_app.FRAME2,
                    text = "Діма" 
                )
bt4.place(relx = 0.02, rely = 0.3, anchor = ctk.NW)

bt5 = create_button(master = m_app.main_app.FRAME2,
                    text = "Богдан" 
                )
bt5.place(relx = 0.02, rely=0.21, anchor = ctk.NW)

bt6 = create_button(master = m_app.main_app.FRAME2,
                    text = "Феликс"   
                )
bt6.place(relx = 0.02, rely = 0.12, anchor = ctk.NW)