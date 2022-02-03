from picamera import PiCamera
from time import sleep
import time



def take_photos():
    
    camera = PiCamera()
    camera.resolution = (4056, 3040)
    camera.start_preview()
    sleep(5)
# Camera warm-up time

    for i in range(120):
        current_time = time.time() # get current time
        camera.capture(f'image_{i:03d}_{current_time}.jpg')
# capture image and save as image_000_1643366165.jpg
        sleep(60) # sleep for 60 seconds before reentering loop
        
take_photos()



