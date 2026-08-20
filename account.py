class Account:
    def __init__(self, account_no, account_type, current_balance, date_created):
        self.__account_no = account_no
        self.__account_type = account_type
        self.__current_balance = current_balance
        self.__date_created = date_created

    def add_funds(self, amount):
        self.__current_balance = self.__current_balance + amount
        print(f'New Balance after Deposit: ${self.__current_balance}\n'
              'Deposited Successfully\n')

    def withdraw(self, amount):
        if self.__current_balance < amount:
            print('Not enough funds for withdrawal\n')
        else:
            self.__current_balance = self.__current_balance - amount
            print(f'New Balance after Withdrew: ${self.__current_balance}\n'
                  'Withdrawal Successfully\n')

    def get_account_no(self):
        return self.__account_no

    def get_account_type(self):
        return self.__account_type

    def get_current_balance(self):
        return self.__current_balance

    def get_date_created(self):
        return self.__date_created

    def set_account_type(self, new_account_type):
        self.__account_type = new_account_type

    def display_information(self):
        print(f'Account Number:{self.__account_no}')
        print(f'Account Type:{self.__account_type}')
        print(f'Current Balance: ${self.__current_balance}')
        print(f'Date created:{self.__date_created}\n')

    def __str__(self):
        return (f"Account {self.__account_no} is a {self.__account_type} account "
                f"with a current balance of {self.__current_balance}, "
                f"created on {self.__date_created}")

    def __repr__(self):
        return (f"Account(account_no={self.__account_no}, "
                f"account_type='{self.__account_type}', "
                f"current_balance={self.__current_balance}, "
                f"date_created='{self.__date_created}')")
