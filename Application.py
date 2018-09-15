import tkinter as tk
from FrameChessboard import *
from win32api import GetSystemMetrics
from ctypes import windll



class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        # variables for center app in the screen
        self.x = ""
        self.y = ""
        # Initialize the GUI
        tk.Tk.__init__(self, *args, **kwargs)
        self.window = tk.Frame(self, width=1000, height=800, background="#232F3E")
        self.window.pack(side="top", expand=True)
        # new frames are stacked on top of each other
        self.frames = {}
        #
        self.instantiate_and_display_canvas()

    def instantiate_and_display_canvas(self):
        # try:
        #     self.frames[FrameChessboard.__qualname__].destroy()
        # except:
        #     pass
        frame = FrameChessboard(app=self.window, controller=self)
        self.frames[FrameChessboard.__qualname__] = frame
        frame.configure(bg="#232F3E")
        frame.grid(row=0, column=0, sticky="nsew")
        frame.grid(sticky="news", columnspan=2, rowspan=30)
        self.frames["FrameChessboard"].start()
        frame.tkraise()

    def center_app_inthescreen(self):
        screen_width = GetSystemMetrics(0)
        screen_height = GetSystemMetrics(1)
        # calculate position x and y coordinates
        self.x = (screen_width / 2) - (0 / 2)
        self.y = (screen_height / 2) - (700 / 2)

    def unblurry(self):
        windll.shcore.SetProcessDpiAwareness(1)

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name.__qualname__]
        frame.tkraise()

