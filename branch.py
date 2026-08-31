class Branch:
    """Represents a physical branch of the finance organisation.

    Main responsibility: managing branch information and opening
    state. The opening state can only change through open_branch()
    and close_branch().
    """

    def __init__(self, branch_number, branch_name, location, phone_number,
                 is_open=False):
        if (isinstance(branch_number, int) and
                not isinstance(branch_number, bool) and branch_number > 0):
            self.__branch_number = branch_number
        else:
            self.__branch_number = 0

        if isinstance(branch_name, str):
            self.__branch_name = branch_name
        else:
            self.__branch_name = ""

        if isinstance(location, str):
            self.__location = location
        else:
            self.__location = ""

        if isinstance(phone_number, str):
            self.__phone_number = phone_number
        else:
            self.__phone_number = ""

        if isinstance(is_open, bool):
            self.__is_open = is_open
        else:
            self.__is_open = False

    def open_branch(self):
        if self.__is_open:
            print(f'{self.__branch_name} branch is already open\n')
        else:
            self.__is_open = True
            print(f'{self.__branch_name} branch opened\n')

    def close_branch(self):
        if self.__is_open:
            self.__is_open = False
            print(f'{self.__branch_name} branch closed\n')
        else:
            print(f'{self.__branch_name} branch is already closed\n')

    def opening_state(self):
        if self.__is_open:
            return "Open"
        else:
            return "Closed"

    def get_branch_number(self):
        return self.__branch_number

    def get_branch_name(self):
        return self.__branch_name

    def get_location(self):
        return self.__location

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, new_phone_number):
        if isinstance(new_phone_number, str):
            self.__phone_number = new_phone_number
        else:
            print('Invalid phone number: change rejected.')

    def update_phone_number(self, phone_number):
        self.set_phone_number(phone_number)
        print(f'{self.__branch_name} branch phone number updated\n')

    def display_information(self):
        print(f'Branch Number: {self.__branch_number}')
        print(f'Branch Name: {self.__branch_name}')
        print(f'Location: {self.__location}')
        print(f'Phone Number: {self.__phone_number}')
        print(f'Open: {self.opening_state()}\n')

    def __str__(self):
        return (f"{self.__branch_name} has the branch number "
                f"{self.__branch_number} in {self.__location} to contact, "
                f"use: {self.__phone_number} and its {self.opening_state()}")

    def __repr__(self):
        return (f"Branch(branch_number={self.__branch_number}, "
                f"branch_name='{self.__branch_name}', "
                f"location='{self.__location}', "
                f"phone_number='{self.__phone_number}', "
                f"is_open={self.__is_open})")
