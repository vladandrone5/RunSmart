import sqlite3

# table field legend:
# type = run type (Speed, Easy, Long)
# distance = distance in Km
# time = time of the activity in seconds
# pace = the pace converted in seconds


class DatabaseManager:
    def __init__(self):
        self.con = sqlite3.connect("data/run_history.db") # connecting the db to the program
        self.create_table()

    def create_table(self):
        curs = self.con.cursor()
        curs.execute("CREATE TABLE IF NOT EXISTS Run(type TEXT, distance REAL, time INTEGER, pace INTEGER)")

    def add_run(self, type, dist, time, pace): # add and save to DB
        curs = self.con.cursor()

        curs.execute("INSERT INTO Run (type, distance, time, pace) VALUES (?, ?, ?, ?)", (type, dist, time, pace))

        self.con.commit()
    
    def convert_to_seconds(self, time_str):
        time_stamp = time_str.split(":")
    
        length = len(time_stamp)

        if length == 3: # if it's for Time field
            h = int(time_stamp[0])
            m = int(time_stamp[1])
            s = int(time_stamp[2])
            total_time = 3600 * h + 60 * m + s
        else: # if it's for Pace field
            m = int(time_stamp[0])
            s = int(time_stamp[1])
            total_time = 60 * m + s

        return total_time



