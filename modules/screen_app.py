import customtkinter
import modules.create_frame as m_frame
#
class App(customtkinter.CTk):
    def __init__(self,app_width,app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        #
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{100}")
        self.resizable(False, False)
        self.title("Головне вікно програми")
        self.FRAME_FONT = customtkinter.CTkFont("Arial", 15)
        self.FRAME = m_frame.My_Frame(text= "Friendly Chat", font= self.FRAME_FONT, master = self, width= 130, height= app_height - 20, border_width= 5)
        self.FRAME2 = m_frame.My_Frame(text= "Чати", font= self.FRAME_FONT, master = self, width= 130, height= app_height - 20, border_width= 5)
        self.FRAME3 = m_frame.My_Frame(text= "", font= self.FRAME_FONT, master = self, width= 500, height= app_height - 20, border_width= 5)
        # self.FRAME3 = m_frame.My_Frame(text= "", master = self, width= 500, height= app_height - 20, border_width= 5)
        # self.FRAME = customtkinter.CTkFrame(master=self, width=300, height= app_height)
        
        self.FRAME.grid(row = 1, column = 0, padx = 20, pady = 10)
        self.FRAME2.place(relx = 0.19, rely= 0.017, anchor = customtkinter.NW)
        self.FRAME3.place(relx = 0.36, rely= 0.017, anchor = customtkinter.NW)
        # self.FRAME.pack(padx= 10, pady = 10, expand = True)
        # self.FRAME.place(relx = 0, rely= 0)

main_app = App(800, 600)