class Bank:

    def __init__(self, balance):
        self.balance=balance
        self.length=len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1<=self.length and account2<=self.length and self.balance[account1-1]>=money:
            self.balance[account1-1]-=money
            self.balance[account2-1]+=money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account<=self.length:
            self.balance[account-1]+=money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account<=self.length and self.balance[account-1]>=money:
            self.balance[account-1]-=money
            return True
        return False
    def show(self):
        print(self.balance)

s=Bank([10, 100, 20, 50, 30])
s.withdraw(3, 10)
s.transfer(5, 1, 20)
s.deposit(5, 20)
s.show()
