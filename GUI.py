import tkinter as tk
from datetime import datetime
import json


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
    
class MainMenu(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        label_intro = tk.Label(self, text = "Welcome to the Personal Data Analytics dashboard!",
                               bg = "grey", fg = "black", width = "90", height = 3)
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
        
        #Date input------------------------------------------------------------
        text_date = tk.Label(self, text="Date")
        text_date.grid(row=0, column = 0)
        self.info_date = tk.StringVar()
    
        today = datetime.today()#Set date of today for insert on entry line
        date = today.strftime("%d/%m/%Y")
        
        entry_date = tk.Entry(self, textvariable = self.info_date, width = 50)
        entry_date.insert(0,date)
        entry_date.grid(row = 0, column = 1)
        
        #Ask for amount input--------------------------------------------------
        #(optional: tweak so it says a euro sign or smth)
        text_amount = tk.Label(self, text = "Amount")
        text_amount.grid(row = 1, column = 0)
        self.info_amount = tk.DoubleVar()
        
        entry_amount = tk.Entry(self, textvariable= self.info_amount, width = 50)
        entry_amount.grid(row = 1, column = 1)
        
        #Ask for category input------------------------------------------------
        #(take from list of categories) DDL
        text_category = tk.Label(self, text = "Category")
        text_category.grid(row = 2, column = 0)
        self.info_category = tk.StringVar()
        
        entry_category = tk.Entry(self, textvariable = self.info_category, width = 50)
        entry_category.grid(row = 2, column = 1)
        
        #Ask for account input------------------------------------------------- 
        #(take from list of available accounts) DDL
        text_account = tk.Label(self, text = "Account")
        text_account.grid(row = 3, column = 0)
        self.info_account = tk.StringVar()
        
        entry_account = tk.Entry(self, textvariable = self.info_account, width = 50)
        entry_account.grid(row = 3, column = 1)
        
        #Ask for type input----------------------------------------------------
        #(credit, debit, transfer) DDL
        text_ast = tk.Label(self, text = "D/C/T")
        text_ast.grid(row = 4, column = 0)
        self.info_ast = tk.StringVar()
        
        choices = ['Add', 'Substract', 'Transfer']
        self.info_ast.set('Substract')
        entry_ast = tk.OptionMenu(self,self.info_ast, *choices)
        entry_ast.grid(row = 4, column = 1)
        
        #Make so that if 'transfer' is selected, a field for fromaccount appears 
        #And when transfer is not selected, the field disappears
        
#        if tkvar == 'Transfer' and transfer == False:
#            master.switch_frame(AddTransaction)
#            text_fromaccount = tk.Label(self, text = "From account")
#            text_fromaccount.grid(row = 5, column = 0)
            
#            entry_fromaccount = tk.Entry(self, width = 50)
#            entry_fromaccount.grid(row = 3, column = 1)
#            transaction_fromaccount = entry_fromaccount.get()
        
#        elif tkvar == 'Subtract' or 'Add':
#            master.switch_frame(AddTransaction)
#            transaction_fromaccount = 'yes'
#            pass
        
        #Ask for additional comments-------------------------------------------
        #(not necessary, don't check)
        text_comment = tk.Label(self, text = "Comments")
        text_comment.grid(row = 6, column = 0)
        self.info_comment = tk.StringVar()
        
        entry_comment = tk.Entry(self, textvariable = self.info_comment, width = 50)
        entry_comment.grid(row = 6, column = 1)
        
        #Back to main menu button----------------------------------------------
        button_mainmenu = tk.Button(self, text = "Back",
                                    command = lambda: master.switch_frame(MainMenu))
        button_mainmenu.grid(row = 7, column = 2)  
        
        #Confirm button--------------------------------------------------------
        button_mainmenu = tk.Button(self, text = "Confirm",
                                    command = lambda: self.SaveToDatabase(master))
        button_mainmenu.grid(row = 7, column = 1)  
        
    def SaveToDatabase(self,master):
        
        transaction_dict = dict([
            ("date",self.info_date.get()),
            ("amount",self.info_amount.get()),
            ("category",self.info_category.get()),
            ("account",self.info_account.get()),
#            ("from_account",self.transaction_fromaccount)
            ("ast",self.info_ast.get()),
            ("comment",self.info_comment.get()),
            ("number",None)
            ])
        
        print(transaction_dict)
        
        f = open("db.json","w")
        json.dumps(transaction_dict)
        f.close()
        
        print("Transaction saved to database")
        
        master.switch_frame(AddTransaction)
        
class TransactionList(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        #Back to main menu button
        button_mainmenu = tk.Button(self, text = "Back",
                                    command = lambda: master.switch_frame(MainMenu))
        button_mainmenu.grid(row = 5, column = 2)