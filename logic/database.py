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

    def format_reverse_seconds(self, seconds): # transforms the seconds format back to hh:mm:ss
        total_minutes, final_seconds = divmod(seconds, 60)

        hours, final_minutes = divmod(total_minutes, 60)

        if hours == 0:
            return f"{final_minutes:02d}:{final_seconds:02d}"
        else:
            return f"{hours:02d}:{final_minutes:02d}:{final_seconds:02d}"


    def get_all_runs(self):
        curs = self.con.cursor()
        curs.execute("SELECT * FROM Run")

        return curs.fetchall()
    
    def get_all_runs_with_id(self):
        curs = self.con.cursor()

        curs.execute("SELECT rowid, type, distance, time, pace FROM Run")

        return curs.fetchall()

    def latest_run_by_distance(self, target_distance):
        curs = self.con.cursor()

        curs.execute("""
            SELECT time
            FROM Run
            WHERE distance = ?
            ORDER BY rowid DESC
            LIMIT 1
        """, (target_distance,))

        result = curs.fetchone()

        if result:
            return result[0]
        return None
    



