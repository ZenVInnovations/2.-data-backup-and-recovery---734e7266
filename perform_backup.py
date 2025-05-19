import shutil
import os
import logging
import time
from file_functions import *
from compress_and_extract import *

MAX_RETRIES=3 #maximum number of tries to backup
THRESHOLD=10000 #Backup size limit

#Configure logging
logging.basicConfig(filename='backup_log.txt', level=logging.ERROR)

def perform_backup():
    retries = 0
    total_files=0
    total_storage=0
    while retries < MAX_RETRIES:
        try:
            # Specify your data sources to be backed up
            data_sources=list_files_in_directory("input")
            total_files=len(data_sources)

            file_sizes = [get_file_size(x) for x in data_sources]
            total_storage=sum(file_sizes)
            
            if(total_storage>THRESHOLD):
                logging.error(f"Storage limit exceeded. Trying again")
                file_sizes.remove(max(file_sizes))

            # Specify the output filename for the compressed backup
            backup_filename = "backup_archive.zip"

            # Compress the data sources into a single ZIP archive
            compress_data(data_sources, backup_filename)

            #transfer data to desired directory
            shutil.copy("backup_archive.zip","test_backup")
            logging.info("Backup performed successfully.")

            #remove the temporary generated zip file
            remove_file("backup_archive.zip")

            # If the backup is successful, break out of the loop
            break
        except Exception as e:
            # Log the retry attempt
            logging.warning(f"Retry attempt {retries + 1} failed. Error: {e}")
            # Sleep for a short duration before the next retry
            time.sleep(5)
            retries += 1
    else:
        logging.error(f"All retry attempts failed. Backup unsuccessful.")

    return [total_files,total_storage]
