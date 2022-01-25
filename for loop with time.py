from time import sleep
import datetime


def take_time():
    for i in range(3):
        e = datetime.datetime.now()
        current_time = ("%s.%s.%s %s.%s.%s" % (e.hour, e.minute, e.second, e.day, e.month, e.year, ))
        file = open(f'file_{i:03d}_{current_time}', 'w')
        file.close()
        sleep(5)
        
take_time()
        
    
# less photos to allow time to get time at start and finish

