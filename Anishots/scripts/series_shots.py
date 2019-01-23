from mss import mss
import mss.tools
import os, os.path
import errno
import win32api
import time
import tkinter as tk
from tkinter import filedialog
import PyQt5
from PIL import Image

class ScreenShotMSS:

    def screenshot(self, amount, i):
        file = []
        with mss.mss() as sct:
            for _ in range(amount):
                file=sct.shot(output ='run%s.png' %i)


class FileHandling:

    def __init__(self):
        root = tk.Tk()
        self.path  = filedialog.askdirectory(title ="Choose output folder")
        root.withdraw()

    def make_dir(self):

        ''' Open "path" for writing, creating any parent directories as needed. '''

        try:
            os.mkdir(self.path)
            print("Successfully created the directory %s" % self.path)
        except OSError as exc:

            if exc.errno == errno.EEXIST and os.path.isdir(self.path):
                pass
            else:
                print("Creation of the directory %s failed" % self.path)

    def change_dir(self):
        try:
            os.chdir(self.path)
        except OSError as exc:
            raise

    def make_change(self):
        self.make_dir()
        self.change_dir()

class PostProcessing:


    def crop_im(self, image):
        directory = FileHandling()
        directory.make_change()

        im = Image.open(image)
        width, height = im.size

        left= (width - 200 )
        top =(height - 200 )
        right = (width + 200)
        bottom =(height + 200 )
        cropped_image = im.crop((left, top, right, bottom))

        cropped_image.save('L_2d_cropped.png')


    def optimise(self):
        pass

class Config:

    def setup(self):
        i = 0
        state_left = 1  # left button down
        # frame_ps = float(input("select an interval e.g 0.05 >>\t"))

        # instance creation
        folder = FileHandling()
        folder.make_change()
        scrn = ScreenShotMSS()

        time.sleep(1)  # temp wait to ensure it doesn't run after the mouse event that clicks compile

        while True:
            a = win32api.GetKeyState(0x01)

            if a != state_left:
                pass
            else:
                i += 1
                scrn.screenshot(1, i)

            time.sleep(0.05)


if __name__ == '__main__':
    start = PostProcessing()
    start.crop_im('C:\\Users\\jalexanu\\Desktop\\ScreenSeries\\run1.png')



#TODO: SNIP screenshot or area in python
#TODO: Image buffer
#TODO: Use HTMLShot to convert a HTML image into an element

