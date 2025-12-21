import customtkinter
from ui.input_view import InputView
from ui.history_view import RunHistory
from logic.database import DatabaseManager
from ui.prediction_view import PredictionView

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("RunSmart")
        self.geometry("800x600")

        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.pack(fill = "both", expand = True)

        db = DatabaseManager()

        self.tabview.add("Add Run")
        self.tabview.add("History")
        self.tabview.add("Predictions")
        
        self.history = RunHistory(self.tabview.tab("History"), db)
        self.history.pack(expand = True, fill = "both")

        self.target_predictions = PredictionView(self.tabview.tab("Predictions"), db)
        self.target_predictions.pack(expand = True, fill = "both")

        self.view = InputView(self.tabview.tab("Add Run"), self.history)
        self.view.pack(expand = True, fill = "both")


        self.quit_button = customtkinter.CTkButton(self, text = "Exit App", command = self.destroy)
        self.quit_button.place(relx = 0.02, rely = 0.95, anchor = "sw")



if __name__ == "__main__":
    app = App()
    app.mainloop()

