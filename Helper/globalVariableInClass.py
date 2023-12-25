class Bank:
    def __init__(self):
        self._balance = 0
        
    @property
    def balance(self):
        return self._balance
    
    def withdraw(self,n):
        self._balance = self._balance - n
    
    def deposit(self,n):
        self._balance = self._balance + n
        
    def __str__(self):
        return f"you have ${self._balance} in your bank account"


def main():
    bank = Bank()
    print(bank)
    bank.deposit(200)
    bank.withdraw(100)
    print(bank)
    

if __name__ == "__main__":
    main()