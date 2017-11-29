class Account:

    def __init__(self, accNum, custName):
        self.accountNumber = accNum
        self.customerName = custName
        self.accountBalance = 0

    def getBalance(self):
        return self.accountBalance

    def withdrawMoney(self, amount):
        if (amount < self.accountBalance):
            print("You have withdrawn £" + amount)
            self.accountBalance -= amount
        else:
            print("You do not have enough funds to withdraw that")

    def depositMoney(self, amount):
        if (amount > 0):
            print("You have deposited £" + amount)
            self.accountBalance += amount
        else:
            print("Your deposit must be greater than 0")


class SavingsAccount(Account):

    def __init__(self, accNum, custName, intRate):
        super().__init__(accNum, custName)
        self.accountType = "Savings"
        self.interestRate = intRate


    def withdrawMoney(self, amount):
        print("You cannot withdraw funds from a savings account, only transfer funds")



class CurrentAccount(Account):



class StudentAccount(CurrentAccount):






'''
TO DO - 
Add in account types
Add in interest rates for account types
Add in different features for account types
Tidy up
Done
'''

def main():
    a = Account(1, "Kira")
    b = Account(2, "Ed")

    a.depositMoney(230)
    b.depositMoney(500)

    a.withdrawMoney(50)
    b.withdrawMoney(100)

main()
