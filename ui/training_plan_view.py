import customtkinter

class TrainingPlanView(customtkinter.CtkScrollableFrame):
    def __init__(self, parent, db):
        super().__init__(parent)
        self.db = db


        self.title_label = customtkinter.CTkLabel(self, text = "Current Training Week: 1", font = ("Arial", 20, "bold"))
        self.title_label.pack(pady = 20)

        self.schedule_frame = customtkinter.CTkFrame(self)
        self.schedule_frame.pack(fill = "both", expand = True, padx = 20)

        self.setup_headers()
    
    def setup_headers(self):
        
        headers = ["Day", "Planned Activity", "Status"]

        for i, header in enumerate(headers):
            lbl = customtkinter.CTkLabel(self.schedule_frame, text = header, font = ("Arial", 12, "bold"))
            lbl.grid(row = 0, column = i, padx = 20, pady = 19)