import customtkinter
from logic.database import DatabaseManager

class PredictionView(customtkinter.CTkFrame):
    def __init__(self, parent, db):
        super().__init__(parent)

        self.db = db

        self.title = customtkinter.CTkLabel(self, text = "Race Predictions", font = ("Arial", 20, "bold"))
        self.title.pack(pady = 20)

        self.grid_frame = customtkinter.CTkFrame(self)
        self.grid_frame.pack(fill = "both", expand = True, padx = 20, pady = 10)

        distances = ["5k", "10k", "Half Marathon", "Marathon"]
        self.time_labels = {}
        self.prediction_labels = {}

        headers = ["Distance", "Current Time", "Predicted Time"]

        for col_index, header_text in enumerate(headers):
            header_label = customtkinter.CTkLabel(self.grid_frame, text = header_text, font = ("Arial", 12, "bold"))
            header_label.grid(row = 0, column = col_index, padx = 10, pady = 10)

        
        for i, distance in enumerate(distances, start = 1):
            
            current_label = customtkinter.CTkLabel(self.grid_frame, text = distance)
            current_label.grid(row = i, column = 0, padx = 10, pady = 10, sticky = "w")

            current_time_label = customtkinter.CTkLabel(self.grid_frame, text = "--:--:--")
            current_time_label.grid(row = i, column = 1, padx = 10, pady = 10, sticky = "w")
            self.time_labels[distance] = current_time_label

            current_predict_label = customtkinter.CTkLabel(self.grid_frame, text = "--:--:--")
            current_predict_label.grid(row = i, column = 2, padx = 10, pady = 10, sticky = "w")
            self.prediction_labels[distance] = current_predict_label



