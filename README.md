# RunSmart 🏃‍♂️‍➡️
My very own running app  
I tought this will be fun, to just generate my own workouts here

## Description

This is a Running desktop app that analyzes your workouts and gives you a prediction of the race times for specific popular distances (5k, 10k, Half Marathon, Marathon). 
It uses the following key concepts and mechanisms: 
- Stores every "User input" workout into a database, which can be visualized
- Predicts a race time based on your past workouts
- Generates a training plan for X weeks with user preferences -> that way it makes uniqe plans for every user
- The predictions are made using Basic ML algorithms (Logistic Regression, Clustering). It basically focuses only on "hard" sessions that are "converted" into a specific 5k time that let's the algorithm to show progress over the weeks

## How to run
- First of all make sure you have a `venv` installed in the main folder. If not just create one by writting to terminal: `$ python3 -m venv <name_of_venv>`. For activation use `$ source venv/bin/activate` and to deactivate just type `$ deactivate`
- Once you activate your `venv`, you have to just run the `main.py` file in the main folder (the app should open)
- Explore the app and enjoy

## Current implementations (what we have)

- a working input window that resets after filling the boxes (with `customtkinter`)
- a database connection via `sqlite3`
- updated with error handling for DB input (format or empty) [20 Dec 2025]
- added running history tab for viewing all the workout history [21 dec 2025]
- added auto-refreshing database (without restarting the app to see the new workouts) [21 dec 2025]
- formated the RunHistory tabel so it's more organized and also converted the time and pace to user friendly format [21 dec 2025]
- added the predictions tab without the times (the prediction logic will be implemented) [21 dec 2025]
- implemented the "Current Time" column based on the latest 5k time in the Workout Database [31 dec 2025]
- implemented Scrollable tabs for each training week (with navigation buttons between the weeks) + run cell creating [31 dec 2025]
- first tests of "ML engine" for predicting race times, only focusing on the threshold (true speed sessions) [3 jan 2026]
- still to work on the dataset analysis and prediction (it improves the times to fast) [3 jan 2026]

* So on short, we have a database for workouts, a history of workouts, a predictions tab (without the prediction logic), refreshing the database

## To implement the next session:

- error handling for any error appears in my head randomly :)
- error handling for predictions (optimizations on the model)
- logic for plan generation (partition on training phases)
- implement the prediction logic (current progress to the training plan)