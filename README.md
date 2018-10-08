# rpi_lcd
LCD display program for Raspberry Pi

1. Install wiring pi.

    Refer to [wiringpi-and-the-raspberry-pi-compute-board][1]
```
cd ~
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
```
Or
```
sudo apt-get install wiringpi
```

2. Compile
```
cc -o pcd8544_rpi pcd8544_rpi.c PCD8544.c  -L/usr/local/lib -lwiringPi
```

3. Run
```
sudo ./pcd8544_rpi
```

4. Auto start
Add following line in "/etc/rc.local" before "exit 0" line.
```
sudo /home/pi/cpu_show/cpushow
```

Reference to post of [EnjoyPi][1]

[1]: http://wiringpi.com/wiringpi-and-the-raspberry-pi-compute-board/ "WiringPi"
[2]: http://raspifans.com/bbs/forum.php?mod=viewthread&tid=123 "EnjoyPi"
