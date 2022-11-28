from socket import *
import pyautogui
import webbrowser
#import queue
import time

#task = queue.Queue()

dt = 0.01

def put_key(key):
    #pyautogui.typewrite(key)
    #pyautogui.press(key)

    pyautogui.keyDown(key)
    time.sleep(dt)
    pyautogui.keyUp(key)

def avoid():
    url = "youtube.com/watch?v=G476yr…"
    webbrowser.open(url)

dat = [
    ["up", "e"],
    ["down", "d"],
    ["right", "f"],
    ["left", "s"],
    ["x", "i"],
    ["y", "j"],
    ["b", "k"],
    ["a", "l"],
    ["start","u"],
    ["select","r"],
    ["l", "w"],
    ["r", "o"],
]

## UDP受信クラス
class udprecv():
    def __init__(self):

        SrcIP = ""                             # 受信元IP
        SrcPort = 50007                                 # 受信元ポート番号
        self.SrcAddr = (SrcIP, SrcPort)                 # アドレスをtupleに格納

        self.BUFSIZE = 1024                             # バッファサイズ指定
        self.udpServSock = socket(AF_INET, SOCK_DGRAM)  # ソケット作成
        self.udpServSock.bind(self.SrcAddr)             # 受信元アドレスでバインド

    def recv(self):
        while True:                                     # 常に受信待ち

            data, addr = self.udpServSock.recvfrom(self.BUFSIZE)
                                                        # 受信
            cmd = data.decode()
            print(cmd, addr)                            # 受信データと送信アドレス表示

            # GUI呼び出し
            for x,key in dat:
                if x == cmd:
                    print(f'press {cmd} key ({key})')
                    put_key(key)
            if cmd == "exit":
                avoid()

udp = udprecv()     # クラス呼び出し
udp.recv()          # 関数実行
