#!/bin/bash

# Function to check the password
check_password() {
    read -sp "Enter password: " entered_password
    echo
    # Replace 'your_secure_password' with your actual secure password
    if [ "$entered_password" != "your_secure_password" ]; then
        echo "Incorrect password. Exiting."
        exit 1
    fi
}

# Check the password before proceeding
check_password

# Remove the existing cron job
(crontab -l | grep -v "$PYTHON_PATH $SCRIPT_PATH") | crontab -

echo "Cron job stopped successfully!"
