# The parking lot can have multiple level1.
# Each level1 can have 'compact', 'large', 'bike' and 'electric' spots.
# Vehicle should be charged according to Spot type, time of parking and duration of parking.
# Should be able to add more spots to level1.
# Show the available number of spots on each level1.


import Payment
obj2=Payment.Payment()

class ParkingLot():

    def __init__(self):
        # self.VehichleType=VehichleType

        self.level1 = [{'bus': 0, 'car':0,   'bike':0}]
        self.level2 = [{'bus': 10, 'car': 5, 'bike': 0}]
        self.level3 = [{'bus': 10, 'car': 5, 'bike': 0}]

    def display_spots(self):
        print("####Welcome to Parking lot#####")
        for i in self.level1:
            print(f"slots Available in level 1 : Bus ={i['bus']} Car={i['car']}, Bike={i['bike']}")
        for i in self.level2:
            print(f"slots Available in level 2 : Bus ={i['bus']} Car={i['car']}, Bike={i['bike']}")
        for i in self.level3:
            print(f"slots Available in level 3 : Bus ={i['bus']} Car={i['car']}, Bike={i['bike']}")
            self.enter_Details_level1()


    def enter_Details_level1(self):
        VehichleType = str(input("#######Enter the vehicle type you wanted to park in level1 = #bus# or #car# or #bike#  #######"))
        if VehichleType=="bus":
            for i in self.level1:
                if i['bus'] >0:
                    i['bus']-=1
                    obj2.v_bus()
                else:
                    print("Not spots available for bus at this level1 Proceed to level 2")
                    self.enter_Details_level2()
        elif VehichleType=="car":
            for i in self.level1:
                if i['car'] >0:
                    i['car']-=1
                    obj2.v_car()
                else:
                    print("Not spots available for car at this level1 Proceed to level 2")
                    self.enter_Details_level2()
        elif VehichleType=="bike":
            for i in self.level1:
                if i['bike'] >0:
                    i['bike']-=1
                    obj2.bike()
                else:
                    print("Not spots available for bike at this level1 Proceed to level 2")
                    self.enter_Details_level2()
        else:
            query = input("Your Vehicle is not allowed to park here, Press Q to exit or any key word to enter vehicle type again")
            if query == 'Q':
                exit
            else:
                self.enter_Details_level1()

    def enter_Details_level2(self):
        VehichleType = str(input("#######Enter the vehicle type you wanted to park in level2 = #bus# or #car# or #bike#  #######"))
        if VehichleType=="bus":
            for i in self.level2:
                if i['bus'] >0:
                    i['bus']-=1
                    obj2.v_bus()
                else:
                    print("Not spots available for bus at this level2 Proceed to level 3")
                    self.enter_Details_level3()
        elif VehichleType=="car":
            for i in self.level2:
                if i['car'] >0:
                    i['car']-=1
                    obj2.v_car()
                else:
                    print("Not spots available for car at this level2 Proceed to level 3")
                    self.enter_Details_level3()
        elif VehichleType=="bike":
            for i in self.level2:
                if i['bike'] >0:
                    i['bike']-=1
                    obj2.v_bike()
                else:
                    print("Not spots available for bike at this level2 Proceed to level 3")
                    self.enter_Details_level3()
        else:
            query = input("Your Vehicle is not allowed to park here, Press Q to exit or any key word to enter vehicle type again")
            if query == 'Q':
                exit
            else:
                self.enter_Details_level2()

    def enter_Details_level3(self):
        VehichleType = str(input("#######Enter the vehicle type you wanted to park in level3 = #bus# or #car# or #bike#  #######"))
        if VehichleType=="bus":
            for i in self.level3:
                if i['bus'] >0:
                    i['bus']-=1
                    obj2.v_bus()
                else:
                    print("No spots available for bus at this level3 please leave the building")
        elif VehichleType=="car":
            for i in self.level3:
                if i['car'] >0:
                    i['car']-=1
                    obj2.v_car()
                else:
                    print("No spots available for Car at this level3 please leave the building")
        elif VehichleType=="bike":
            for i in self.level3:
                if i['bike'] >0:
                    i['bike']-=1
                    obj2.v_bike()
                else:
                    print("No spots available for Bike at this level3 please leave the building")
        else:
            query = input("Your Vehicle is not allowed to park here, Press Q to exit or any key word to enter vehicle type again")
            if query == 'Q':
                exit
            else:
                obj1.enter_Details_level3()


