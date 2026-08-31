from account import Account
from branch import Branch


class Client:
    """Represents a client of the finance organisation.

    Main responsibility: managing the client's own information
    (contact details) and the client's relationships - the accounts
    the client holds (aggregation) and their preferred branch
    (association).
    """

    def __init__(self, client_no, first_name, last_name, email, address):
        if isinstance(client_no, int) and not isinstance(client_no, bool) and client_no > 0:
            self.__client_no = client_no
        else:
            self.__client_no = 0

        if isinstance(first_name, str):
            self.__first_name = first_name
        else:
            self.__first_name = ""

        if isinstance(last_name, str):
            self.__last_name = last_name
        else:
            self.__last_name = ""

        if isinstance(email, str):
            self.__email = email
        else:
            self.__email = ""

        if isinstance(address, str):
            self.__address = address
        else:
            self.__address = ""

        self.__accounts = []
        self.__preferred_branch = None

    def show_contact_info(self):
        print(f'Client Number:{self.__client_no}')
        print(f'First Name:{self.__first_name}')
        print(f'Last Name:{self.__last_name}')
        print(f'Email:{self.__email}')
        print(f'Address:{self.__address},\n')

    def get_client_no(self):
        return self.__client_no

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

    def set_email(self, new_email):
        if isinstance(new_email, str):
            self.__email = new_email
        else:
            print('Invalid email: change rejected.')

    def set_address(self, new_address):
        if isinstance(new_address, str):
            self.__address = new_address
        else:
            print('Invalid address: change rejected.')

    def add_account(self, account):
        if not isinstance(account, Account):
            print('Invalid account: only Account objects can be added.')
            return
        if account in self.__accounts:
            print('Account already assigned to this client.')
            return
        self.__accounts.append(account)
        print(f'Account {account.get_account_no()} added to client '
              f'{self.__client_no}')

    def remove_account(self, account):
        if account not in self.__accounts:
            print('Account is not assigned to this client.')
            return
        self.__accounts.remove(account)
        print(f'Account {account.get_account_no()} removed from client '
              f'{self.__client_no}')

    def get_accounts(self):
        return list(self.__accounts)

    def set_preferred_branch(self, branch):
        if branch is None or isinstance(branch, Branch):
            self.__preferred_branch = branch
            if branch is None:
                print('Preferred branch cleared.')
            else:
                print(f'Preferred branch set to {branch.get_branch_name()}.')
        else:
            print('Invalid branch: change rejected.')

    def get_preferred_branch(self):
        return self.__preferred_branch

    def __str__(self):
        return (f"{self.__first_name} {self.__last_name} has the client number: "
                f"{self.__client_no}, preferred contact: {self.__email}, "
                f"has the address: {self.__address}")

    def __repr__(self):
        return (f"Client(client_no={self.__client_no}, "
                f"first_name='{self.__first_name}', "
                f"last_name='{self.__last_name}', email='{self.__email}', "
                f"address='{self.__address}')")
