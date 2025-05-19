from csv_functions import *

def generate(data):

    #extract time
    x=[d[2] for d in data]

    #extract file numbers
    y1=[d[0] for d in data]

    #extract total size
    y2=[d[1] for d in data]

    #convert to list
    list_to_csv(x,y1,"numfiles_vs_time.csv")
    list_to_csv(x,y2,"storage_vs_time.csv")
