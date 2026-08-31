from account import Account


class Transaction:
    """Represents a transaction on an account.

    Main responsibility: managing transaction information and its
    status. The status only changes through process_transaction()
    and cancel_transaction(), and processing applies the amount to
    a validated Account object.
    """

    def __init__(self, transaction_id, transaction_type, amount, description,
                 status='Pending'):
        if (isinstance(transaction_id, int) and
                not isinstance(transaction_id, bool) and transaction_id > 0):
            self.__transaction_id = transaction_id
        else:
            self.__transaction_id = 0

        if isinstance(transaction_type, str):
            self.__transaction_type = transaction_type
        else:
            self.__transaction_type = ""

        if isinstance(amount, int) and not isinstance(amount, bool) and amount > 0:
            self.__amount = amount
        else:
            self.__amount = 0

        if isinstance(description, str):
            self.__description = description
        else:
            self.__description = ""

        if isinstance(status, str):
            self.__status = status
        else:
            self.__status = "Pending"

    def process_transaction(self, account):
        if not isinstance(account, Account):
            print('Invalid account: transaction requires an Account object.')
            return
        if self.__status == 'Pending':
            if self.__transaction_type == 'Deposit':
                account.add_funds(self.__amount)
            elif self.__transaction_type == 'Withdraw':
                account.withdraw(self.__amount)
            else:
                print('Unknown transaction type')
                return
            self.__status = 'Processed'
            print('Transaction processed')
        else:
            print('Transaction cannot be processed')

    def cancel_transaction(self):
        if self.__status == 'Pending':
            self.__status = 'Cancelled'
            print('Transaction cancelled')
        else:
            print('Transaction cannot be cancelled')

    def display_information(self):
        print(f'Transaction ID: {self.__transaction_id}')
        print(f'Transaction Type: {self.__transaction_type}')
        print(f'Amount: ${self.__amount}')
        print(f'Description: {self.__description}')
        print(f'Status: {self.__status}\n')

    def get_transaction_id(self):
        return self.__transaction_id

    def get_transaction_type(self):
        return self.__transaction_type

    def get_amount(self):
        return self.__amount

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def set_description(self, new_description):
        if isinstance(new_description, str):
            self.__description = new_description
        else:
            print('Invalid description: change rejected.')

    def __str__(self):
        return (f"{self.__transaction_id} has the transaction type: "
                f"{self.__transaction_type} with the amount: {self.__amount}, "
                f"description: {self.__description}, "
                f"and the status: {self.__status}")

    def __repr__(self):
        return (f"Transaction(transaction_id={self.__transaction_id}, "
                f"transaction_type='{self.__transaction_type}', "
                f"amount={self.__amount}, description='{self.__description}', "
                f"status='{self.__status}')")
