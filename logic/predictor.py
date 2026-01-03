import numpy as np
from sklearn.linear_model import LinearRegression

class RacePredictor:
    def __init__(self, db_manager):
        self.db = db_manager

    def predict_future_race_time(self, weeks_in_future=8):
        # 1. Fetch data
        runs = self.db.get_all_runs_with_id()
        
        print(f"\n--- ML DEBUG START ---")
        if len(runs) < 3:
            return None

        # --- STEP 1: Smart Filtering (The Fix) ---
        # We separate runs into 'valid' and 'invalid' BEFORE calculating stats.
        valid_runs = []
        
        for run in runs:
            distance_km = run[2]
            # Only consider runs longer than 2km as "Real Efforts" for the baseline
            if distance_km >= 2.0:
                valid_runs.append(run)

        if not valid_runs:
            print("No runs > 2.0km found.")
            return None

        # --- STEP 2: Calculate Baseline from VALID runs only ---
        # Now the 'Best Pace' will be your Marathon (4:17), not a short sprint.
        valid_paces = [r[4] for r in valid_runs]
        current_best_pace = min(valid_paces) 
        threshold = current_best_pace * 1.3 # Threshold is now realistic (e.g., 4:17 * 1.3 = ~5:34)

        print(f"Realistic Best Pace: {current_best_pace} sec/km")
        print(f"Filter Threshold: {threshold} sec/km")

        # --- STEP 3: Build the Training Set ---
        X = []
        y = []

        for run in valid_runs: # We iterate only through the valid list
            run_id = run[0]
            distance_km = run[2]
            time_sec = run[3]
            pace = run[4]

            # Now we apply the threshold
            if pace <= threshold:
                # Normalize
                equiv_5k = time_sec * (5.0 / distance_km) ** 1.06
                norm_pace = equiv_5k / 5.0
                
                X.append([run_id])
                y.append(norm_pace)
                print(f"Run {run_id} ({distance_km}km @ {pace}s/km): KEPT")
            else:
                print(f"Run {run_id} ({distance_km}km @ {pace}s/km): SKIP (Too Slow)")

        if len(X) < 2:
            print("Not enough valid runs after filtering.")
            return None

        # 4. Train
        model = LinearRegression()
        model.fit(X, y)

        # 5. Predict
        last_run_id = runs[-1][0]
        future_id = last_run_id + (weeks_in_future * 3)
        predicted_pace = model.predict([[future_id]])[0]
        
        # Sanity Clamp
        best_normalized = min(y)
        
        if predicted_pace >= best_normalized:
            print("Force improvement (3%)")
            return best_normalized * 0.97

        return predicted_pace