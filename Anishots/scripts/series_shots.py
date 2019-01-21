from mss import mss
import mss.tools
import os, os.path
import tempfile
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

    path = "tmp/action"

    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s" % path)

    def on_exists(self, filename):
        if os.path.exists(filename):
            pass

    def mkdir_p(path):
        try:
            os.makedirs(path)
        except OSError as exc:  # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                raise

    def safe_open_w(path):
        ''' Open "path" for writing, creating any parent directories as needed.
        '''
        mkdir_p(os.path.dirname(path))
        return open(path, 'w')


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
#TODO: create lineart based on image
