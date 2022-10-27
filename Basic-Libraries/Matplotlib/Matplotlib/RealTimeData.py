import csv
import random
import time
x_val = 0
total_1 = 1000
total_2 = 1000

fieldnames = ['x_val','total_1','total_2']

with open('LiveData.csv','w') as csv_file:
    csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
    csv_writer.writeheader()
    
while True:
    
    with open('LiveData.csv','a') as csv_file:
        csv_writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        
        info = {
            'x_val'   : x_val,
            'total_1' : total_1,
            'total_2' : total_2
        }
        
        csv_writer.writerow(info)
        print(x_val,total_1,total_2)
        
        x_val += 1
        total_1 = total_1 + random.randint(-6,8)
        total_2 = total_2 + random.randint(-5,6)
        
        time.sleep(1)