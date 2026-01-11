from picamera2 import Picamera2, Preview
from time import sleep
from gpiozero import Button
import pygame

button = Button(18)
#Button will be pressed when GPIO 18 is grounded

#Get screen resolution
screen_width, screen_height = 640, 480
#Failed - RE and SUBPROCESS
#Failed - Tkinter
#Failed - DRM

#Using pygame - works!
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.init()
screen_width = pygame.display.Info().current_w - 1
screen_height = pygame.display.Info().current_h -1 
print("Current screen resolution")
print(screen_width)
print(screen_height)

camera = Picamera2()
#can specify a lower resolution for the preview on the next line, but did not improve performance. Camera must be the holdup
camera_config = camera.create_still_configuration(lores={"size": (screen_width, screen_height)}, display="lores")
camera.configure(camera_config)
#camera.start_preview(Preview.DRM)
camera.start_preview(Preview.DRM, x=0, y=0, width=screen_width, height=screen_height)
camera.start()

#Name picture files and save multiples
picName="blank.jpg"
picNum=1
while picNum<999:
	button.wait_for_press()
	picName = f"pic{picNum}.jpg"
	camera.capture_file(picName)
	picNum = picNum+1
	button.wait_for_release()
	sleep(1)
camera.stop_preview()

