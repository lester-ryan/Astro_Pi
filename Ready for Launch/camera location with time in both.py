from picamera import PiCamera
from orbit import ISS
from time import sleep
import time

def take_photos():
    camera = PiCamera()
    camera.resolution = (2592, 1944)
    camera.start_preview()
    sleep(5)
# Camera warm-up time

    for i in range(3*55):
        current_time = time.time()
        location = ISS.coordinates()
        file= open(f'image_{i:03d}_{current_time}_{location}.txt','w')
        file.close()
        camera.capture(f'image_{i:03d}_{current_time}.jpg')
# will generate a text file of name image_000_IERS2010 latitude -25.3839 N longitude -53.5197 E elevation 425957.1 m.txt)        
#        will generate file of name image_000_1643210154.jpg
        sleep(60)
take_photos()

# camera turns on warms up for 5 secs
# gets location and saves it as name in text file
# takes a photo saves it with above file name and does nothing for 60 secs
# repeats this 165 times for approx 165 mins








