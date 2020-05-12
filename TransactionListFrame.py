import tkinter as tk
import MainMenuFrame

class TransactionListFrame(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        #Back to main menu button
        button_mainmenu = tk.Button(self, text = "Back",
                                    command = lambda: master.switch_frame(MainMenuFrame.MainMenu))
        button_mainmenu.grid(row = 5, column = 2)