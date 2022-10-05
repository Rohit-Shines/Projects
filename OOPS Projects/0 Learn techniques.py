Display, Asktoenter, Check Availablity, Quit // -> are mojor methods to define something


from abc import *
class Myinterface(ABC):
 # abstract An abstract method is a method that is declared without an implementation (without braces, and followed by a semicolon),
 #   def displayItems(self):pass

   def AskToEnter(self):pass
   def availability(self): pass
   def quit(self): pass

class LearnTechniques(Myinterface):

    # Constructor Method
    def __init__(self):
        self.items = [ {'code': 0, 'name': 'coke', 'price': 5,'stock': 5}, {'code': 1, 'name': 'cadbury', 'price': 10,'stock': 5}, {'code': 2, 'name': 'chips', 'price': 2,'stock': 5},] # in on big list, Multiple Dictionaries keyes
        self.itemBox= '' # self.itemBox = '' # Default vale for itemBox if given wrong code

    # Display Anything using F key
    def display(self): # #  the code will run til the itemBox is false
        for i in self.items:
            print(f" Code name:{i['code']}    {i['name']}    cost:  {i['price']} stock {i['stock']}")
        obj.AskToEnter()

    # Query to take entry and choose which method to execut
    def AskToEnter(self): # #  the code will run til the itemBox is false
        query = input("Enter the code number of the itemBox you want to get: ")
        for i in self.items:
            if query== i['code']:
                self.itemBox=i
                print("self.itemBox",self.itemBox)
                print(self.itemBox['stock'])

        if self.itemBox['code'] =='':
            print('INVALID CODE')  # wrong code entered not in our itemBox list
            obj.AskToEnter()

        elif self.itemBox['code']==0:
            for i in self.items:
                if i['stock'] >0:
                    i['stock']-=1
                    obj2.v_bus()
                    print( self.items)

     ## check if any item is available or not
    def check_availability(self):

        for i in self.items:
            if i['stock'] > 0:
                i['stock'] -= 1
                obj2.v_bus()
                print(self.items)








    def quit(self):
        query = input("To quit the machine enter q and to continue buying enter anything: ")
        if query == 'q':
            exit
        else:
            obj.AskToEnter()

obj=LearnTechniques()
obj.display()