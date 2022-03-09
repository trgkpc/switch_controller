import pygame
import pygame.locals
import time

def call_key(dat):
    print(dat)

def main() :
    pygame.joystick.init()
    joystick0 = pygame.joystick.Joystick(0)
    joystick0.init()

    print('joystick start')

    pygame.init()

    while True:
        # コントローラーの操作を取得
        eventlist = pygame.event.get()
        xy = []
        for i in range(joystick0.get_numaxes()):
            xy.append(joystick0.get_axis(i))

        # イベント処理
        for e in eventlist:
            if e.type == pygame.locals.QUIT:
                return
            if e.type == pygame.locals.JOYBUTTONDOWN:
                xy.append(e.button)

        call_key(xy)

        time.sleep(0.1)

if __name__ == '__main__':
    try:
        main()
    except pygame.error:
        print('joystickが見つかりませんでした。')
