class Transaction:
    def __init__(self, transaction_id, transaction_type, amount, description,
                 status='Pending'):
        self.__transaction_id = transaction_id
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__description = description
        self.__status = status

    def process_transaction(self, account):
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

    def update_transaction(self, description):
        self.__description = description
        print('Transaction description updated')

    def display_information(self):
        print(f'Transaction ID: {self.__transaction_id}')
        print(f'Transaction Type: {self.__transaction_type}')
        print(f'Amount: ${self.__amount}')
        print(f'Description: {self.__description}')
        print(f'Status: {self.__status}\n')

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
