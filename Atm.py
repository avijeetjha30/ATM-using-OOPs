class Atm:

    __counter = 1
    def __init__(self):
        self.__pin = ""
        self.__balance = 0.0

        self.menu() 

        Atm.__counter = Atm.__counter + 1

    """
    # use getter and setter method to change your private data (pin) inside class you can't change private class outside class
    # You can change Private data(atteribute value) outside of the class using <objName>._<className>__<attributeName> = <value>
    def get_pin(self):
        '''Getter method'''
        print(self.__pin)
    
    def set_pin(self,new_pin):
        self.__pin = new_pin
        print("Your new oin is {}".format(new_pin))
    """

    @staticmethod
    def get_counter():
        print(Atm.__counter)
    
    @staticmethod
    def set_counter(new):
        if(type(new) == int):
            Atm.__counter = new
        else:
            print("Enter only integer Value")
    

    def menu(self):

        '''Instruction of menu that what are you doing to find docstring used <objectName>.<methodName_(menu).__doc__>'''
        
        print("##################################################")
        print("""Hello, What would you like to do
        1. press 1 to create pin
        2. press 2 to deposite ammount
        3. press 3 to check balance
        4. press 4 to withdraw balance
        5. press 5 to change your pin
        6. press any other key to quit
        """)

        user_input = input()
        if user_input == "1":
            if self.__pin == "":
                self.create_pin()
            else:
                print("You already create your pin press 5 to change your pin")
                self.menu()

        
        elif user_input == "2":
            # if user does not create pin first
            if self.__pin == "":
                print("First you have to create your pin")
                self.menu()
            else:
                self.deposit_ammount()
        
        elif user_input == "3":
            # if user does not create pin first
            if self.__pin == "":                
                print("First you have to create your pin")
                self.menu()
            else:
                self.check_balance()
        
        elif user_input == "4":
            # if user does not create pin first
            if self.__pin == "":
                print("First you have to create your pin")
                self.menu()
            else:
                self.withdraw_ammount()
        
        elif user_input == "5":
            # if user does not create pin first
            if self.__pin == "":
                print("First you have to create your pin")
                self.menu()
            else:
                self.change_pin()

        else:
            self.quit_atm()


    def create_pin(self):

        '''First you have to create your pin to find docstring used <objectName>.<methodName_(menu).__doc__>'''

        print("Enter 4 digit pin to create")
        user_pin = input()
        
        if len(user_pin) > 3:
            # we use try and except because if user input is in charachter the code is not throw any error on console
            try:
                if type(int(user_pin)) == int:
                    self.__pin = user_pin
                    print(f"Your pin is : {user_pin}")
            
            except ValueError:
                print("Pin is in digit not in charachter")
                self.create_pin()
        else:
            print("You have to enter at least 4 digit of pin")
            self.create_pin() 
        self.menu()


    def change_pin(self):

        '''Change your pin'''

        try:
            print("Enter your pin")
            old_pin = input()
            if old_pin == self.__pin:
                print("Enter your  new pin")
                new_pin = input()
                if len(new_pin) > 3 and type(int(new_pin)) == int:
                    self.__pin = new_pin
                    print("your new_pin is", self.__pin)
                else:
                    print("Your length of new pin is either not greater than 4 or are of integer type")
            else:
                print("Enter Valid pin")
                self.change_pin()
        except ValueError:
            print("Enter Valid pin")
            self.change_pin()
        self.menu()


    def deposit_ammount(self):

        '''Deposit some ammount to find docstring used <objectName>.<methodName_(menu).__doc__>'''

        print("Enter your Pin")
        user_pin = input()
        
        if user_pin == self.__pin:
            # we use try and except because if user input is in charachter the code is not throw any error on console
            try:
                print("Enter ammount you want to deposit")
                deposit_balance = float(input())
                self.__balance = self.__balance + deposit_balance
                print(f"Avilable balance is {round(self.__balance)}")
            except ValueError:
                print("You Enter wrong value")
                self.deposit_ammount()
        else:
            print("Invalid pin")
            self.deposit_ammount()
        self.menu()
    

    def check_balance(self):

        '''Check you avilable balanece in your account to find docstring used <objectName>.<methodName_(menu).__doc__>'''

        print("Enter your valid pin")
        user_pin = input()
        
        if user_pin == self.__pin:
            print(f"Avilable Balance is {round(self.__balance)}")
        else:
            print("Invalid pin")
            self.check_balance()
        self.menu()
    

    def withdraw_ammount(self):

        '''Withdraw ammount from your account to find docstring used <objectName>.<methodName_(menu).__doc__>'''

        print("Enter Your 4 digit pin")
        user_pin = input()
        
        if user_pin == self.__pin:
            # we use try and except because if user input is in charachter the code is not throw any error on console
            try:
                print("Enter ammount you want to withdraw")
                withdraw_balance = float(input())
                if withdraw_balance <= self.__balance:
                    self.__balance = self.__balance - withdraw_balance
                    
                    if self.__balance <= 1000.00:
                        print(f"Avilable balance is {round(self.__balance)} which is below 1000 so you will be charged some extra")
                        self.menu()
                    else:
                        print(f"Avilable Balance is {round(self.__balance)}")
                        self.menu()
                else:
                    print(f"Avilable Balance is {round(self.__balance)} but you enterd {withdraw_balance}")
                    self.withdraw_ammount()
            except ValueError:
                print("You Enter wrong amount")
                self.check_balance()
        else:
            print("Invalid pin")
            self.withdraw_ammount()
        
        self.menu()
    
    def quit_atm(self):
        print("Bye, thank you")