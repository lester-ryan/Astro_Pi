import datetime

def code_start_time():
    file = open('start_time.txt', 'w')
# write a txt file   

    e = datetime.datetime.now()
    start_time = ("%s:%s:%s %s/%s/%s " % (e.hour, e.minute, e.second, e.day, e.month, e.year, ))
# get current date and time



    file.writelines(start_time)
# write information to file


# close the file
    file.close()
    
def code_end_time():
    file = open('end_time.txt', 'w')
# write a txt file   

    e = datetime.datetime.now()
    end_time = ("%s:%s:%s %s/%s/%s " % (e.hour, e.minute, e.second, e.day, e.month, e.year, ))
# get current date and time



    file.writelines(end_time)
# write information to file


# close the file
    file.close()
    
    
code_start_time()
code_end_time()
