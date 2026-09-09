class Account:
    """Represents a financial account.

    Main responsibility: managing account information and balance
    behaviour. The balance can only change through add_funds() and
    withdraw(), which validate the amount and (for withdrawals) the
    available funds. Each successful deposit or withdrawal creates a
    transaction record which the account creates and owns, making
    Account and Transaction a composition relationship.

    Topic 4 update: read access is now provided through properties
    (account_no, account_type, current_balance, date_created and
    transactions) so outside code can use attribute-style syntax
    instead of getter and setter calls.
    """

    def __init__(self, account_no, account_type, current_balance, date_created):

        if isinstance(account_no, int) and not isinstance(account_no, bool) and account_no > 0:
            self.__account_no = account_no
        else:
            self.__account_no = 0

        if isinstance(account_type, str):
            self.__account_type = account_type
        else:
            self.__account_type = ""

        if isinstance(date_created, str):
            self.__date_created = date_created
        else:
            self.__date_created = ""

        if isinstance(current_balance, int) and not isinstance(current_balance, bool) and current_balance >= 0:
            self.__current_balance = current_balance
        else:
            self.__current_balance = 0

        self.__transactions = []
        self.__next_transaction_id = 1

    def add_funds(self, amount):
        if not (isinstance(amount, int) and not isinstance(amount, bool)):
            print("Invalid amount: must be a number.")
            return
        if amount <= 0:
            print("Invalid amount: must be positive.")
            return
        self.__current_balance = self.__current_balance + amount
        self.__create_transaction('Deposit', amount, self.__current_balance)
        print(f'New Balance after Deposit: ${self.__current_balance}\n'
              'Deposited Successfully\n')

    def withdraw(self, amount):
        if not (isinstance(amount, int) and not isinstance(amount, bool)):
            print("Invalid amount: must be a number.")
            return
        if amount <= 0:
            print("Invalid amount: must be positive.")
            return
        if self.__current_balance < amount:
            print('Not enough funds for withdrawal\n')
            return
        self.__current_balance = self.__current_balance - amount
        self.__create_transaction('Withdraw', amount, self.__current_balance)
        print(f'New Balance after Withdrawal: ${self.__current_balance}\n'
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
        if isinstance(new_account_type, str):
            self.__account_type = new_account_type
        else:
            print('Invalid account type: change rejected.')

    def get_transactions(self):
        return list(self.__transactions)

    account_no = property(get_account_no)
    account_type = property(get_account_type, set_account_type)
    current_balance = property(get_current_balance)
    date_created = property(get_date_created)
    transactions = property(get_transactions)

    def __create_transaction(self, transaction_type, amount,
                             resulting_balance):
        """Create, record, and return a transaction for a completed movement of money.

        This private helper is reused by add_funds() and withdraw(), and
        assigns each transaction a unique identifier.
        """
        from transaction import Transaction
        transaction = Transaction(
            self.__next_transaction_id, transaction_type, amount,
            f'{transaction_type} on account {self.__account_no}',
            status='Processed', resulting_balance=resulting_balance)
        self.__next_transaction_id = self.__next_transaction_id + 1
        self.__transactions.append(transaction)
        return transaction

    def display_information(self):
        print(f'Account Number:{self.__account_no}')
        print(f'Account Type:{self.__account_type}')
        print(f'Current Balance: ${self.__current_balance}')
        print(f'Date created:{self.__date_created}')
        print(f'Transaction records:{len(self.__transactions)}\n')

    def __str__(self):
        return (f"Account {self.__account_no} is a {self.__account_type} account "
                f"with a current balance of {self.__current_balance}, "
                f"created on {self.__date_created}")

    def __repr__(self):
        return (f"Account(account_no={self.__account_no}, "
                f"account_type='{self.__account_type}', "
                f"current_balance={self.__current_balance}, "
                f"date_created='{self.__date_created}')")
