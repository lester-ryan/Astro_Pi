from picamera import PiCamera
from time import sleep
from orbit import ISS
import time

def take_photos:
    camera = PiCamera()
    camera.resolution = (2592, 1944)

    for i in range(3*55):
        location = ISS.coordinates()
        time = time.time()
        camera.capture(f'image_{i:03d}_{time}_{location}.jpg')
        sleep(60)
        
take_photos()
        
# cant test ISS module so not sure what format location will be in    
# less photos to allow time to get time at start and finish
# worried about errors pulling the whole thing down, should i seperate it out more
