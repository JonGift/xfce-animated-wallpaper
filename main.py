import time
import os

os.system("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s /home/yamist/Downloads/test.jpg")
i = 1
while True:
	time.sleep(2)
	os.system("xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s /home/yamist/Downloads/xfce_background_changer/xfce-animated-wallpaper/img/" + str(i) + ".png")
	i += 1
	if i == 521:
		i = 1