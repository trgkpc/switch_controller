import pygame
import pygame.locals
import time

class BasicJoycon:
    def __init__(self):
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        pygame.init()

    def __call__(self):
        while True:
            event = pygame.event.wait()

            if event.type == pygame.locals.QUIT:
                break
            else:
                self.event_handler(event)

    def event_handler(self, event):
        pass

class Joycon(BasicJoycon):
    def __init__(self):
        super(Joycon, self).__init__()

    def event_handler(self, event):
        if event.type == pygame.locals.JOYBUTTONDOWN:
            print("button", event.button, "が押されました")

if __name__ == '__main__':
    joycon = None
    try:
        joycon = Joycon()
    except pygame.error:
        print('joystickが見つかりませんでした。')

    if joycon is not None:
        joycon()
