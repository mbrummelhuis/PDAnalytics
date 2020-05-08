import tkinter as tk
from datetime import datetime


class App(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Personal Data Analytics")
        self._frame = None
        self.switch_frame(MainMenu)
    
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        
        if not self._frame == None:
            self._frame.destroy()
        
        self._frame = new_frame
        self._frame.grid()
    
class MainMenu(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        label_intro = tk.Label(self, text = "Welcome to the Personal Data Analytics dashboard!")
        label_intro.grid(row = 0, column = 0, columnspan = 3)
    
        #Add transaction button
        button_addtransaction = tk.Button(self, text = "Add transaction", padx = 40, 
                                          command = lambda: master.switch_frame(AddTransaction))
        button_addtransaction.grid(row = 2, column = 0)
        
        #Transaction list button
        button_transactionlist = tk.Button(self, text = "Transaction list", padx = 42,
                                           command = lambda: master.switch_frame(TransactionList))
        button_transactionlist.grid(row = 2, column = 1)
        
        #Quit button
        button_quit = tk.Button(self, text = "Quit program", padx = 46, command = master.destroy)
        button_quit.grid(row = 2, column = 2)

class AddTransaction(tk.Frame):
    
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        
        text_date = tk.Label(self, text="Date")
        text_date.grid(row=0, column = 0)
        
        #Set date of today for insert on entry line
        today = datetime.today()
        date = today.strftime("%d/%m/%Y")
        
        entry_date = tk.Entry(self, width = 50)
        entry_date.insert(0,date)
        entry_date.grid(row = 0, column = 1)
        transaction_date = entry_date.get()
        
        
        #Ask for amount input (optional: tweak so it says a euro sign or smth)
        text_amount = tk.Label(self, text = "Amount")
        text_amount.grid(row = 1, column = 0)
        
        entry_amount = tk.Entry(self, width = 50)
        entry_amount.grid(row = 1, column = 1)
        transaction_amount = entry_amount.get()
        
        #Ask for category input (take from list of categories) DDL
        text_category = tk.Label(self, text = "Category")
        text_category.grid(row = 2, column = 0)
        
        entry_category = tk.Entry(self, width = 50)
        entry_category.grid(row = 2, column = 1)
        transaction_category = entry_category.get()
        
        #Ask for account input (take from list of available accounts) DDL
        text_account = tk.Label(self, text = "Account")
        text_account.grid(row = 3, column = 0)
        
        entry_account = tk.Entry(self, width = 50)
        entry_account.grid(row = 3, column = 1)
        transaction_account = entry_account.get()
        
        #Ask for type input (credit, debit, transfer) DDL
        text_ast = tk.Label(self, text = "D/C/T")
        text_ast.grid(row = 4, column = 0)
        
        tkvar = tk.StringVar(master)
        choices = ['Add', 'Substract', 'Transfer']
        entry_ast = tk.OptionMenu(self,tkvar, *choices)
        entry_ast.grid(row = 4, column = 1)
        
        #Ask for additional comments (not necessary, don't check)
        text_comment = tk.Label(self, text = "Comments")
        text_comment.grid(row = 5, column = 0)
        
        entry_comment = tk.Entry(self, width = 50)
        entry_comment.grid(row = 5, column = 1)
        transaction_account = str(entry_comment.get())
        
        #Back to main menu button
        button_mainmenu = tk.Button(self, text = "Back",
                                    command = lambda: master.switch_frame(MainMenu))
        button_mainmenu.grid(row = 6, column = 2)  
        
        #Confirm button
        button_mainmenu = tk.Button(self, text = "Confirm")
        button_mainmenu.grid(row = 6, column = 1)  
        
class TransactionList(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        #Back to main menu button
        button_mainmenu = tk.Button(self, text = "Back",
                                    command = lambda: master.switch_frame(MainMenu))
        button_mainmenu.grid(row = 5, column = 2)