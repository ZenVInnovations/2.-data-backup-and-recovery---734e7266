import os

def get_file_size(file_path):
    try:
        # Get the size of the file in bytes
        file_size = os.path.getsize(file_path)
        return file_size
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def list_files_in_directory(directory):
    try:
        file_paths = []
        # Iterate through all files in the directory
        for filename in os.listdir(directory):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
        
            # Check if it's a regular file (not a directory)
            if os.path.isfile(file_path):
                # Append the file path to the list
                file_paths.append(file_path)
    
        return file_paths
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def remove_file(file_path):
    try:
        os.remove(file_path)
        #print(f"File '{file_path}' removed successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
