# utils/db_manager.py
"""
This file sets up a simple SQLite database to store website data.
It creates a table to store URLs and their associated website names.
"""

import sqlite3  # SQLite library to interact with databases
import os  # File handling (for creating directories)

from loguru import logger  # For logging database setup information

def init_db():
    """Initialize the SQLite database and create the necessary table."""
    
    # Define the path for the database file
    db_file = "data/db.sqlite3"

    # Ensure the 'data' folder exists to store the database file
    os.makedirs("data", exist_ok=True)

    # Connect to the SQLite database (creates the file if it doesn't exist)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create a table to store website page URLs and associated website names
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pages (
            url TEXT PRIMARY KEY,
            website TEXT
        )
    ''')

    # Save (commit) the changes to the database
    conn.commit()

    # Log the completion of the database setup
    logger.bind(agent="Database", task="Setup", page="N/A").info("Database setup complete.")

    # Return the database connection to be used later in the program
    return conn
