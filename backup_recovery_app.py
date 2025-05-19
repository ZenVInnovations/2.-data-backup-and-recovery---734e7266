from perform_backup import *
from generate_csv import *
from visualization import *
import time
import psutil

def backup_job():
    ans=perform_backup()

    #get time at which backup was done
    print("Backup job running at", time.ctime())
    ans.append(time.ctime())
    return ans

#print(backup_job())

#to check backup_main
def capture_cpu_performance():
    # Get CPU percentage usage
    cpu_percentage = psutil.cpu_percent()

    # Get detailed CPU usage information
    cpu_info = psutil.cpu_percent(percpu=True)
    #print(cpu_info)

    return cpu_percentage
data=[]
cpu_list=[]
max_iterations=5
i=0
while(i<max_iterations):
   data.append(backup_job())
   cpu_list.append(capture_cpu_performance())
   i+=1
   time.sleep(2)

generate(data)

plot_file_types("C:/Users/anshu/Desktop/CP/new")
plot_size("storage_vs_time.csv")
plot_number("numfiles_vs_time.csv")
plot_cpu_utilization("storage_vs_time.csv",cpu_list)


    
