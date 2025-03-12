class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully!")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount 
            print(f"{amount} withdrawn successfully!")
        else:
            print("Invalid withdrawal amount or insufficient balance.")  

client_1 = BankAccount('haris', 50000)
client_1.withdraw(49999)
