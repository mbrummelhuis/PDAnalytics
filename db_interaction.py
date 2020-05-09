import json
from GUI import AddTransaction

class Transaction:
    def __init__(self, date, amount, category, account, ast, comment, 
                 db_file, transaction_number):
        self.date = date
        self.amount = amount
        self.category = category
        self.account = account
        self.ast = ast
        self.comment = comment
        self.transaction_number = transaction_number
    
transaction_dict = AddTransaction.WriteToDictionaryAndReload()

with open("db.json") as open_file:
    json.dump(transaction_dict)    

        
        
