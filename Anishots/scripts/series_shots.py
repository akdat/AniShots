from mss import mss
import mss.tools
import os, os.path
import errno
import win32api
import time
import tkinter as tk
from tkinter import filedialog


class ScreenShotMSS:

    def screenshot(self, amount, i):
        with mss.mss() as sct:
            for _ in range(amount):
                file = sct.shot(output ='run%s.png' %i)


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

    def make_change(self,):
        self.make_dir()
        self.change_dir()

class Optimiser:
    def lossless(self):
        pass

if __name__ == '__main__':

    i = 0
    state_left = 1  # left button down
    #frame_ps = float(input("select an interval e.g 0.05 >>\t"))

    #instance creation
    folder = FileHandling()
    folder.make_change()
    scrn = ScreenShotMSS()

    time.sleep(1) #temp wait to ensure it doesn't run after the mouse event that clicks compile

    while True:
        a = win32api.GetKeyState(0x01)

        if a != state_left:
            pass
        else:
            i += 1
            scrn.screenshot(1, i)

        time.sleep(0.05)


#TODO: POST PROCESSING
#TODO: Image buffer
#TODO: SNIP screenshot or area in python
#TODO: create lineart based on image

