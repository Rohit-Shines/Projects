import random
import sys

class ATM():

    def __init__(self, name, account_number, password ,balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.password = password
        self.items = [
            {'name': 'rohit', 'account':1234, 'password': 1993},
            {'name': 'ankith', 'account':1234, 'password': 1989},
            {'name': 'sahithi', 'account':1234, 'password': 1998},
        ]


    def display(self):
        while True:
            query = input("Do you want to do any transaction?(y/n):")
            if query == "y": obj.transaction()
            elif query == "n":
                print("""
            --------------------------------------------
           | Thanks for choosing PANDU GUNDU Bankuuuu   |
           |    Visit us again!    LOVE YOU             |
            ---------------------------------------------
                """)
                break #  to break executing the code here
            else:
                print("Wrong command!  Enter 'y' for yes and 'n' for NO.\n")

    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}") # Converts to upper case
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: Nu.{self.balance}\n")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Nu.", self.balance)
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Nu.{self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Nu.{amount} withdrawal successful!")
            print("Current account balance: Nu.", self.balance)
            print()

    def check_balance(self):
        print("Available balance: Nu.", self.balance)
        print()

    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu: ( Not food Menu)
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************
        """)

        while True:
            try:
                query = int(input("Enter 1, 2, 3, 4 or 5:"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if query == 1:
                    obj.account_detail()
                elif query == 2:
                    obj.check_balance()
                elif query == 3:
                    amount = int(input("How much you want to deposit(Nu.):"))
                    obj.deposit(amount)
                elif query == 4:
                    amount = int(input("How much you want to withdraw(Nu.):"))
                    obj.withdraw(amount)
                elif query == 5:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: Nu.{self.balance}                    
              Thanks for choosing us as your bank  
              Transaction number: {random.randint(10000, 1000000)}  # generating random number                
          ******************************************
          """)
                    sys.exit()

print("*******WELCOME TO GUNDU PANDU Bank *******\n", "----------Create Your Account----------")
name = input("Enter your name   : ")
account_number = input("Enter your account number: ")
password = input("Enter 4 digits password")
print("Congratulations! Account created successfully......\n")

obj = ATM(name,account_number,password)
obj.display()



