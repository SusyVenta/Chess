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
        self.window = tk.Frame(self, width=500, height=500, background="#232F3E")
        self.resizable(width=tk.TRUE, height=tk.TRUE)
        self.window.pack(side="top", expand=True)
        self.geometry('%sx%s' % (int(self.winfo_screenwidth() / 2), int(self.winfo_screenheight() / 2)))
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

    def unblur(self):
        windll.shcore.SetProcessDpiAwareness(1)

    def show_frame(self):
        frame = FrameChessboard(app=self.window, controller=self)
        frame.configure(bg="#232F3E")
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid(sticky="news", columnspan=2, rowspan=30)
        frame.start()
        frame.tkraise()
