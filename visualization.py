import os
import matplotlib.pyplot as plt
from collections import Counter
from csv_functions import * 

def plot_file_types(folder_path):

    try:
        # Initialize a counter to store file types and their counts
        file_types_counter = Counter()

        # Traverse through the files in the given folder
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)

            # Check if it is a file (not a subdirectory)
            if os.path.isfile(filepath):
                # Get the file extension
                _, file_extension = os.path.splitext(filename)
                # Increment the counter for the file type
                file_types_counter[file_extension.lower()] += 1

        # Extract file types and their counts from the counter
        file_types, file_counts = zip(*file_types_counter.items())

        # Plot the file types vs. number of files
        plt.figure(figsize=(10, 6))
        plt.bar(file_types, file_counts, color='green')
        plt.xlabel('File Types')
        plt.ylabel('Number of Files')
        plt.title('File Types Distribution in the Folder')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('types_of_files.png')
        #plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def plot_size(path):

    try:
        #extract lists from csv file
        #time
        x=csv_to_list(path)[0]
        #total_size
        y=csv_to_list(path)[1]
        y=[int(i) for i in y]
    
        #plot
        plt.figure(figsize=(10, 6))
        plt.bar(x, y, color='green')
        plt.xlabel('Time')
        plt.ylabel('Data_backed_up')
        plt.title('Backed up data vs date')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('number_of_files.png')
        #plt.show()
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def plot_number(path):

    try:
        #extract list from csv files
        #time
        x=csv_to_list(path)[0]
        #number of files
        y=csv_to_list(path)[1]
        y=[int(i) for i in y]

        #plot
        plt.figure(figsize=(10, 6))
        plt.bar(x, y, color='green')
        plt.xlabel('Time')
        plt.ylabel('Number of files backed up')
        plt.title('total files backed up vs date')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('storage_graph.png')
        #plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def plot_cpu_utilization(path,cpu_list):
    try:
        #extract list from csv files
        #time
        x=csv_to_list(path)[0]
        #cpu_utilization
        y=cpu_list

        #plot
        plt.figure(figsize=(10, 6))
        plt.bar(x, y, color='green')
        plt.xlabel('Time')
        plt.ylabel('CPU utilization')
        plt.title('CPU utilization vs date')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('cpu_utilization.png')
        #plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

