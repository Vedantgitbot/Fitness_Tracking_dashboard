import pandas as pd
import sqlite3
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Data/fitness_data.db"))

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM fitness_data;", conn)
    conn.close()
    return df

def train_model():
    df = load_data()
    df = df.dropna()

    X = df[[
        "Total_Distance", "Tracker_Distance", "Very_Active_Distance",
        "Moderately_Active_Distance", "Light_Active_Distance",
        "Very_Active_Minutes", "Fairly_Active_Minutes",
        "Lightly_Active_Minutes", "Sedentary_Minutes", "Steps"
    ]]
    y = df["Calories_Burned"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Model trained successfully")
    print(f"Mean Absolute Error: {mae:.2f}")
    print(f"R² Score: {r2:.3f}")

    model_path = os.path.join(os.path.dirname(__file__), "../Data/calorie_predictor.pkl")
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

def predict_calories(input_data):
    model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../Data/calorie_predictor.pkl"))
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model not found. Please run train_model() first.")

    model = joblib.load(model_path)
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    return round(prediction, 2)

if __name__ == "__main__":
    train_model()
    sample = {
        "Total_Distance": 5.2,
        "Tracker_Distance": 5.1,
        "Very_Active_Distance": 1.3,
        "Moderately_Active_Distance": 2.5,
        "Light_Active_Distance": 1.4,
        "Very_Active_Minutes": 25,
        "Fairly_Active_Minutes": 40,
        "Lightly_Active_Minutes": 90,
        "Sedentary_Minutes": 500,
        "Steps": 9500
    }
    predicted = predict_calories(sample)
    print(f"Predicted Calories Burned: {predicted}")
