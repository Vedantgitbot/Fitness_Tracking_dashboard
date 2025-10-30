import pandas as pd
from sqlconnect import get_connection

def get_total_steps_per_user():
    """Return total steps taken per user."""
    query = """
    SELECT UserID, SUM(Steps) AS Total_Steps
    FROM fitness_data
    GROUP BY UserID
    ORDER BY Total_Steps DESC;
    """
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def get_avg_calories_per_day():
    """Return average calories burned per day across all users."""
    query = """
    SELECT Date, AVG(Calories_Burned) AS Avg_Calories
    FROM fitness_data
    GROUP BY Date
    ORDER BY Date;
    """
    conn = get_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


def get_user_daily_activity(user_id):
    """Return daily activity data for a specific user."""
    query = """
    SELECT Date, Steps, Total_Distance, Calories_Burned
    FROM fitness_data
    WHERE UserID = ?
    ORDER BY Date;
    """
    conn = get_connection()
    df = pd.read_sql_query(query, conn, params=(user_id,))
    conn.close()
    return df


def get_top_users_by_calories(n=5):
    """Return top N users by total calories burned."""
    query = """
    SELECT UserID, SUM(Calories_Burned) AS Total_Calories
    FROM fitness_data
    GROUP BY UserID
    ORDER BY Total_Calories DESC
    LIMIT ?;
    """
    conn = get_connection()
    df = pd.read_sql_query(query, conn, params=(n,))
    conn.close()
    return df


if __name__ == "__main__":
    print("Total Steps per User:")
    print(get_total_steps_per_user().head())

    print("\nAverage Calories per Day:")
    print(get_avg_calories_per_day().head())

    print("\nUser Daily Activity (UserID=1):")
    print(get_user_daily_activity(1).head())

    print("\nTop 5 Users by Calories:")
    print(get_top_users_by_calories(5))
