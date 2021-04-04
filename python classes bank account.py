class BankAccount:
    """"An exemplary class to hold bank account details  of savings, current, loan accounts """

    def __init__(self, name, accountNumber, openingBalance, typeOfAccount):
        self.name = name
        self.accountNumber =accountNumber
        self.openingBalance =openingBalance
        self.typeOfAccount = typeOfAccount

    def __str__(self):
        return 'account number :' + self.accountNumber + ' has total balance : ' + str(self.openingBalance)

    def deposit(self, amount_diposited):
        self.openingBalance += amount_diposited
        return self.openingBalance

    def withdrawn(self, amount_withdrawn):
        self.openingBalance -= amount_withdrawn
        return self.openingBalance

    def get_balance(self):
        return self.openingBalance


a1 = BankAccount('rayappan', '123',  10.55, 'current')
a2 = BankAccount('Bigil','456',  13.65, 'savings')
a3 = BankAccount('Anbu', '789',  5.00, 'savings')

print(a1)
a1.deposit(5.55)
print(a1)
a2.withdrawn(3.45)
print(a2)
print(a3.withdrawn(2))
print(a3.get_balance())