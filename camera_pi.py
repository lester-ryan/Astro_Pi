from picamera import PiCamera
from time import sleep

def take_photos:
    camera = PiCamera()
    camera.resolution = (2592, 1944)

    for i in range(3*55):
        camera.capture(f'image_{i:03d}.jpg')
        sleep(60) 
    
# less photos to allow time to get time at start and finish
# photos will be saved as 001.jpg 002.jpg etc