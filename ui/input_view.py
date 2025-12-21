import customtkinter
from logic.database import DatabaseManager

run_types = ["Easy", "Speed", "Long"]

class InputView(customtkinter.CTkFrame):
    def __init__(self, parent, history):
        super().__init__(parent)

        self.db = DatabaseManager()
        self.history = history

        #handling section for field "Type"

        self.type_selector = customtkinter.CTkOptionMenu(self, values = run_types)
        self.type_selector.pack(pady = 10)

        #handling section for field "Distance"

        self.distance_entry = customtkinter.CTkEntry(self, placeholder_text = "Distance (km)")
        self.distance_entry.pack(pady = 10)

        #handling section for field "Time"

        self.time_entry = customtkinter.CTkEntry(self, placeholder_text = "Time (hh:mm:ss)")
        self.time_entry.pack(pady = 10)

        #handling section for field "Pace"

        self.pace_entry = customtkinter.CTkEntry(self, placeholder_text = "Pace (mm:ss) / km")
        self.pace_entry.pack(pady = 10)

        save_button = customtkinter.CTkButton(self, text = "Save Run", command = self.save_run)
        save_button.pack(pady = 10)

    def save_run(self):
        type = self.type_selector.get()
        dist = self.distance_entry.get()
        time = self.time_entry.get()
        pace = self.pace_entry.get()

        dot_count_time = time.count(":")
        dot_count_pace = pace.count(":")

        if dot_count_time > 2 or dot_count_time == 0 or dot_count_pace != 1:
            print("Error: Time or pace format incorect")

        elif type == "" or dist == "" or time == "" or pace == "":
            print("Error: Please fill in all fields")

        else:
            try:
                dist = float(dist)
                time = self.db.convert_to_seconds(time)
                pace = self.db.convert_to_seconds(pace)

                self.db.add_run(type, dist, time, pace)

                self.type_selector.set("Easy")
                self.distance_entry.delete(0, 'end')
                self.time_entry.delete(0, 'end')
                self.pace_entry.delete(0, 'end')

                self.history.load_data()
            except ValueError:
                print("Distance, time or pace is not a number")
            
            


