class Account:

    def __init__(self, accNum, custName):
        self.accountNumber = accNum
        self.customerName = custName
        self.accountBalance = 0
        self.accountType = None

    def getBalance(self):
        return self.accountBalance

    def getAccountType(self):
        return self.accountType

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


def main():
    a = Account(1, "Kira")
    b = Account(2, "Ed")

    a.depositMoney(230)
    b.depositMoney(500)

    a.withdrawMoney(50)
    b.withdrawMoney(100)

main()
