import customtkinter as ctk
import modules.screen_app as m_app
import modules.text_input as m_input
import modules.create_frame as m_frame
import modules.create_form_frame as m_form

button_width = 70
button_height = 50
margin_left = 50
message_y = 0
button_color = "orange"
counter = 1



def send_message():
    global message_y
    global counter
    if m_input.text.get():
        if counter == 2:
            msg_frame = m_form.MessageFrame(text= m_input.text.get(), font= m_input.font_size, username= "Микола", master= m_app.main_app.FRAME4, width= 200, height= 60, border_width= 3)
            msg_frame.place_left()
            msg_frame.grid(row = message_y, pady = 10)
            # msg_frame.place(relx = 0.13 , rely = 0.9 , anchor = ctk.E)
            message_y += 1
            counter = 1
        else:
            msg_frame = m_form.MessageFrame(text= m_input.text.get(), font= m_input.font_size, username= "Дмитро", master= m_app.main_app.FRAME4, width= 200, height= 60, border_width= 3)
            msg_frame.place_right()
            msg_frame.grid(row = message_y, pady = 10)
            # msg_frame.place(relx =0.26 , rely =  0.9 ,anchor = ctk.W)
            message_y += 1
            counter = 2
        m_input.text_input.delete(0, ctk.END)

send_button = ctk.CTkButton(
    master = m_app.main_app.FRAME3, 
    text ="->",
    width = button_width,
    height = button_height,
    fg_color = button_color,
    command= send_message
)

send_button.place(
    x = m_app.main_app.FRAME3._current_width // 2 + m_input.width_input // 2, 
    y = m_app.main_app.FRAME3._current_height - button_height, 
    anchor = ctk.CENTER
)