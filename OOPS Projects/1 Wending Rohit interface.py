from abc import *
class Myinterface(ABC):
 # abstract An abstract method is a method that is declared without an implementation (without braces, and followed by a semicolon),
 #   def displayItems(self):pass

   def AskToEnter(self):pass
   def Payment(self): pass
   def quit(self): pass

class VendMachine1(Myinterface):
    def __init__(self):
        self.items = [
            {'code': 0, 'name': 'coca cola', 'price': 5},
            {'code': 1, 'name': 'cadbury', 'price': 10},
            {'code': 2, 'name': 'chips', 'price': 2},
        ] # in on big list, Multiple Dictionaries
        self.item=''
        # self.itemBox = '' # Default vale for itemBox if given wrong code

    def displayItems(self): # #  the code will run til the itemBox is false
        print("Welcome to the vending machine")
        for i in self.items:
            print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")
        obj.AskToEnter()

    def AskToEnter(self): # #  the code will run til the itemBox is false
        query = int(input("Enter the code number of the itemBox you want to get: "))
        for i in self.items:
            if query == i['code']:
                self.item = i
        if self.item == '':
            print('INVALID CODE')  # wrong code entered not in our itemBox list
            obj.AskToEnter()
        else:
            print(f"Great, {self.item['name']} will cost you {self.item['price']} dollars")
            obj.Payment()

    def Payment(self):
        price = int(input(f"Enter {self.item['price']} dollars to purchase: "))
        if price == self.item['price']:
            print(f"Thank you for buying here is your {self.item['name']}")
            obj.quit()
        else:
            print(f"Please enter only {self.item['price']} dollars")

    def quit(self):
        query = input("To quit the machine enter q and to continue buying enter anything: ")
        if query == 'q':
            exit
        else:
            obj.AskToEnter()
############
class VendMachine2(Myinterface):
    def __init__(self):
        self.items = [
            {'code': 0, 'name': 'coca cola', 'price': 5},
            {'code': 1, 'name': 'cadbury', 'price': 10},
            {'code': 2, 'name': 'chips', 'price': 2},
        ] # in on big list, Multiple Dictionaries
        self.item=''
        # self.itemBox = '' # Default vale for itemBox if given wrong code

    print("22222222222")
    def displayItems(self): # #  the code will run til the itemBox is false
        print("Welcome to the vending machine2")
        for i in self.items:
            print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")
        obj2.AskToEnter()

    def AskToEnter(self): # #  the code will run til the itemBox is false
        query = int(input("Enter the code number of the itemBox you want to get2: "))
        for i in self.items:
            if query == i['code']:
                self.item = i
        if self.item == '':
            print('INVALID CODE')  # wrong code entered not in our itemBox list
            obj2.AskToEnter()
        else:
            print(f"Great, {self.item['name']} will cost you {self.item['price']} dollars")
            obj2.Payment()

    def Payment(self):
        price = int(input(f"Enter {self.item['price']} dollars to purchase2: "))
        if price == self.item['price']:
            print(f"Thank you for buying here is your {self.item['name']}")
            obj2.quit()
        else:
            print(f"Please enter only {self.item['price']} dollars")

    def quit(self):
        query = input("To quit the machine enter q and to continue buying enter anything2: ")
        if query == 'q':
            exit
        else:
            obj2.AskToEnter()

obj2 = VendMachine2()
obj2.displayItems()
