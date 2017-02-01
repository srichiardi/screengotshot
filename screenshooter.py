from Tkinter import *
import tkFileDialog
from ttk import Progressbar
import time
import os
from modules.imagipy import add_url_time


def screenshot(url, fname):
    WIDTH = 1024
    ROOT = os.path.dirname(os.path.abspath(__file__))
    RASTERIZE_SCRIPT = "{root}/js-scripts/rasterize.js".format(root=ROOT)
    
    cmd = 'phantomjs {rast} "{url}" {out} {w}px'.format(
        rast=RASTERIZE_SCRIPT, url=url, out=fname, w=WIDTH )
    os.system(cmd)


class ScreenShooterGui(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("WebSite ScreenShooter")
        self.geometry("390x360")

        self.mainFrame = Frame(self)
        self.mainFrame.pack(pady=5, padx=5)

        self.urlLabelFrame = Frame(self.mainFrame)
        self.urlLabelFrame.pack(pady=5, side=TOP, fill=X)
        self.urlImportLabel = Label(self.urlLabelFrame, text="web URLs:")
        self.urlImportLabel.pack(side=LEFT, padx=5)

        self.importTextFrame = Frame(self.mainFrame)
        self.importTextFrame.pack(pady=5, side=TOP, fill=X)
        self.yTextScrollbar = Scrollbar(self.importTextFrame)
        self.yTextScrollbar.pack(side=RIGHT, fill=Y)
        self.xTextScrollbar = Scrollbar(self.importTextFrame, orient=HORIZONTAL)
        self.xTextScrollbar.pack(side=BOTTOM, fill=X)
        self.importUrlsText = Text(self.importTextFrame, padx=5, pady=5,
                                   wrap=NONE, width=50, height=10,
                                   yscrollcommand=self.yTextScrollbar.set,
                                   xscrollcommand=self.xTextScrollbar.set)
        self.importUrlsText.pack(side=TOP, padx=5, pady=5, fill=X)
        self.yTextScrollbar.config(command=self.importUrlsText.yview)
        self.xTextScrollbar.config(command=self.importUrlsText.xview)

        self.outputLabelFrame = Frame(self.mainFrame)
        self.outputLabelFrame.pack(pady=5, side=TOP, fill=X)
        self.outputFileLabel = Label(self.outputLabelFrame, text="Path to the output folder:")
        self.outputFileLabel.pack(side=LEFT, padx=5)

        self.outputFieldFrame = Frame(self.mainFrame)
        self.outputFieldFrame.pack(pady=5, side=TOP, fill=X)
        self.outputFieldEntry = Entry(self.outputFieldFrame,
                                      name="outputFile", width=30)
        self.outputFieldEntry.pack(side=LEFT,padx=5)
        self.btnBrowse = Button(self.outputFieldFrame, height=1, width=6,
                                text="Browse...",command=self.browse)
        self.btnBrowse.pack(side=RIGHT, padx=5)

        self.controlsFrame = Frame(self.mainFrame)
        self.controlsFrame.pack(pady=5, side=TOP, fill=X)
        self.btnClose = Button(self.controlsFrame, height=1, width=6,
                               text="Close", command=self.close)
        self.btnClose.pack(side=LEFT, padx=5)
        self.btnRun = Button(self.controlsFrame, height=1, width=6,
                             text="Run", command=self.run)
        self.btnRun.pack(side=RIGHT, padx=5)

        # *** PROGRESS BAR ***
        self.status = Progressbar(self.mainFrame, orient='horizontal',
                                  length=310, mode='determinate',
                                  value=0, maximum=100)
        self.status.pack(pady=5, padx=5, side=BOTTOM)

    def browse(self):
        outputPath = tkFileDialog.askdirectory(parent=self)
        self.outputFieldEntry.delete(0, last=END)
        self.outputFieldEntry.insert(0, outputPath)

    def close(self):
        self.destroy()

    def run(self):
        textUrls = self.importUrlsText.get('1.0', 'end')
        # creating a list ignoring empty values
        listOfUrls = [x for x in textUrls.split("\n") if x]
        stepAmount = 100 / len(listOfUrls)
        for url in listOfUrls:
            url = url.strip()
            fileName = url.split("/")[2] + ".png"
            output = self.outputFieldEntry.get() + "/" + fileName
            screenshot(url, output)
            add_url_time(url, output)
            self.status.step(stepAmount)
            self.update()


    def mainloop(self):
        Tk.mainloop(self)

ScreenShooterGui().mainloop()
