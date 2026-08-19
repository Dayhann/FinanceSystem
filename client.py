class Client:
    def __init__(self, client_no, first_name, last_name, email, address):
        self.__client_no = client_no
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__address = address

    def update_contact_info(self, email, address):
        self.__email = email
        self.__address = address
        print('Client contact information updated\n')

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
    def get__address(self):
        return self.__address
    
    print()

    def set_email(self,new_email):
        self.__email = new_email
    def set_address(self,new_address):
        self.__address = new_address
    
    print()

    def __str__(self):
        return (f"{self.__first_name} {self.__last_name} has the client number: "
                f"{self.__client_no}, preferred contact: {self.__email}, "
                f"has the address: {self.__address}")

    def __repr__(self):
        return (f"Client(client_no={self.__client_no}, "
                f"first_name='{self.__first_name}', "
                f"last_name='{self.__last_name}', email='{self.__email}', "
                f"address='{self.__address}')")
