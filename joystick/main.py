import pygame
from pygame.locals import *
import time
import socket as sk
import psutil

table = [
    [14, "l"],
    [15, "r"],
    [0, "a"],
    [1, "x"],
    [3, "y"],
    [2, "b"],
    [[1,0], "up"],
    [[0,1], "left"],
    [[-1,0], "down"],
    [[0,-1], "right"],
    [5,"start"],
    [4,"select"],
    [12,"exit"]
]


ip="192.168.0.19"
main_port = 50007
sub_port = 50008
def send(data, port):
    print(f'send {data}')
    with sk.socket(sk.AF_INET, sk.SOCK_DGRAM) as s:
        s.sendto(str(data).encode('utf-8'), (ip, port))

def call_key(dat):
    for x,key in table:
        if x == dat:
            send(key, main_port)
            send(psutil.sensors_battery(), sub_port)

def main() :
    pygame.joystick.init()
    joystick0 = pygame.joystick.Joystick(0)
    joystick0.init()

    print('joystick start')

    pygame.init()

    while True:
         # コントローラーの操作を取得
        eventlist = pygame.event.get()

        # イベント処理
        for e in eventlist:
            if e.type == QUIT:
                return
            if e.type == pygame.locals.JOYHATMOTION:
                x, y = joystick0.get_hat(0)
                call_key([x,y])                
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                call_key(e.button)

        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except pygame.error:
        print('joystickが見つかりませんでした。')


