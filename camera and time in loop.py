from picamera import PiCamera
from time import sleep

def take_photos:
    camera = PiCamera()
    camera.resolution = (2592, 1944)

    for i in range(3*55):
        e = datetime.datetime.now()
        current_time = ("%s.%s.%s %s_%s_%s" % (e.hour, e.minute, e.second, e.day, e.month, e.year, ))
        camera.capture(f'image_{i:03d}_{current_time}.jpg')
        sleep(60)
        
take_photos()
        
    
# less photos to allow time to get time at start and finish
# photos will be saved as 001.jpg 002.jpg etc