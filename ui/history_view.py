import customtkinter
from logic.database import DatabaseManager

class RunHistory(customtkinter.CTkScrollableFrame):
    def __init__(self, master, db):
        super().__init__(master)

        self.db = db

        self.title_label = customtkinter.CTkLabel(self, text = "Run History", font = ("Arial", 24, "bold"))
        self.title_label.pack(pady = 10)

        self.load_data()
    

    def load_data(self):

        for child in self.winfo_children():
            child.destroy()
        
        header_type = customtkinter.CTkLabel(self, text = "Type", font = ("Arial", 12, "bold"))
        header_type.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "w")

        header_distance = customtkinter.CTkLabel(self, text = "Distance (km)", font = ("Arial", 12, "bold"))
        header_distance.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = "w")

        header_time = customtkinter.CTkLabel(self, text = "Time", font = ("Arial", 12, "bold"))
        header_time.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = "w")

        header_pace = customtkinter.CTkLabel(self, text = "Pace", font = ("Arial", 12, "bold"))
        header_pace.grid(row = 0, column = 3, padx = 10, pady = 5, sticky = "w")

        runs = self.db.get_all_runs()

        for i, (run_type, dist, time, pace) in enumerate(runs):
            current_row = i + 1

            readable_time = self.db.format_reverse_seconds(time)
            readable_pace = self.db.format_reverse_seconds(pace)

            # Run type label
            type_label = customtkinter.CTkLabel(self, text = run_type)
            type_label.grid(row = current_row, column = 0, padx = 10, pady = 2, sticky = "w")

            # Distance label
            dist_label = customtkinter.CTkLabel(self, text = f"{dist} km")
            dist_label.grid(row = current_row, column = 1, padx = 10, pady = 2, sticky = "w")

            # Time label
            time_label = customtkinter.CTkLabel(self, text = f"{readable_time}")
            time_label.grid(row = current_row, column = 2, padx = 10, pady = 2, sticky = "w")

            # Pace label
            pace_label = customtkinter.CTkLabel(self, text = f"{readable_pace}/km")
            pace_label.grid(row = current_row, column = 3, padx = 10, pady = 2, sticky = "w")



        