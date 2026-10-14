class Bank:
    def __init__(self, accountnumber, balance, branch, balans):
        self._account = accountnumber            
        self._balance = balance           
        self._branch = branch     
        self._balans = balans

    def _displayBalanceAndBranch(self): 
        print("Balance:", self._balance)
        print("Branch:", self._branch)


class Money(Bank):
    def displayDetails(self):
        print("Account number:", self._account)  
        self._displayBalanceAndBranch() 


obj = Money("676169", 670.00, "LandBank", f"{balans}" )
obj.displayDetails()

balans = int(input("Update current balance: "))
if balans > -1:
  print(f"your new balance is: {balans} ")
else:
  print("invalid input! balance can not be negative")
