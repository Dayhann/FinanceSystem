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
