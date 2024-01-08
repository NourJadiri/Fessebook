import customtkinter as ctk
from src.front.frames.LoginFrame import LoginFrame
from src.front.frames.UserFrame import UserFrame
from src.front.frames.LoginFrame import sc


class IHM(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        super().__init__(*args, **kwargs)

        self.geometry('1200x800')

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.login_frame = LoginFrame(master=self.main_frame, callback=self.login)
        self.login_frame.pack(fill="both", expand=True)


        self.show_frame(self.login_frame)

    def login(self):
        username = self.login_frame.login_entry.get()
        password = self.login_frame.password_entry.get()

        status = sc.login(username, password)

        if status:
            print(sc.session_user)
            self.user_frame = UserFrame(master=self.main_frame, user = sc.session_user)
            self.show_frame(self.user_frame)
            self.login_frame.pack_forget()
        else:
            self.login_frame.password_entry.delete(0, 'end')
            self.login_frame.display_login_error()

    def show_frame(self, frame):
        frame.pack(fill="both", expand=True)
        frame.tkraise()