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
        #
        self.lastx = ""
        self.lasty = ""

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

    def move(self, event):
        if self.frames["FrameChessboard"].move_flag:
            new_xpos, new_ypos = event.x, event.y

            self.frames["FrameChessboard"].board.move(self.frames["FrameChessboard"].a8,
                             new_xpos - self.mouse_xpos, new_ypos - self.mouse_ypos)

            self.mouse_xpos = new_xpos
            self.mouse_ypos = new_ypos
        else:
            self.frames["FrameChessboard"].move_flag = True
            self.frames["FrameChessboard"].board.tag_raise(self.frames["FrameChessboard"].a8)
            self.mouse_xpos = event.x
            self.mouse_ypos = event.y

    def release(self, event):
        self.frames["FrameChessboard"].move_flag = False


    def highlight_moves_by_clicking_on_square(self, event):
        # get object closest to to current mouse position
        item2 = self.frames["FrameChessboard"].board.find_closest(event.x, event.y)
        # get 3d tag of the closest element
        current_piece = self.frames["FrameChessboard"].board.gettags(item2)[2]

        #print (self.frames["FrameChessboard"].board.itemcget(item2, "tag")) # --> h8, black, rook, current.
        # item = highlighted piece
        item = self.frames["FrameChessboard"].a7

        if current_piece == "rook" and 'a7' in self.frames["FrameChessboard"].board.gettags(item)[0]:
            # get current color of the square
            current_color = self.frames["FrameChessboard"].board.itemcget(item, 'fill')
            # if current square is not highlighted
            if current_color == 'grey' or current_color == "white":
                # highlight square
                self.frames["FrameChessboard"].board.itemconfig(item, fill='green')
            else:
                # if it was already highlighted, set it back to its original color
                self.frames["FrameChessboard"].board.itemconfig(item, fill=self.frames["FrameChessboard"].board.gettags(item)[1])

