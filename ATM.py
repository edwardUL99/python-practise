import random

class ATM:
    def __init__(self, name, account, balance=0.0, overdraft=0.0):
        self.name = name
        self.pin = int (input("What pin would you like?(4 digits): "))
        self.balance = balance
        self.account = account[:1].upper() + account[1:].lower()
        self.overdraft = overdraft
        self.transHistory = []
        self.dpHistory = []
        self.login = False
        print()
        print("This is a %s Account belonging to %s\n" % (self.account,name))

    def deposit(self, amount):
        if self.account == "Current" and self.login:
            if amount >= 0:
                self.balance += amount
                self.dpHistory.append(amount)
        elif self.account == "Credit" and self.login:
            print("This is a credit account, you can not deposit funds")

    def withdraw(self, amount):
        if self.account == "Current" and self.login:
            if (amount <= self.balance and amount % 5 == 0):
                self.balance -= amount
                fifties = int (amount / 50)
                remainder = amount % 50
                twenties = int (remainder / 20)
                remainder = remainder % 20
                tens = int (remainder / 10)
                remainder = remainder % 10
                fives = int (remainder / 5)

                print("%d fifties\n%d twenties\n%d tens\n%d fives\n" % (fifties, twenties, tens, fives))
                print("Your balance is now €%d\n" % (self.balance))
                self.transHistory.append(amount)
            elif amount > self.balance:
                print('You do not have enough funds in your account to withdraw €%d as your balance is €%.02f' % (amount, self.balance))
            elif amount % 5 != 0:
                print('Please enter a multiple of 5 to withdraw')
        elif self.account == "Credit" and self.login:
            if amount % 5 == 0:
                fifties = int (amount / 50)
                remainder = amount % 50
                twenties = int (remainder / 20)
                remainder = remainder % 20
                tens = int (remainder / 10)
                remainder = remainder % 10
                fives = int (remainder / 5) 
                print("%d fifties\n%d twenties\n%d tens\n%d fives\n" % (fifties, twenties, tens, fives))
                self.overdraft += (amount + (amount * 0.20))
                print("You're bill is currently at €%.02f including interest" % (self.overdraft))

    def payBill(self, amount):
        if amount == "all" and self.login:
            self.overdraft -= self.overdraft
            print("Your bill is now €%.02f\n" % (self.overdraft))
        elif (self.account == "Credit" and self.overdraft > 0) and self.login:
             if amount <= self.overdraft:
                self.overdraft -= (amount - (amount * 0.075))
                print("Your bill is now €%.02f, including the separate payments fee at 7.5 per cent\n" % (self.overdraft))

    def viewHistory(self, choice):
        choice = choice[:1].upper() + choice[1:].lower()
        if self.login:
            if choice == "Transaction":
                print()
                print("Transaction History(most recent to the right) in euro:")
                print(self.transHistory)
            elif choice == "Deposit":
                print()
                print("Deposit History(most recent to the right) in euro:")
                print(self.dpHistory)
            else:
                print("Invalid Choice")

    def logon(self, pin):
        if pin == self.pin:
            self.login = True
            print("You are logged in\n")
        else:
            print("Your pin is incorrect\n")
        return self.login

    def logout(self):
        self.login = False
        print("You are now logged out")
                          
                



