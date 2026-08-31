from client import Client
from account import Account
from transaction import Transaction
from branch import Branch

client_1 = Client(23344, 'Lui', 'Gallarello', 'lui@gmail.com', 'Adelaide')
client_2 = Client(24355, 'Fahim', 'Dayhan', 'fahim@gmail.com', 'Adelaide')
client_3 = Client(34222, 'Don', 'Cucurella', 'don@yahoo.com', 'Sydney')

account = Account(433133, 'Savings', 45, '3/4/2026')
account_2 = Account(633130, 'Spending', 4500, '3/4/2023')
account_3 = Account(743130, 'Savings', 500, '5/4/2020')

transaction = Transaction(4760, 'Withdraw', 50, 'Paycheck withdrawal')
transaction_2 = Transaction(6543, 'Deposit', 500, 'Paycheck deposit')
transaction_3 = Transaction(8812, 'Deposit', 250, 'Birthday gift')

branch = Branch(101, 'Adelaide Central', 'Adelaide', '08 8123 4500', True)
branch_2 = Branch(102, 'Glenelg', 'Glenelg', '08 8234 9988')
branch_3 = Branch(103, 'Sydney City', 'Sydney', '02 9000 1234', True)

print('====================CLIENTS BEFORE UPDATE====================')
client_1.show_contact_info()
client_2.show_contact_info()
client_3.show_contact_info()

client_2.set_email('fahim.dayhan@yahoo.com')
client_2.set_address('Mawson Lakes')

print('====================CLIENTS AFTER UPDATE====================')

client_1.show_contact_info()
client_2.show_contact_info()
client_3.show_contact_info()

print(client_1)
print(client_2)
print(client_3)
print()
print(repr(client_1))
print(repr(client_2))
print(repr(client_3))

print('====================ACCOUNTS BEFORE TRANSACTIONS====================')

account.display_information()
account_2.display_information()
account_3.display_information()

account.add_funds(50)
account_2.withdraw(400)
account_3.add_funds(500)

print('====================TRANSACTIONS BEFORE METHODS====================')

transaction.display_information()
transaction_2.display_information()
transaction_3.display_information()

transaction.process_transaction(account)
transaction_2.cancel_transaction()

transaction_3.set_description('Updated Birthday Gift Deposit')

print('====================TRANSACTIONS AFTER METHODS====================')

transaction.display_information()
transaction_2.display_information()
transaction_3.display_information()

print('====================ACCOUNTS AFTER TRANSACTIONS====================')

account.display_information()
account_2.display_information()
account_3.display_information()

print(account)
print(account_2)
print(account_3)
print()
print(repr(account))
print(repr(account_2))
print(repr(account_3))

print('====================BRANCHES BEFORE METHODS====================')

branch.display_information()
branch_2.display_information()
branch_3.display_information()

branch.close_branch()
branch_2.open_branch()
branch_3.update_phone_number('02 9000 5678')

print('====================BRANCHES AFTER METHODS====================')

branch.display_information()
branch_2.display_information()
branch_3.display_information()

print(branch)
print(branch_2)
print(branch_3)
print()
print(repr(branch))
print(repr(branch_2))
print(repr(branch_3))

print('====================ENCAPSULATION: READING WITH GETTERS====================')

print(f'Client 2 number: {client_2.get_client_no()}')
print(f'Client 2 name: {client_2.get_first_name()} {client_2.get_last_name()}')
print(f'Client 2 email: {client_2.get_email()}')
print(f'Client 2 address: {client_2.get_address()}')
print(f'Account 1 balance: {account.get_current_balance()}')
print(f'Transaction 3 status: {transaction_3.get_status()}')
print(f'Branch 3 phone number: {branch_3.get_phone_number()}')

print('====================VALIDATION: INVALID CHANGES REJECTED====================')

client_1.set_email(12345)
print(f'Client 1 email unchanged: {client_1.get_email()}')

account.set_account_type(999)
print(f'Account 1 type unchanged: {account.get_account_type()}')

account.add_funds(-50)
account.add_funds('fifty')
print(f'Account 1 balance unchanged: {account.get_current_balance()}')

account_2.withdraw(True)
account_2.withdraw(99999)
print(f'Account 2 balance unchanged: {account_2.get_current_balance()}')

transaction_3.set_description(123)
print(
    f'Transaction 3 description unchanged: {transaction_3.get_description()}')

branch_3.set_phone_number(12345)
print(f'Branch 3 phone number unchanged: {branch_3.get_phone_number()}')

transaction_3.process_transaction('not an account')
print(f'Transaction 3 status unchanged: {transaction_3.get_status()}')

print('Invalid constructor data falls back to safe defaults:')
bad_account = Account('abc', 123, -5, True)
bad_account.display_information()

print('====================VALIDATION: VALID CHANGES ACCEPTED====================')

account_2.set_account_type('Everyday')
print(f'Account 2 new type: {account_2.get_account_type()}')

transaction_3.set_description('Birthday gift from family')
print(f'Transaction 3 new description: {transaction_3.get_description()}')

print('====================AGGREGATION: CLIENTS AND ACCOUNTS====================')

client_1.add_account(account)
client_1.add_account(account_2)
client_2.add_account(account_3)

client_1.add_account(account)
client_1.add_account('not an account')

print(f'Client 1 accounts: '
      f'{[acc.get_account_no() for acc in client_1.get_accounts()]}')
print(f'Client 2 accounts: '
      f'{[acc.get_account_no() for acc in client_2.get_accounts()]}')

account_4 = Account(855201, 'Savings', 1000, '1/6/2026')
client_3.add_account(account_4)
client_3.remove_account(account_4)
print('Account 4 still exists after removal from client 3:')
account_4.display_information()

print('====================ASSOCIATION: PREFERRED BRANCHES====================')

client_1.set_preferred_branch(branch)
client_2.set_preferred_branch(branch_3)
client_3.set_preferred_branch('Glenelg')

client_1.set_preferred_branch(branch_2)

print(f'Client 1 preferred branch: '
      f'{client_1.get_preferred_branch().get_branch_name()}')
print(f'Client 2 preferred branch: '
      f'{client_2.get_preferred_branch().get_branch_name()}')
print(f'Client 3 preferred branch: {client_3.get_preferred_branch()}')

print('Branches remain independent objects:')
branch.display_information()
branch_2.display_information()
branch_3.display_information()
