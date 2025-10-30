import sqlite3
import os

def get_connection():
    """Create and return a SQLite database connection."""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, "Data", "fitness_data.db")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    return sqlite3.connect(db_path)
