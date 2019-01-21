from mss import mss
import mss.tools
import os.path
import win32api
import time


class ScreenShotMSS:

    def screenshot(self, amount, i):

        with mss.mss() as sct:
            for _ in range(amount):
                file = sct.shot(output ='run%s.png' %i)
                print(file)

class Optimiser:

    def lossless(self):
        pass

class FileHandling:
    def on_exists(self, filename):
        if os.path.exists(filename):
            pass



if __name__ == '__main__':
    scrn = ScreenShotMSS()
    i = 0
    state_left = 1 #left button down

    time.sleep(1) #temp wait to ensure it doesn't run after the mouse event that clicks compile

    while True:
        a = win32api.GetKeyState(0x01)
        if a != state_left:
            pass
        else:
            i += 1
            scrn.screenshot(1, i)

        time.sleep(0.1)



#TODO: ON first Click(mouse event outside of program) start taking acreenshots on second click stop
#TODO: output image to file
#TODO: Image buffer
#TODO: Optimise images in buffer

