class BankAccount:
    def __init__(self, accountHolder):
        self._balance = 0
        self._name = accountHolder
        with open(self._name + "ledger.txt", "w") as ledgerFile:
            ledgerFile.write("Balance is 0\n")

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            return
        self._balance += amount
        with open(self._name + "ledger.txt", "a") as ledgerFile:
            ledgerFile.write("Deposit " + str(amount) + "\n")

    def withdraw(self, amount):
        if self._balance < amount or amount < 0:
            return
        self._balance -= amount
        with open(self._name + "ledger.txt", "a") as ledgerFile:
            ledgerFile.write("Withdraw " + str(amount) + "\n")
            ledgerFile.write("Balance " + str(self._balance) + "\n")
