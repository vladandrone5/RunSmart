import customtkinter

class TrainingPlanView(customtkinter.CTkFrame):
    def __init__(self, parent, db):
        super().__init__(parent)

        self.db = db

        self.current_week = 1
        self.total_weeks = 8
        self.training_plan = {}

        self.day_containers = {}

        self.header_frame = customtkinter.CTkFrame(self, fg_color = "transparent")
        self.header_frame.pack(fill = "x", pady = (20, 10), padx = 20)

        #previous week button (<)
        self.prev_btn = customtkinter.CTkButton(
            self.header_frame, text = "<", width = 40, command = lambda: self.change_week(-1)
        )
        self.prev_btn.pack(side = "left")

        # Title label (Week X)
        self.title_label = customtkinter.CTkLabel(
            self.header_frame,
            text = "Week 1",
            font = ("Arial", 22, "bold"),
            anchor = "w"
        )
        self.title_label.pack(side = "left")


        self.next_btn = customtkinter.CTkButton(
            self.header_frame, text = ">", width = 40, command = lambda: self.change_week(1)
        )
        self.next_btn.pack(side = "left")

        self.schedule_container = customtkinter.CTkScrollableFrame(self, fg_color = "transparent")
        self.schedule_container.pack(fill = "both", expand = True, padx = 20, pady = 10)

        self.setup_week_skeleton()

        self.refresh_view()
    
    def setup_week_skeleton(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

        self.add_separator()

        for day in days:

            row_frame = customtkinter.CTkFrame(self.schedule_container, fg_color = "transparent")
            row_frame.pack(fill = "x", expand = False)

            day_label = customtkinter.CTkLabel(
                row_frame,
                text = day,
                font = ("Arial", 16),
                width = 120,
                anchor = "w"
            )
            day_label.pack(side = "left", padx = (0, 10), pady = 15)

            content_placeholder = customtkinter.CTkFrame(row_frame, fg_color = "transparent")
            content_placeholder.pack(side = "left", fill = "both", expand = True)

            self.day_containers[day] = content_placeholder

            self.add_separator()
    
    def add_separator(self):
        sep = customtkinter.CTkFrame(self.schedule_container, height = 2, fg_color = ("gray70", "gray30"))
        sep.pack(fill = "x")
    
    def change_week(self, direction):
        new_week = self.current_week + direction

        if 1 <= new_week <= self.total_weeks:
            self.current_week = new_week
            self.refresh_view()
    
    def refresh_view(self):

        self.title_label.configure(text = f"Week {self.current_week}")

        for day, container in self.day_containers.items():
            for widget in container.winfo_children():
                widget.destroy()
        
        week_data = self.training_plan.get(self.current_week)

        if week_data:
            for day_name, run_info in week_data.items():
                if day_name in self.day_containers:
                    self.create_run_cell(
                        self.day_containers[day_name],
                        run_info["type"],
                        run_info["dist"]
                    )


    def create_run_cell(self, parent_widget, run_type, distance):

        cell_frame = customtkinter.CTkFrame(
            parent_widget,
            border_width = 2,
            border_color = ("gray50", "gray70"),
            fg_color = ("gray90", "gray20")
        )

        cell_frame.pack(side = "left", pady = 5, anchor = "w")

        run_text = f"{run_type} - {distance}km"
        cell_label = customtkinter.CTkLabel(
            cell_frame,
            text = run_text,
            font = ("Arial", 14, "bold"),
            padx = 15,
            pady = 8
        )
        cell_label.pack()


    def load_dummy_plan(self):

        dummy_schedule = {
            "Monday": {"type": "Easy Run", "dist": 5.0},
            "Wednesday": {"type": "Intervals", "dist": 8.0},
            "Friday": {"type": "Tempo Run", "dist": 7.0},
            "Sunday": {"type": "Long Run", "dist": 15.0}
        }

        print("load dummy schedule")

        for day_name, run_data in dummy_schedule.items():
            target_container = self.day_containers.get(day_name)

            if target_container:
                self.create_run_cell(
                    target_container,
                    run_data["type"],
                    run_data["dist"]
                )