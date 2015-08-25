# -*- coding: utf-8 -*-
import random
import string


class Account(object):
    """
    User's bank account.
    """

    number = None
    balance = None
    state = 'Open'

    def __init__(self, number, amount=0):
        self.number = number
        self.balance = amount

    def deposit(self, amount):
        """
        Put money in.
        :param amount:
        :return: balance
        """
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Take money out.
        :param amount:
        :return: balance
        """
        if self.balance < amount:
            raise Exception('Not enough money in the account.')
        else:
            self.balance -= amount
            return self.balance

    def close(self):
        if self.balance != 0:
            raise Exception('Account has a non-zero balance.')

        self.state = 'Closed'

    @staticmethod
    def generate():
        return ''.join([random.choice(string.digits) for _ in range(10)])


class Customer(object):
    """
    Bank user.
    """

    client_id = None
    client_name = None
    accounts = {}

    def __init__(self, client_id, client_name):
        self.client_id = client_id
        self.client_name = client_name

    def open_account(self):
        """
        Open a new account with 0 balance.
        :return: Account
        """

        account_number = Account.generate()
        account = Account(account_number, 0)

        self.accounts[account_number] = account
        return account

    def close_account(self, number):
        """
        Close the account.
        :param number: string account number
        """

        if number not in self.accounts:
            raise Exception('Account does not exist.')

        self.accounts[number].close()

    @property
    def name(self):
        return self.client_name
