
# Static method is a method that belongs to a class rather than an instance of the class.
# Static methods are defined using the @staticmethod decorator and do not take self as the first parameter

class BankAccount:
    MIN_BALANCE = 100  # Class variable; captilalize constants in python

    def __init__(self, owner, balance = 0) :
        self.owner = owner
        self._balance = balance # creating protected instance attribute
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance is {self._balance}.")
        else:
            print("Deposit amount must be positive.")

    @staticmethod
    def isvalid_interest_rate(rate):
        return 0 <= rate <= 5
    
account = BankAccount("Alice", 500)
account.deposit(250)

print(BankAccount.isvalid_interest_rate(3)) # True
print(BankAccount.isvalid_interest_rate(7)) # True

# Both static and instance methods are stored in the class itself, not in each individual instance
# therefore, there is memory efficiency (one copy in memory)
# Static methods are ideal for utility functions or tasks related to a class's domain that don't need access to instance or class data

