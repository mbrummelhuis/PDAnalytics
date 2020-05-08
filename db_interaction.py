import json

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
    
    def WriteToDatabase(self):
        transaction_dict = dict([
            ("date",self.date),
            ("amount",self.amount),
            ("category",self.category),
            ("account",self.account),
            ("ast",self.ast),
            ("comment",self.comment)
            ])
        
        json.dumps(transaction_dict)
        return
    
    def PullFromDatabase(self, db_file):
        json.loads(db_file)
        
        
