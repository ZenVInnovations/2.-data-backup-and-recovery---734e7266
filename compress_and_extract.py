import zipfile
import os

def compress_data(data_sources, output_filename):
    try:
        with zipfile.ZipFile(output_filename, 'w') as zipf:
            for source in data_sources:
                # Add each file/directory to the ZIP archive
                zipf.write(source, os.path.basename(source))
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    

def restore_backup(backup_file, destination_path):
    try:
        #Extract zipfile from backup directory
        with zipfile.ZipFile(backup_file, 'r') as zip_file:
            zip_file.extractall(destination_path)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
