class BankAccount():
    def __init__(self, number , name, balance):
        if balance < 0:
            raise ValueError("negative initial balance")
        self.account__number = number
        self.__name = name
        self.__balance = balance
    
    def id(self):
        return self.account__number

    def deposit(self,amount):
        self.__balance += amount
    
    def withdraw(self,amount):
        result = False
        if self.__balance - amount >= 0:
            self.__balance -=amount
            result = True
        return result

    def __str__(self):
        out = "{}{}{}".format(self.account__number, self.__name, self.__balance)
        return out
   
def open_database(filename, db):
    try:
        with open('C:\\Users\\Home-PC\\Desktop\\happy\\{}'.format(filename))as lines:
            for line in lines:
                line.strip()
                name,account_number,balance=line.split(',')
                print(account_number,type(account_number))
                print(balance,type(balance))
                db.append(BankAccount(int(account_number),name,int(balance)))
    except Exception as f:
        print("error in file",f,type(f))

def print_database(db):
     for acct in db:
         print(acct)
         
            
def get_account(db, account_number):
    for  acct in db:
         if acct.id() == account_number:
             return acct
def main():
    
    database=[]
    try:
        open_database("accountdata.txt",database)
        print_database(database)
        print("........")
        customer = get_account(database,129)
        if customer:
            print("account 129 before it deposit of $100:",end="")
            print(customer)
            customer.deposit(100)
            print("account 129 after it deposit of $100:",end="")
            print(customer)
            print("........")
            print("account 129 before it deposit of $500:",end="")
            print(customer)
            customer.withdraw(500)
            print("account 129 after it deposit of $500:",end="")
            print(customer)
            print("........")
            print("account 129 before it deposit of $8000:",end="")
            print(customer)
            customer.withdraw(8000)
            print("account 129 after withdraw of $8000",end="")
            print(customer)
    except Exception:
        print("error in data base")
        raise
main()        
                
                

                
                

                 
                    

                
                
                
                

                
             
             
                          
                
        
        
        
        
        
        
        
        
        
