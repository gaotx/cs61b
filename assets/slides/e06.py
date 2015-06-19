# Bound Methods

class Adder:
    """An example class that adds two numbers.

    >>> seven = Adder(6, 1)
    >>> seven.total()
    7
    """
    def __init__(self, a, b):
        self.a, self.b = a, b

    def total(self):
        return self.a + self.b

# Implementing an Object System

def make_instance(cls):
    """Return a new instance of the `cls` class."""
    attributes = {} # instance attributes, e.g. {'a': 6, 'b': 1}

    def get_value(name):
        if name in attributes: # name is an instance attribute
            return attributes[name]
        value = cls['get'](name) # look up name in class
        return (bind_method(value, instance) if callable(value) else value)

    def set_value(name, value):
        attributes[name] = value # assignment creates/modifies instance attrs

    instance = {'get': get_value, 'set': set_value} # dispatch dictionary
    return instance

def bind_method(function, instance):
    return lambda *args: function(instance, *args)

def make_class(attributes={}):
    def get_value(name):
        if name in attributes: # name is a class attribute
            return attributes[name]
        else:
            return None

    def set_value(name, value):
        attributes[name] = value

    def __new__(*args):
        instance = make_instance(cls)
        return init_instance(instance, *args)

    cls = {'get': get_value, 'set': set_value, 'new': __new__}
    return cls

def init_instance(instance, *args):
    init = instance['get']('__init__')
    if callable(init):
        init(*args)
    return instance

def make_account_class():
    """Return the Account class, which has deposit and withdraw methods.

    >>> Account = make_account_class()
    >>> brian_acct = Account['new']('Brian')
    >>> brian_acct['get']('holder')
    'Brian'
    >>> brian_acct['get']('interest')
    0.02
    >>> brian_acct['get']('deposit')(20)
    20
    >>> brian_acct['get']('withdraw')(5)
    15

    >>> brian_acct['get']('balance')
    15
    >>> brian_acct['set']('interest', 0.08)
    >>> Account['get']('interest')
    0.02
    >>> brian_acct['get']('interest')
    0.08
    """
    interest = 0.02

    def __init__(self, account_holder):
        self['set']('balance', 0)
        self['set']('holder', account_holder)

    def deposit(self, amt):
        balance = self['get']('balance') + amt
        self['set']('balance', balance)
        return self['get']('balance')

    def withdraw(self, amt):
        balance = self['get']('balance')
        if amt > balance:
            return 'Insufficient funds'
        self['set']('balance', balance - amt)
        return self['get']('balance')

    return make_class(locals())

Account = make_account_class()

# Implementing Inheritance

def make_class(attributes={}, base_class=None):
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)
        else:
            return None

    def set_value(name, value):
        attributes[name] = value

    def __new__(*args):
        instance = make_instance(cls)
        return init_instance(instance, *args)

    cls = {'get': get_value, 'set': set_value, 'new': __new__}
    return cls

def make_checking_account_class():
    """Return the CheckingAccount class, which imposes a $1 withdrawal fee.

    >>> john_acct = CheckingAccount['new']('John')
    >>> john_acct['get']('interest')
    0.01
    >>> john_acct['get']('deposit')(20)
    20
    >>> john_acct['get']('withdraw')(5)
    14
    """
    interest = 0.01
    withdraw_fee = 1

    def withdraw(self, amount):
        fee = self['get']('withdraw_fee')
        return Account['get']('withdraw')(self, amount + fee)

    return make_class(locals(), Account)

CheckingAccount = make_checking_account_class()

def dict_demo():
    """
    >>> seven = Adder(6, 1)
    >>> seven.__dict__ == {'a': 6, 'b': 1}
    True
    >>> seven.__dict__['a']
    6
    >>> seven.__dict__['b']
    1
    >>> seven.__dict__['a'] += 1
    >>> seven.__dict__['a']
    7
    >>> 'total' in list(Adder.__dict__.keys())
    True
    >>> Adder.__dict__['total'] is Adder.total
    True
    >>> Adder.__dict__['total'](seven)
    8
    """
    pass
