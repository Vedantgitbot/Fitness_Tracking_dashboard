from data_load import load_raw_data
import pandas as pd

def clean_data(filepath):
    df = load_raw_data(filepath)

    df.columns = [
        "UserID", "Date", "Total_Distance", "Tracker_Distance",
        "Logged_Activities_Distance", "Very_Active_Distance",
        "Moderately_Active_Distance", "Light_Active_Distance",
        "Sedentary_Active_Distance", "Very_Active_Minutes",
        "Fairly_Active_Minutes", "Lightly_Active_Minutes",
        "Sedentary_Minutes", "Steps", "Calories_Burned"
    ]

    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    df = df.drop_duplicates(subset=["UserID", "Date"], keep="last")
    df = df.dropna(subset=["UserID", "Date"])

    print(f"Cleaned data: {df.shape[0]} rows")
    return df


if __name__ == "__main__":
    cleaned_df = clean_data("Data/Activity.csv")
    cleaned_df.to_csv("Data/Activity_cleaned.csv", index=False)
    print("🎉 Saved cleaned file to Data/Activity_cleaned.csv")

