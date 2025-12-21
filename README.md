# RunSmart 🏃‍♂️‍➡️
My very own running app  
I tought this will be fun, to just generate my own workouts here

## Current implementations (what we have)

- a working input window that resets after filling the boxes (with `customtkinter`)
- a database connection via `sqlite3`
- updated with error handling for DB input (format or empty) [20 Dec 2025]
- added running history tab for viewing all the workout history [21 dec 2025]
- added auto-refreshing database (without restarting the app to see the new workouts) [21 dec 2025]
- formated the RunHistory tabel so it's more organized and also converted the time and pace to user friendly format [21 dec 2025]
- added the predictions tab without the times (the prediction logic will be implemented) [21 dec 2025]

* So on short, we have a database for workouts, a history of workouts, a predictions tab (without the prediction logic), refreshing the database

## To implement the next session:

- error handling for any error appears in my head randomly :)
- implement the prediction logic (based on saved workouts / current progress to the training plan)