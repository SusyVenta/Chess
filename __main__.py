import tkinter as tk
from Application import *
import sys
import os


# logo
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


chess_app = Application()
app_icon = resource_path("chess.png")
app_ext_icon = resource_path("chess.ico")
# change icon inside the app
chess_app.tk.call('wm', 'iconphoto', chess_app._w, tk.PhotoImage(file=app_icon))
# change app title inside main window
chess_app.title("Chess")
chess_app.center_app_inthescreen()
chess_app.geometry('%dx%d+%d+%d' % (500, 500, chess_app.x, chess_app.y))
chess_app.configure(bg="#232F3E")
chess_app.rowconfigure(0, weight=1)
chess_app.columnconfigure(0, weight=1)
chess_app.unblurry()
chess_app.resizable(False, False)
# run the app
chess_app.mainloop()