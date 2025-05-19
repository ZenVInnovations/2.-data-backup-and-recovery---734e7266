import csv

def list_to_csv(x,y,filename):
    # Combine lists into a list of tuples
    data = list(zip(x,y))
    # Specify the CSV file path
    csv_file_path = filename

    try:
        # Write the lists to the CSV file
        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            # Write data rows
            csv_writer.writerows(data)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def csv_to_list(path):
    csv_file_path = path
    x=[]
    y=[]

    try:
        # Read data from the CSV file and append to lists
        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Read each row and append data to lists
            for row in csv_reader:
                x.append((row[0]))
                y.append(row[1])
        return [x,y]
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

