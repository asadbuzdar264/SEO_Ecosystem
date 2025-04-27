# This is the main file for the bot. It sets up the bot and starts it.
from dotenv import load_dotenv  # Loads secret keys (like API keys)
import os  # Helps with files and folders
from config.logging_config import setup_logging  # Sets up our log file
from utils.db_manager import init_db  # Sets up our database
load_dotenv()

def main():
    # Set up logging
    setup_logging()

    # Initialize the database
    init_db()

    # Ask the user for a website URL
    # This is the URL that the bot will use to check for changes
    website_url = input("Please type the website URL (like https://example.com): ")

    # Write to the log file that we started
    print(f"Starting SEO analysis for {website_url}")
    print(f"Saved {website_url} in the database")
    print("Setup complete! Next, we'll add crawling.")

    #Run the program
if __name__ == "__main__":
    main()
    # This is the main function that runs when the script is executed# main.py
"""
This is the main entry point for the SEO analysis bot.
It sets up logging, initializes the database, and collects the target website URL.
"""

import os  # Helps with environment variables and file handling
from dotenv import load_dotenv  # Loads secret keys (like API keys)

from config.logging_config import setup_logging  # Logging configuration
from utils.db_manager import init_db  # Database setup

def main():
    """Main function to set up and start the SEO bot."""
    # Load environment variables
    load_dotenv()

    # Set up logging
    setup_logging()

    # Initialize the database
    init_db()

    # Ask the user for a website URL
    website_url = input("Please type the website URL (e.g., https://example.com): ").strip()

    # Log startup information
    print(f"Starting SEO analysis for {website_url}")
    print(f"Saved {website_url} in the database.")
    print("Setup complete! Next, we'll add crawling functionality.")

if __name__ == "__main__":
    # Run the program only if this file is executed directly
    main()
