class Account:
    """
    An account has a balance and a holder.
    All accounts share a common interest rate.

    >>> a = Account('Marvin')
    >>> a.holder
    'Marvin'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Insufficient funds.'
    >>> a.balance
    10
    >>> a.interest
    0.02
    """
    interest = 0.02

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds.'
        self.balance -= amount
        return self.balance


class CheckingAccount(Account):
    """
    A bank account that earns less interest and
    charges for withdrawals.

    >>> ch = CheckingAccount('Tom')
    >>> ch.deposit(20)
    20
    >>> ch.withdraw(5)
    14
    >>> ch.interest
    0.01
    """
    interest = 0.01  # overriding
    withdraw_fee = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)


class Bank:
    """
    A bank has accounts and pays interest.

    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> jack.interest
    0.01
    >>> john.interest = 0.06
    >>> bank.pay_interest()
    >>> john.balance
    10.6
    >>> jack.balance
    5.05
    """
    def __init__(self):
        self.accounts = []  # composition

    def open_account(self, holder, amount, account_type=Account):
        account = account_type(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for account in self.accounts:
            account.deposit(account.balance * account.interest)



class SavingsAccount(Account):
    """
    A bank account that charges for deposits.

    >>> s = SavingsAccount('Tom')
    >>> s.deposit(20)
    18
    >>> s.withdraw(5)
    13
    >>> s.interest
    0.01
    """
    deposit_fee = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)


class BestAccount(CheckingAccount, SavingsAccount):
    """
    A bank account that starts off with a free dollar.

    >>> such_a_deal = BestAccount('Marvin')
    >>> such_a_deal.balance
    1
    >>> such_a_deal.deposit(20)
    19
    >>> such_a_deal.withdraw(5)
    13
    """
    def __init__(self,  account_holder):
        self.holder = account_holder
        self.balance = 1
