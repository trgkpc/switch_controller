import pygame
from pygame.locals import *
import time

table = [
    [14, "r"],
    [15, "l"],
    [0, "a"],
    [1, "x"],
    [3, "y"],
    [2, "b"],
    [[1,0], "up"],
    [[0,1], "left"],
    [[-1,0], "down"],
    [[0,-1], "right"],
    [5,"start"],
    [4,"select"]
]

def call_key(dat):
    for x,key in table:
        if x == dat:
            print(key)

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
