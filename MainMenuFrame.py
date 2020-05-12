import tkinter as tk
from AddTransactionFrame import AddTransactionFrame
from TransactionListFrame import TransactionListFrame

class MainMenu(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        #Message top of the screen---------------------------------------------
        label_intro = tk.Label(self, text = "Welcome to the Personal Data Analytics dashboard!",
                               bg = "grey", fg = "black", width = "90", height = 3)
        label_intro.grid(row = 0, column = 0, columnspan = 3)
    
        #Add transaction button------------------------------------------------
        button_addtransaction = tk.Button(self, text = "Add transaction", padx = 40, 
                                          command = lambda: master.switch_frame(AddTransactionFrame))
        button_addtransaction.grid(row = 2, column = 0)
        
        #Transaction list button-----------------------------------------------
        button_transactionlist = tk.Button(self, text = "Transaction list", padx = 42,
                                           command = lambda: master.switch_frame(TransactionListFrame))
        button_transactionlist.grid(row = 2, column = 1)
        
        #Quit button-----------------------------------------------------------
        button_quit = tk.Button(self, text = "Quit program", padx = 46, command = master.destroy)
        button_quit.grid(row = 2, column = 2)
