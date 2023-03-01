import customtkinter as ctk
import modules.screen_app as m_app
import modules.text_input as m_input
import modules.create_frame as m_frame

button_width = 70
button_height = 50
margin_left = 50
message_y = 20
button_color = "orange"


class MessageFrame(m_frame.My_Frame):
    def __init__(self, text, font, master, width, height, border_width, **kwargs):
        super().__init__(text, font, master, width, height, border_width, **kwargs)
        self.NICK = ctk.CTkLabel(master=self, text="Дмитро", font=ctk.CTkFont("Arial", 15))
        self.NICK.place(x = 10, y = 2, anchor=ctk.NW)

def send_message():
    global message_y
    # msg_frame = m_frame.My_Frame(text=None, master=m_app.main_app.FRAME3, width=480, height=50, border_width=3)
    # button_label = ctk.CTkLabel(
    #     master = msg_frame, 
    #     text = m_input.text.get(),
    #     font = m_input.font_size
    # )
    msg_frame = MessageFrame(text=m_input.text.get(), font= m_input.font_size, master=m_app.main_app.FRAME3, width=450, height=80, border_width=3)
    msg_frame.place(x=50,y=message_y)
    message_y += 80

send_button = ctk.CTkButton(
    master = m_app.main_app.FRAME3, 
    text ="->",
    width = button_width,
    height = button_height,
    fg_color = button_color,
    command= send_message
)

send_button.place(
    x = 360, #m_app.main_app.APP_WIDTH // 2 + m_input.width_input // 2 + margin_left 
    y = 540, #m_app.main_app.APP_HEIGHT - button_height // 2
    anchor = ctk.CENTER
)