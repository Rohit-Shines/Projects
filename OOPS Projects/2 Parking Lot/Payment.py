

class Payment():
    def v_bus(self):
        Hours = int(input("Enter Number of hours to park the BUS :"))
        Amount = Hours * 3
        print("Amount to pay to proceed for BUS parking", Amount)

    def v_car(self):
        Hours = int(input("Enter Number of hours to park the CAR :"))
        Amount = Hours * 2
        print("Amount to pay to proceed for CAR parking", Amount)

    def v_bike(self):
        Hours = int(input("Enter Number of hours to park the BIKE :"))
        Amount = Hours * 1
        print("Amount to pay to proceed for BIKE parking", Amount)