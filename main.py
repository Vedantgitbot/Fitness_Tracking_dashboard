import streamlit as st
from graph import (
    plot_total_steps_per_user,
    plot_avg_calories_per_day,
    plot_top_users_by_calories,
    plot_user_daily_activity
)
from ml import predict_calories

st.set_page_config(page_title="Fitness Tracker Dashboard", layout="wide")
st.title("Fitness Tracker Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Total Steps per User")
    fig1 = plot_total_steps_per_user()
    if fig1:
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.info("No data available.")

with col2:
    st.subheader("Average Calories per Day")
    fig2 = plot_avg_calories_per_day()
    if fig2:
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.info("No data available.")

with col3:
    st.subheader("Top Users by Calories")
    fig3 = plot_top_users_by_calories(5)
    if fig3:
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.info("No data available.")

st.markdown("---")

st.subheader("User Daily Activity")
user_id = st.number_input("Enter User ID", min_value=1, step=1)
if st.button("Show Activity"):
    fig4 = plot_user_daily_activity(user_id)
    if fig4:
        st.plotly_chart(fig4, use_container_width=True)
    else:
        st.warning("No data found for the given user ID.")

st.markdown("---")

st.subheader("Predict Calories Burned")
with st.form("prediction_form"):
    total_distance = st.number_input("Total Distance (km)", value=5.0, step=0.1)
    tracker_distance = st.number_input("Tracker Distance (km)", value=5.0, step=0.1)
    very_active_distance = st.number_input("Very Active Distance (km)", value=1.0, step=0.1)
    moderately_active_distance = st.number_input("Moderately Active Distance (km)", value=2.0, step=0.1)
    light_active_distance = st.number_input("Light Active Distance (km)", value=1.5, step=0.1)
    very_active_minutes = st.number_input("Very Active Minutes", value=30)
    fairly_active_minutes = st.number_input("Fairly Active Minutes", value=45)
    lightly_active_minutes = st.number_input("Lightly Active Minutes", value=90)
    sedentary_minutes = st.number_input("Sedentary Minutes", value=500)
    steps = st.number_input("Steps", value=8000)
    submitted = st.form_submit_button("Predict")

if submitted:
    sample = {
        "Total_Distance": total_distance,
        "Tracker_Distance": tracker_distance,
        "Very_Active_Distance": very_active_distance,
        "Moderately_Active_Distance": moderately_active_distance,
        "Light_Active_Distance": light_active_distance,
        "Very_Active_Minutes": very_active_minutes,
        "Fairly_Active_Minutes": fairly_active_minutes,
        "Lightly_Active_Minutes": lightly_active_minutes,
        "Sedentary_Minutes": sedentary_minutes,
        "Steps": steps
    }
    prediction = predict_calories(sample)
    st.metric(label="Estimated Calories Burned", value=f"{prediction} kcal")
