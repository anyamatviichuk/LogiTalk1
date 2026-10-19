from customtkinter import *

class Dodatok(CTk):
   def __init__(self):
        super().__init__()
        self.geometry('600x400')
        self.title("Logitalk")


        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        self.is_show_menu = False


        self.menu_frame = CTkFrame(self, width=40)
        self.menu_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.menu_frame.grid_propagate(False)


        self.btn = CTkButton(self.menu_frame, text='▶️', command=self.toggle_menu, width=30)
        self.btn.pack(anchor="nw", padx=5, pady=5)


        self.menu_content = CTkFrame(self.menu_frame, fg_color="transparent")
        CTkLabel(self.menu_content, text='Імʼя').pack(pady=(10, 5))
        CTkEntry(self.menu_content).pack(padx=10)


        self.chat_field = CTkScrollableFrame(self)
        self.chat_field.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")


        self.input_frame = CTkFrame(self, fg_color="#622648")
        self.input_frame.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="ew")
        self.input_frame.grid_columnconfigure(0, weight=1)

        self.message_entry = CTkEntry(self.input_frame, placeholder_text='Введіть повідомлення:', height=40)
        self.message_entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))

        self.send_button = CTkButton(self.input_frame, text='>', width=50, height=40, fg_color ="#e0b0ff", hover_color="#622648")
        self.send_button.grid(row=0, column=1)


    def toggle_menu(self):
        if self.is_show_menu:
            self.menu_frame.configure(width=40)
            self.btn.configure(text='▶️')
            self.is_show_menu = False
        else:

            self.menu_frame.configure(width=200)
            self.menu_content.pack(fill="both", expand=True, pady=10)
            self.btn.configure(text='◀️')
            self.is_show_menu = True

win = Dodatok()
win.mainloop()




