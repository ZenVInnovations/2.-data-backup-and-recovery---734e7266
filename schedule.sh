#!/bin/bash

# Path to the Python interpreter
PYTHON_PATH=/path/to/python

# Path to the Python script
SCRIPT_PATH=/path/to/your/script.py

# Function to check the password
check_password() {
    read -sp "Enter password: " entered_password
    echo
    # Replace 'your_secure_password' with your actual secure password
    if [ "$entered_password" != "1234" ]; then
        echo "Incorrect password. Exiting."
        exit 1
    fi
}

# Check the password before proceeding
check_password

# Schedule the Python script to run daily at 2:30 PM
echo "30 14 * * * $PYTHON_PATH $SCRIPT_PATH" | crontab -

echo "Script scheduled successfully!"
