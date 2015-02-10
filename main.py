import time
import os
from itertools import cycle

os.system("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s /home/yamist/Downloads/test.jpg")
for i in cycle(range(1, 522)):
    time.sleep(2)
    os.system("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s /home/yamist/Downloads/xfce_background_changer/xfce-animated-wallpaper/img/" + str(i) + ".png")
