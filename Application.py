import os
import sys
import tkinter as tk
from FrameChessboard import *
from win32api import GetSystemMetrics
from ctypes import windll


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        # Initialize the GUI
        tk.Tk.__init__(self, *args, **kwargs)
        self.window = tk.Frame(self, width=600, height=600, background="#232F3E")
        self.window.pack(side="top", expand=True)
        # self.geometry('%dx%d+%d+%d' % (600, 620, self.center_app_inthescreen()[0],
        #                                self.center_app_inthescreen()[1]))
        self.geometry('%sx%s' % (int(self.winfo_screenwidth() / 2.2), int(self.winfo_screenheight() / 2.2)))
        self.title("Chess")
        self.unblur()
        self.resizable(False, False)
        self.tk.call('wm', 'iconphoto', self._w, tk.PhotoImage(file=self.resource_path("Icons\chess.png")))
        #
        self.show_frame()

    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    def center_app_inthescreen(self):
        screen_width = GetSystemMetrics(0)
        screen_height = GetSystemMetrics(1)
        # calculate position x and y coordinates
        x = (screen_width / 2) - 250
        y = (screen_height / 2) - 400
        return [x, y]

    def unblur(self):
        windll.shcore.SetProcessDpiAwareness(1)

    def show_frame(self):
        frame = FrameChessboard(app=self.window, controller=self)
        frame.configure(bg="#232F3E")
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid(sticky="news", columnspan=2, rowspan=30)
        frame.start()
        frame.tkraise()
