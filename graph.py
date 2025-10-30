import plotly.graph_objects as go
import plotly.express as px
from query import (
    get_total_steps_per_user,
    get_avg_calories_per_day,
    get_top_users_by_calories,
    get_user_daily_activity
)

def plot_total_steps_per_user():
    df = get_total_steps_per_user()
    if df.empty:
        return None
    fig = px.bar(
        df,
        x="UserID",
        y="Total_Steps",
        color="Total_Steps",
        color_continuous_scale="Blues",
        title="Total Steps per User"
    )
    fig.update_layout(
        template="plotly_dark",
        xaxis_title="User ID",
        yaxis_title="Total Steps",
        margin=dict(l=40, r=40, t=60, b=40)
    )
    return fig

def plot_avg_calories_per_day():
    df = get_avg_calories_per_day()
    if df.empty:
        return None
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Date"],
        y=df["Avg_Calories"],
        mode="lines+markers",
        line=dict(color="orange", width=3),
        name="Average Calories"
    ))
    fig.update_layout(
        title="Average Calories Burned per Day",
        xaxis_title="Date",
        yaxis_title="Average Calories",
        template="plotly_dark",
        margin=dict(l=40, r=40, t=60, b=40)
    )
    return fig

def plot_top_users_by_calories(n=5):
    df = get_top_users_by_calories(n)
    if df.empty:
        return None
    fig = px.bar(
        df,
        x="UserID",
        y="Total_Calories",
        color="Total_Calories",
        color_continuous_scale="Greens",
        title=f"Top {n} Users by Total Calories Burned"
    )
    fig.update_layout(
        template="plotly_dark",
        xaxis_title="User ID",
        yaxis_title="Total Calories Burned",
        margin=dict(l=40, r=40, t=60, b=40)
    )
    return fig

def plot_user_daily_activity(user_id):
    df = get_user_daily_activity(user_id)
    if df.empty:
        return None
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["Date"],
        y=df["Steps"],
        mode="lines+markers",
        line=dict(color="royalblue", width=2),
        name="Steps"
    ))
    fig.add_trace(go.Scatter(
        x=df["Date"],
        y=df["Calories_Burned"],
        mode="lines+markers",
        line=dict(color="crimson", width=2),
        name="Calories Burned"
    ))
    fig.update_layout(
        title=f"Daily Activity for User {user_id}",
        xaxis_title="Date",
        yaxis_title="Value",
        template="plotly_dark",
        legend_title="Metrics",
        margin=dict(l=40, r=40, t=60, b=40)
    )
    return fig
