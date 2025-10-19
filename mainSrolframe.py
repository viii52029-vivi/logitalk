from customtkinter import *


# -------------------- Вікно входу --------------------
class LoginWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title("LogiTalk - Вхід")
        self.geometry("300x200")

        self.label = CTkLabel(self, text="Введіть ім'я користувача:")
        self.label.pack(pady=20)

        self.username_entry = CTkEntry(self, placeholder_text="Ваш нікнейм")
        self.username_entry.pack(pady=10)

        self.login_button = CTkButton(self, text="Увійти", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        if username.strip():
            self.destroy()
            app = LogiTalk(username)
            app.mainloop()


# -------------------- Головне вікно чату --------------------
class LogiTalk(CTk):
    def __init__(self, username):
        super().__init__()
        self.title("LogiTalk - Чат")
        self.geometry("500x400")

        self.username = username
        self.is_menu_visible = False

        # Поле для виводу повідомлень
        self.chat_box = CTkTextbox(self, width=460, height=250, state="disabled")
        self.chat_box.place(x=20, y=20)

        # Поле введення повідомлення
        self.message_entry = CTkEntry(self, placeholder_text="Введіть повідомлення...", width=350, height=40)
        self.message_entry.place(x=20, y=300)

        # Кнопка відправки
        self.send_button = CTkButton(self, text="Надіслати", width=80, command=self.send_message)
        self.send_button.place(x=380, y=300)

        # Бокове меню
        self.menu_frame = CTkFrame(self, width=120, height=400)
        self.menu_frame.place(x=-120, y=0)  # сховане зліва

        self.menu_label = CTkLabel(self.menu_frame, text="⚙ Налаштування")
        self.menu_label.pack(pady=20)

        self.menu_button = CTkButton(self, text="▶️", width=40, command=self.toggle_menu)
        self.menu_button.place(x=10, y=360)

    # Відправка повідомлення
    def send_message(self):
        message = self.message_entry.get()
        if message.strip():
            self.chat_box.configure(state="normal")
            self.chat_box.insert("end", f"{self.username}: {message}\n")
            self.chat_box.configure(state="disabled")
            self.chat_box.see("end")
            self.message_entry.delete(0, "end")

    # Перемикач бокового меню
    def toggle_menu(self):
        if self.is_menu_visible:
            self.menu_frame.place(x=-120, y=0)
            self.is_menu_visible = False
        else:
            self.menu_frame.place(x=0, y=0)
            self.is_menu_visible = True


# -------------------- Запуск --------------------
if __name__ == "__main__":
    login = LoginWindow()
    login.mainloop()
