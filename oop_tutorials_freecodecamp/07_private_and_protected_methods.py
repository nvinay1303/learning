

class BankAccount:
    MIN_BALANCE = 100  # Class variable; captilalize constants in python

    def __init__(self, owner, balance = 0) :
        self.owner = owner
        self._balance = balance # creating protected instance attribute
    
    def deposit(self, amount):
        if self._validate(amount):
            self._balance += amount
            self.__log_transaction("DEPOSIT", amount)
        else:
            print("Deposit amount must be positive.")

    def _validate(self, amount):
        print("Validating deposit amount...")
        return amount > 0 and (self._balance - amount) >= BankAccount.MIN_BALANCE
    
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging transaction type {transaction_type} of amount: {amount}")


    @staticmethod
    def isvalid_interest_rate(rate):
        return 0 <= rate <= 5
    
account = BankAccount("Alice", 500)
account.deposit(250)
account._validate(100)  # This will work, but is discouraged
# account.__log_transaction("WITHDRAW", 100)  # This will raise an AttributeError