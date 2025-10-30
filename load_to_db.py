import os
import pandas as pd
from sqlconnect import get_connection

def load_data_to_db():
    cleaned_file = os.path.join("Data", "Activity_cleaned.csv")
    df = pd.read_csv(cleaned_file)

    dtype = {
        "UserID": "INTEGER",
        "Date": "TEXT",
        "Total_Distance": "REAL",
        "Tracker_Distance": "REAL",
        "Logged_Activities_Distance": "REAL",
        "Very_Active_Distance": "REAL",
        "Moderately_Active_Distance": "REAL",
        "Light_Active_Distance": "REAL",
        "Sedentary_Active_Distance": "REAL",
        "Very_Active_Minutes": "INTEGER",
        "Fairly_Active_Minutes": "INTEGER",
        "Lightly_Active_Minutes": "INTEGER",
        "Sedentary_Minutes": "INTEGER",
        "Steps": "INTEGER",
        "Calories_Burned": "INTEGER"
    }

    conn = get_connection()
    df.to_sql("fitness_data", conn, if_exists="replace", index=False, dtype=dtype)
    conn.close()

    print("Cleaned data saved to SQLite DB at Data/fitness_data.db")

if __name__ == "__main__":
    load_data_to_db()
