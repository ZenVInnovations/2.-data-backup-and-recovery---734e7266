Automated Data Backup and Recovery System
Overview
The Automated Data Backup and Recovery System is a robust software solution designed to automate the process of regularly backing up data to a remote location and enabling easy recovery in case of data loss or corruption. This project leverages Python for scheduling backups, handling data compression, and generating reports, while Bash scripts manage data transfer and storage.

Features
Automated Backup: The system automates the backup process, ensuring regular and reliable data backups.

Data Compression: Utilizing Python, the system compresses data into a single ZIP archive, optimizing storage space and facilitating efficient data transfer.

Remote Backup: Data is transferred to a remote location for secure storage, minimizing the risk of data loss due to local issues.

Error Handling: The system includes error handling mechanisms, with logging capabilities to track backup attempts, ensuring data integrity.

Visualization: The project provides visual insights into backup performance, including the number of files backed up, storage usage, and CPU utilization.

Components
1. backup_main.py
Main script orchestrating the backup process.
Imports modules for performing backups, generating CSV reports, and visualization.
2. perform_backup.py
Manages the actual backup process, handling retries and logging for error tracking.
Uses file functions, compression, and extraction modules.
3. compress_and_extract.py
Provides functions for compressing and extracting data using the ZIP format.
4. file_functions.py
Contains utility functions for obtaining file sizes, listing files in a directory, and removing files.
5. csv_functions.py
Includes functions for converting data to and from CSV format, facilitating report generation.
6. generate_csv.py
Generates CSV reports for visualization, extracting data from the backup process.
7. schedule.sh
Bash script for scheduling and automating the backup process.
8. stop_schedule.sh
Bash script to stop scheduling

Getting Started
Dependencies:

Python 3.x
Bash (for scheduling)
Installation:

Clone the repository.
Usage:

Run backup_main.py to initiate the backup process.
Visualization:

Use generated CSV files with visualization tools of choice to analyze backup performance.
Configuration
Adjust constants in backup_main.py for maximum retries (MAX_RETRIES) and storage threshold (THRESHOLD) as needed.

Contributors
Anshul Sharma
Suraj Kumar Patel
