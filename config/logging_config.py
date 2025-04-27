# config/logging_config.py
"""
This file sets up the logging system for the SEO Ecosystem project.

It creates a log file (logs/seo_eco.log) to record what the program does.
Logs are saved in JSON format for easy future use (like building a dashboard).
"""

from loguru import logger  # Import Loguru for better logging
import os  # Helps with file and folder operations

def setup_logging():
    """Configure the logging settings for the project."""
    
    # Remove any old/default log settings
    logger.remove()

    # Define the path for the log file
    log_file = "logs/seo_eco.log"

    # Make sure the logs/ folder exists
    os.makedirs("logs", exist_ok=True)

    # Set up the logger to write to the log file
    logger.add(
        log_file,
        format='{time} | {level} | {extra[agent]} | {extra[task]} | {extra[page]} | {message}',
        rotation="10 MB",  # Rotate (start a new log file) when it reaches 10 MB
        serialize=True     # Save logs as JSON (easier for future web apps)
    )

    # Log that the logging system is ready
    logger.bind(agent="Logger", task="Setup", page="N/A").info("Logging setup complete.")

