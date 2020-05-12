from datetime import datetime
import tkinter as tk
import MainMenuFrame

class AddTransactionFrame(tk.Frame):
    
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        
        #Message top of the screen---------------------------------------------
        label_intro = tk.Label(self, text = "Add a transaction",
                               bg = "grey", fg = "black", width = "90", height = 3)
        label_intro.grid(row = 0, column = 0, columnspan = 3)
    
        
        #Date input------------------------------------------------------------
        text_date = tk.Label(self, text="Date")
        text_date.grid(row=1, column = 0)
        self.info_date = tk.StringVar()
    
        today = datetime.today()#Set date of today for insert on entry line
        date = today.strftime("%d/%m/%Y")
        
        entry_date = tk.Entry(self, textvariable = self.info_date, width = 50)
        entry_date.insert(0,date)
        entry_date.grid(row = 1, column = 1)
        
        #Ask for amount input--------------------------------------------------
        #(optional: tweak so it says a euro sign or smth)
        text_amount = tk.Label(self, text = "Amount")
        text_amount.grid(row = 2, column = 0)
        self.info_amount = tk.DoubleVar()
        
        entry_amount = tk.Entry(self, textvariable= self.info_amount, width = 50)
        entry_amount.grid(row = 2, column = 1)
        
        #Ask for category input------------------------------------------------
        #(take from list of categories) DDL
        text_category = tk.Label(self, text = "Category")
        text_category.grid(row = 3, column = 0)
        self.info_category = tk.StringVar()
        
        entry_category = tk.Entry(self, textvariable = self.info_category, width = 50)
        entry_category.grid(row = 3, column = 1)
        
        #Ask for account input------------------------------------------------- 
        #(take from list of available accounts) DDL
        text_account = tk.Label(self, text = "Account")
        text_account.grid(row = 4, column = 0)
        self.info_account = tk.StringVar()
        
        entry_account = tk.Entry(self, textvariable = self.info_account, width = 50)
        entry_account.grid(row = 4, column = 1)
        
        #Ask for type input----------------------------------------------------
        #(credit, debit, transfer) DDL can make this more efficient by assigning it to an integer value.
        text_ast = tk.Label(self, text = "D/C/T")
        text_ast.grid(row = 5, column = 0)
        self.info_ast = tk.StringVar()
        
        choices = ['Add', 'Substract', 'Transfer']
        self.info_ast.set('Substract')
        entry_ast = tk.OptionMenu(self,self.info_ast, *choices)
        entry_ast.grid(row = 5, column = 1)
        
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
        text_comment.grid(row = 7, column = 0)
        self.info_comment = tk.StringVar()
        
        entry_comment = tk.Entry(self, textvariable = self.info_comment, width = 50)
        entry_comment.grid(row = 7, column = 1)
        
        #Back to main menu button----------------------------------------------
        button_mainmenu = tk.Button(self, text = "Back",
                                    command = lambda: master.switch_frame(MainMenuFrame.MainMenu))
        button_mainmenu.grid(row = 8, column = 2)  
        
        #Confirm button--------------------------------------------------------
        button_mainmenu = tk.Button(self, text = "Confirm",
                                    command = lambda: self.SaveToDatabase(master))
        button_mainmenu.grid(row = 8, column = 1)
