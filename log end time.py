import datetime
from time import sleep

def code_end_time():
    
   for i in range(3*55):
       e = datetime.datetime.now()
       end_time = ("%s.%s.%s %s_%s_%s" % (e.hour, e.minute, e.second, e.day, e.month, e.year, ))
       file = open(f'{end_time}_{i:03d}.txt', 'w')
       sleep (10)
    
code_end_time()
