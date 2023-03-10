import customtkinter as ctk
import modules.screen_app as m_app
import modules.text_input as m_input
import modules.create_frame as m_frame
import modules.create_form_frame as m_form

button_width = 70
button_height = 50
margin_left = 50
message_y = 20
button_color = "orange"
counter = 1



def send_message():
    global message_y
    global counter

    if counter == 2:
        msg_frame = m_form.MessageFrame(text= m_input.text.get(), font= m_input.font_size, username= "Николай", master= m_app.main_app.FRAME4, width= 200, height= 60, border_width= 3)
        msg_frame.place_left()
        msg_frame.place(x=10,y=message_y)
        message_y += 60
        counter = 1
    else:
        msg_frame = m_form.MessageFrame(text= m_input.text.get(), font= m_input.font_size, username= "Дмитро", master= m_app.main_app.FRAME4, width= 200, height= 60, border_width= 3)
        msg_frame.place_right()
        msg_frame.place(x=300,y=message_y)
        message_y += 60
        counter = 2
    print(counter)

    


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