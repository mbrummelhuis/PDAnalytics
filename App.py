import tkinter as tk
from MainMenuFrame import MainMenu

class App(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Personal Data Analytics")
        self.geometry('600x400')
        self._frame = None
        self.switch_frame(MainMenu)
    
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        
        if not self._frame == None:
            self._frame.destroy()
        
        self._frame = new_frame
        self._frame.grid()


