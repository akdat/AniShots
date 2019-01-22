from mss import mss
import mss.tools
import os, os.path
import errno
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

    def __init__(self, path):
        self.path =path

    def make_dir(self):

        ''' Open "path" for writing, creating any parent directories as needed. '''

        try:
            os.mkdir(self.path)
            print("Successfully created the directory %s" % self.path)
        except OSError as exc:
            if exc.errno == errno.EEXIST and os.path.isdir(self.path):
                print('here')
                pass
            else:
                print("Creation of the directory %s failed" % self.path)
                print('here2')
                raise

    def change_dir(self):
        try:
            os.chdir(self.path)
        except OSError as exc:
            print('here4')
            raise
            #if exc.errno =

    def make_change(self,):
        self.make_dir()
        self.change_dir()
        pass

if __name__ == '__main__':

    folder = FileHandling("C:\\Users\\jalexanu\\Desktop\\ScreenSeries")
    folder.make_change()

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
#TODO: create lineart based on image
