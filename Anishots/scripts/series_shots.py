from mss import mss
import mss.tools
import os.path

class ScreenShotMSS:

    def screenshot(self, amount):
        print('yo')
        with mss.mss() as sct:
            for _ in range(amount):
                file = sct.shot(output ="stuff.png")
                print(file)


class FileHandling:
    def on_exists(self, filename):
        if os.path.isfile(filename):
            pass

if __name__ == '__main__':
    scrn = ScreenShotMSS()
    scrn.screenshot(20)
    print('yo')


#TODO: ON first Click start taking acreenshots on second click stop
#TODO: output image to file
#TODO: Image buffer
#TODO: Optimise images in buffer

