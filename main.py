import time
import os
from itertools import cycle

def wallpaper(i):
    #Change image path here.
    os.system("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s /home/yamist/Downloads/xfce-animated-wallpaper/img/" + str(i) + ".png")

direction = input('Input (left/right)')

if direction.lower() == 'left':
    for i in cycle(reversed(range(1, 521))):
        time.sleep(2)
        wallpaper(i)

elif direction.lower() == 'right':
    for i in cycle(range(1, 521)):
        time.sleep(2)
        wallpaper(i)