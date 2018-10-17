import time
import datetime
from PCD8544 import PCD8544 as lcd
# import threading
# import Adafruit_DHT
# from speed import RaspberryMonitorNetSpeed as rmn
 
ns = [-1, -1]
th = [-2, -2]
 
def main():
    a = lcd(dc=13, rst=5, sclk=26, din=19, cs=6, vcc=20, bl=21)
    a.begin(contrast=60)
    # tmp = threading.Thread(target=network_speed)
    # tmp.setDaemon(True)
    # tmp.start()
    # tmp = threading.Thread(target=temperature_humidity)
    # tmp.setDaemon(True)
    # tmp.start()
    while True:
        try:
            a.clear()
            # 上传速度
            # a.draw_str(0, 'U: ' + str(ns[1]))
            # 下载速度
            # a.draw_str(1, 'D: ' + str(ns[0]))
            # 温度
            # a.draw_str(2, 'T: ' + str(th[1]) + ' C')
            # 湿度
            # a.draw_str(3, 'H: ' + str(th[0]) + '%')
            # 时间
            a.draw_str(4, datetime.datetime.now().__str__()[5:].lstrip('0').split('.')[0])
            a.display()
            time.sleep(1)
        except KeyboardInterrupt:
            a.quit()
            exit(0)
 
# def network_speed():
#     global ns
#     b = rmn('bankroft', '123456')
#     while True:
#         time.sleep(1)
#         ns = b.get_human_speed()
 
# def temperature_humidity():
#     global th
#     pin = 25
#     while True:
#         time.sleep(10)
#         th = Adafruit_DHT.read_retry(11, 25)
 
if __name__ == '__main__':
    main()