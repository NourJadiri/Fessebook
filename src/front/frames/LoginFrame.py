import customtkinter as ctk
from src.services import Service

sc = Service()

class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, callback, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.pack(fill="both", expand=True)

        self.title = ctk.CTkLabel(master=self, text="Login", font=("Helvetica", 32, "bold"))
        self.title.grid(row=0, column=0, pady=20)

        self.login_frame = ctk.CTkFrame(master=self, corner_radius=20, border_width=2, border_color='pink')
        self.login_frame.grid_columnconfigure(0, weight=1)
        self.login_frame.grid_rowconfigure(0, weight=1)
        self.login_frame.grid(row=1, column=0, padx=50, pady=20, sticky='nsew')

        self.login_label = ctk.CTkLabel(master=self.login_frame, text="Login", font=("Helvetica", 14, "bold"))
        self.login_label.grid(row=0, column=0)

        self.login_entry = ctk.CTkEntry(master=self.login_frame, width=200, height=30)
        self.login_entry.grid(row=1, column=0, padx=10, pady=(0, 10))

        self.password_label = ctk.CTkLabel(master=self.login_frame, text="Password", font=("Helvetica", 14, "bold"))
        self.password_label.grid(row=2, column=0, pady=(10, 0))

        self.password_entry = ctk.CTkEntry(master=self.login_frame, width=200, height=30, show='*')
        self.password_entry.grid(row=3, column=0, padx=10, pady=(0, 10))

        self.login_button = ctk.CTkButton(master=self.login_frame, text="Login", height=30, command=callback)
        self.login_button.grid(row=5, column=0, pady=(50, 20), padx=20, sticky='ew')

    def display_login_error(self):
        self.login_error = ctk.CTkLabel(master=self.login_frame, text="Nom d'utilisateur ou mot de passe incorrect",
                                        text_color='red', wraplength=self.login_frame.winfo_width() - 10)
        self.login_error.grid(row=4, column=0, pady=10, padx=10)
