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
        
        self.update_predictions()
    
    def update_predictions(self):
        distance_map = {
            "5k": 5.0,
            "10k": 10.0,
            "Half Marathon": 21.0975,
            "Marathon": 42.195
        }

        base_seconds = self.db.latest_run_by_distance(5.0)

        for label_text, km_dist in distance_map.items():

            if base_seconds:
                predicted_seconds = base_seconds * (km_dist / 5.0) ** 1.06

                time_str = self.db.format_reverse_seconds(int(predicted_seconds))
            else:
                time_str = "--:--:--"
            
            if label_text in self.time_labels:
                self.time_labels[label_text].configure(text = time_str)
            
            



