import json

class Transaction:
    def __init__(self):
        self.date
        self.amount
        self.category
        self.account
        self.ast
        self.comment
        self.number
    
    def saveToDatabase(self):
        #Open database file
        with open("db.json") as f:
            data = json.load(f)
        
        #Create new transaction ID by adding one to last transaction ID
        entries = len(data['transactions']) - 1
        self.number = data['transactions'][entries]['number'] + 1
        
        #Create dict with all transaction data
        transaction_dict = dict([
            ("date",self.date),
            ("amount",self.amount),
            ("category",self.category),
            ("account",self.account),
#            ("from_account",self.transaction_fromaccount)
            ("ast",self.ast),
            ("comment",self.comment),
            ("number",self.number)
            ])
        
        #Add dictionary as json object to the array 'transactions'
        data['transactions'].append(transaction_dict)
        
        #Put json object back in database file
        with open("db.json","w") as f:
            json.dump(data,f, indent = 2)
            
        print("Database updated with new transaction") #Check
    
    def selectFromDatabase(self):
        
        pass