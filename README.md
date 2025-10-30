🏋️ Fitness Tracker Dashboard

A complete ETL + Machine Learning + Dashboard project that processes fitness tracking data, predicts calories burned, and visualizes user activity with interactive charts.

Built using Python, Streamlit, SQLite, Plotly, and Scikit-Learn.

📁 Project Structure
Fitness_Track_Dashboard/
│
├── 📂 Data/
│   ├── Activity.csv                # Raw fitness dataset
│   ├── Activity_cleaned.csv        # Cleaned data after preprocessing
│   ├── fitness_data.db             # SQLite database storing cleaned records
│   └── calorie_predictor.pkl       # Trained ML model (optional)
│
├── 📂 Src/
│   ├── data_cleaning.py            # Handles data preprocessing & cleaning
│   ├── data_load.py                # Loads and inspects dataset
│   ├── load_to_db.py               # Loads cleaned data into SQLite DB
│   ├── sqlconnect.py               # Database connection utility
│   ├── query.py                    # SQL queries for data aggregation
│   ├── graph.py                    # Visualization functions (Plotly)
│   ├── ml.py                       # Machine Learning model (Calorie Prediction)
│   └── main.py                     # Streamlit Dashboard UI
│
├── .gitignore
└── README.md

⚙️ Features

ETL Pipeline

Cleans and transforms raw fitness tracking data (Activity.csv).

Loads cleaned data into a local SQLite database.

Data Analytics

Aggregates steps, calories, and distances per user.

Identifies top-performing users and daily trends.

Machine Learning

Trains a regression model to predict calories burned using distance, steps, and activity time.

Interactive Dashboard

Built in Streamlit with Plotly visualizations.

Displays real-time graphs and calorie predictions.

🧠 Tech Stack
Category	Tools Used
Language	Python
Data Processing	Pandas, NumPy
Database	SQLite
Visualization	Plotly, Streamlit
Machine Learning	Scikit-learn
Environment	Conda / Virtualenv
🚀 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/Fitness_Track_Dashboard.git
cd Fitness_Track_Dashboard

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run ETL Pipeline
cd Src
python data_cleaning.py
python load_to_db.py

4️⃣ Train the Model
python ml.py

5️⃣ Launch the Dashboard
streamlit run main.py


Then open your browser at:

http://localhost:8501

📊 Dashboard Highlights

Total Steps per User

Average Calories Burned per Day

Top Users by Total Calories

User-Specific Activity Trends

Calorie Prediction Model

🧩 Example Outputs
Graph	Description

	Total Steps per User

	Average Calories per Day

	Predicted Calories Burned
