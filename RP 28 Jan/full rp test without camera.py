from time import sleep
import time
from orbit import ISS

def take_photos():
    sleep(5)
    for i in range(2*2):
        txtfile = (open('test file for ISS.txt', 'a'))
        location = ISS.coordinates()
        txtfile.writelines(f'{location} {i:03d}')
        txtfile.writelines('\n')
        txtfile.close()
        current_time = time.time()
#        camera.capture(f'image_{i:03d}_{e}.jpg')
        file = open(f'image_{i:03d}_{current_time}.jpg', 'w')
        sleep(1)
        
take_photos()





    

