class Account:

    def __init__(self, accNum, custName):
        self.accountNumber = accNum
        self.customerName = custName
        self.accountBalance = 0
        self.interestRate = 0


    def getBalance(self):
        return self.accountBalance

    def getInterestRate(self):
        return self.interestRate

    def getCustomerName(self):
        return self.customerName

    def withdrawMoney(self, amount):
        if amount < self.accountBalance:
            print("You have withdrawn £" + str(amount))
            self.accountBalance -= amount
        else:
            print("You do not have enough funds to withdraw that")

    def depositMoney(self, amount):
        if amount > 0:
            print("You have deposited £" + str(amount))
            self.accountBalance += amount
        else:
            print("Your deposit must be greater than 0")

# ---------------------------------------------------------------------------

class SavingsAccount(Account):

    def __init__(self, accNum, custName, setupBalance = 0):
        super().__init__(accNum, custName)
        self.accountType = "Savings"
        self.balance = setupBalance
        self.interestRate = 1.3

    def withdrawMoney(self, amount):
        print("You cannot withdraw funds from a savings account, only transfer funds")


    def transferFunds(self, transferTarget, amount):
        transferTarget.accountBalance += amount
        print("You have transfered £" + str(amount) + " to", transferTarget.getCustomerName())

# ---------------------------------------------------------------------------

class CurrentAccount(Account):

    def __init__(self, accNum, custName, cardNum, setupBalance = 0):
        super().__init__(accNum, custName)
        self.accountType = "Current Account"
        self.accountBalance = setupBalance
        self.interestRate = 0.5
        self.cardNumber = cardNum

    def withdrawMoney(self, amount, cardNum):
        if self.checkCardNum(cardNum):
            self.accountBalance -= amount
            print("You have withdrawn £" + str(amount))
        else:
            print("Your card number is not correct")

    def checkCardNum(self, cardNum):
        return cardNum == self.cardNumber

# ---------------------------------------------------------------------------

class StudentAccount(CurrentAccount):

    def __init__(self, accNum, custName, cardNum, setupBalance = 0):
        super().__init__(accNum, custName, cardNum, setupBalance)
        self.interestRate = 0.7
        self.accountBalance += 50

# ---------------------------------------------------------------------------

def main():
    save = SavingsAccount(1, "Ollie", 200)

    current = CurrentAccount(2, "Keith", 123, 500)

    student = StudentAccount(3, "Jack", 456, 1000)

    save.depositMoney(100)
    save.withdrawMoney(100)
    save.transferFunds(current, 50)

    print(current.getBalance())
    # Correct
    current.withdrawMoney(100, 123)
    # Incorrect
    current.withdrawMoney(100, 124)

    print(student.getBalance())

main()
