import customtkinter
from ui.input_view import InputView

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("RunSmart")
        self.geometry("800x600")

        self.view = InputView(self)
        self.view.pack(expand = True, fill = "both")


if __name__ == "__main__":
    app = App()
    app.mainloop()

