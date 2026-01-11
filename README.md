# OpenDroneCam
Build accessable mapping, photogrammetry, and photography cameras with flight controller connectivity for homemade professional drones

One of the most exciting aspects of drones is how they make powerful sensing technologies accessible to small businesses and individuals. However, recent government actions threaten that accessibility. Building DIY vehicles is an option, but usable sensors are hard to find.

This project aims to provide tools for building affordable cameras that are suitable for mapping, photogrammetry, and photography.
The first version is python code meant to be used on any Raspberry Pi with a camera attached to its CSI port. It outputs an HDMI or analog video preview and captures full-resolution photos when GPIO 18 (pin 12) is shorted to ground (pin 14). This allows flight controllers with relay capability to control when pictures are taken. It can also be used to make a point and shoot camera with a button.

Future goals:
Add video recording
Improve filename code to prevent overwriting older photos and videos
Save photo and video files to USB device for easier downloading to non-linux systems
Add serial UART based communications to support more flight controllers
Add remote control of camera settings
Support USB cameras
Support other SBCs and microcontrollers
