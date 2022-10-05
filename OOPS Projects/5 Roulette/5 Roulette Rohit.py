# import random
import sys
sys.setrecursionlimit(2000) # this will help to ignore error of recursion 1245

class roulette():

    def __init__(self):
        self.cash = 1000
        self.cntr = 0

        self.list = [23, 22, 13, 24, 26, 5, 17, 8, 17, 6, 0, 32, 7, 20, 24, 32, 9, 20, 30, 10, 32, 7, 34, 11, 13, 1, 36, 18, 11, 29, 25, 27, 29, 11, 20, 29, 18, 14, 16, 36, 15, 24, 26, 34, 0, 3, 4, 31, 30, 30, 28, 0, 2, 12, 27, 9, 33, 14, 33, 2, 32, 22, 24, 6, 31, 23, 28, 35, 9, 4, 19, 21, 2, 35, 33, 24, 24, 6, 6, 32, 25, 23, 14, 26, 9, 31, 14, 14, 12, 27, 32, 11, 21, 1, 4, 5, 2, 6, 0, 28, 33, 27, 34, 26, 33, 35, 24, 2, 13, 2, 31, 7, 27, 2, 30, 9, 11, 17, 32, 17, 26, 4, 1, 12, 15, 32, 27, 4, 12, 20, 11, 34, 0, 7, 29, 1, 5, 14, 25, 20, 0, 36, 18, 32, 1, 8, 2, 8, 27, 20, 11, 35, 10, 7, 34, 33, 3, 11, 10, 5, 30, 19, 33, 32, 27, 14, 23, 12, 30, 25, 33, 27, 23, 32, 31, 21, 34, 8, 7, 0, 2, 22, 15, 5, 2, 15, 9, 14, 1, 31, 24, 10, 17, 2, 31, 9, 24, 36, 15, 19, 7, 0, 4, 23, 10, 25, 2, 18, 7, 36, 26, 15, 32, 6, 19, 8, 2, 22, 10, 33, 26, 30, 14, 34, 6, 11, 10, 8, 17, 5, 0, 4, 30, 7, 23, 33, 28, 29, 4, 17, 23, 10, 34, 18, 12, 16, 15, 1, 26, 32, 25, 24, 24, 4, 29, 27, 17, 24, 7, 32, 34, 3, 3, 25, 15, 14, 22, 23, 12, 28, 9, 5, 31, 32, 0, 5, 25, 18, 24, 23, 24, 3, 24, 2, 8, 29, 22, 9, 0, 25, 21, 22, 15, 27, 5, 26, 0, 30, 35, 29, 17, 4, 26, 8, 11, 15, 33, 28, 23, 12, 9, 15, 24, 23, 21, 8, 31, 13, 2, 31, 16, 5, 24, 2, 22, 7, 19, 13, 17, 29, 5, 13, 18, 33, 30, 12, 6, 13, 15, 26, 20, 0, 4, 28, 20, 31, 4, 16, 21, 6, 18, 25, 8, 19, 25, 0, 14, 34, 10, 19, 28, 2, 17, 36, 11, 30, 7, 15, 0, 35, 12, 9, 20, 17, 33, 21, 27, 23, 22, 34, 20, 26, 35, 15, 29, 30, 32, 32, 16, 20, 0, 30, 12, 31, 7, 10, 34, 32, 28, 7, 25, 10, 31, 28, 0, 35, 24, 14, 14, 14, 33, 19, 6, 26, 18, 18, 11, 24, 20, 30, 17, 25, 27, 30, 34, 4, 28, 13, 20, 14, 34, 7, 26, 5, 6, 19, 1, 33, 22, 24, 3, 4, 25, 17, 8, 8, 29, 3, 11, 24, 26, 33, 0, 17, 13, 17, 35, 18, 7, 17, 20, 27, 6, 35, 12, 13, 15, 18, 29, 10, 14, 17, 24, 33, 36, 15, 3, 0, 26, 1, 28, 18, 19, 15, 6, 22, 21, 1, 33, 22, 13, 8, 6, 22, 7, 31, 1, 23, 7, 28, 3, 17, 32, 6, 22, 36, 31, 13, 35, 35, 33, 27, 11, 2, 3, 10, 1, 21, 27, 33, 24, 17, 24, 24, 33, 21, 15, 23, 2, 18, 8, 7, 30, 4, 5, 2, 9, 10, 35, 17, 20, 25, 34, 30, 9, 35, 23, 12, 23, 3, 22, 31, 7, 28, 25, 26, 25, 5, 35, 35, 1, 23, 35, 32, 3, 35, 27, 11, 26, 10, 34, 8, 5, 13, 3, 1, 36, 24, 31, 35, 3, 29, 7, 11, 34, 29, 33, 30, 19, 5, 30, 27, 5, 20, 15, 21, 6, 8, 32, 10, 4, 3, 8, 16, 0, 2, 16, 18, 31, 13, 35, 9, 18, 30, 24, 14, 6, 7, 15, 29, 23, 12, 3, 9, 28, 22, 16, 13, 0, 27, 14, 20, 34, 19, 20, 5, 25, 33, 27, 8, 1, 21, 7, 16, 19, 19, 26, 7, 12, 26, 9, 7, 19, 26, 8, 7, 4, 35, 30, 5, 11, 28, 26, 31, 25, 21, 15, 3, 6, 27, 5, 27, 20, 26, 7, 14, 30, 6, 15, 29, 0, 8, 2, 31, 4, 35, 21, 28, 30, 7, 18, 6, 19, 20, 27, 33, 11, 25, 25, 21, 36, 0, 22, 4, 15, 14, 8, 16, 13, 31, 36, 31, 13, 31, 25, 3, 27, 34, 18, 15, 33, 16, 8, 0, 18, 6, 23, 5, 22, 36, 31, 10, 9, 10, 26, 1, 11, 1, 35, 15, 19, 25, 16, 13, 17, 0, 16, 11, 12, 29, 32, 11, 21, 35, 4, 18, 17, 16, 34, 17, 36, 34, 3, 6, 20, 2, 19, 1, 2, 14, 26, 32, 17, 29, 12, 35, 30, 3, 17, 31, 21, 2, 32, 30, 17, 28, 9, 2, 31, 8, 2, 21, 4, 27, 32, 36, 9, 7, 2, 14, 7, 11, 6, 27, 34, 0, 8, 33, 14, 6, 20, 24, 24, 32, 27, 23, 17, 1, 22, 31, 20, 27, 18, 29, 30, 16, 0, 12, 5, 24, 24, 22, 19, 34, 27, 26, 11, 7, 34, 24, 23, 24, 28, 29, 21, 11, 6, 14, 35, 6, 36, 30, 27, 15, 0, 11, 28, 15, 29, 21, 3, 2, 15, 15, 31, 14, 35, 16, 8, 2, 3, 11, 4, 19, 16, 19, 28, 8, 28, 27, 35, 5, 15, 17, 14, 23, 21, 14, 28, 8, 8, 8, 7, 30, 1, 20, 16, 27, 7, 17, 5, 34, 35, 30, 16, 9, 18, 32, 2, 3, 19, 0, 3, 32, 27, 13, 6, 15, 31, 12, 11, 25, 20, 27, 29, 19, 2, 4, 6, 5, 22, 12, 34, 22, 36, 32, 36, 6, 33, 18, 16, 35, 29, 30, 7, 23, 29, 15, 6, 34, 8, 19, 20, 16, 1, 8, 9, 18, 33, 19, 7, 32, 0, 36, 13, 14, 31, 17, 28, 16, 28, 18, 12, 33, 33, 21, 33, 34, 21, 28, 19, 28, 26, 9, 16, 16, 35, 15, 21, 17, 36, 24, 27, 12, 33, 3, 7, 34, 10, 4, 34, 19, 13, 21, 8, 7, 17, 24, 28, 11, 21, 1, 0, 25, 20, 2, 14, 8, 8, 14, 22, 30, 8, 27, 16, 3, 7, 4, 19, 30, 9, 8, 17, 8, 1, 11, 2, 12, 10, 1, 12, 35, 29, 9, 11, 20, 11, 19, 6, 33, 19, 27, 24, 30, 20, 2, 6, 34, 34, 4, 18, 17, 11, 30, 7, 31, 35, 7, 3, 24, 26, 35, 16, 20, 19, 29, 4, 23, 25, 3, 11, 6, 25, 33, 26, 30, 3, 30, 19, 12, 19, 31, 10, 1, 4, 27, 13, 4, 8, 18, 27, 30, 33, 9, 8, 8, 17, 16, 0, 35, 21, 32, 35, 3, 18, 2, 31, 22, 19, 18, 23, 15, 1, 25, 23, 2, 18, 0, 21, 29, 1, 22, 2, 24, 5, 31, 32, 28, 31, 32, 8, 1, 35, 35, 30, 9, 13, 2, 0, 15, 5, 21, 0, 32, 0, 30, 33, 9, 10, 25, 4, 24, 21, 2, 7, 17, 13, 29, 0, 10, 36, 33, 1, 21, 15, 35, 8, 12, 25, 35, 18, 19, 20, 24, 36, 25, 0, 13, 22, 31, 13, 9, 26, 31, 2, 33, 18, 24, 17, 2, 17, 30, 31, 16, 7, 14, 28, 4, 15, 29, 0, 25, 13, 23, 21, 14, 5, 24, 29, 16, 16, 14, 2, 23, 19, 30, 19, 36, 15, 11, 20, 9, 2, 14, 15, 19, 25, 18, 28, 18, 19, 33, 30, 1, 16, 25, 28, 9, 13, 22, 17, 12, 14, 31, 24, 21, 0, 8, 20, 4, 25, 0, 20, 25, 11, 14, 12, 2, 11, 5, 12, 35, 23, 8, 16, 32, 9, 19, 16, 14, 5, 18, 11, 25, 11, 32, 32, 17, 26, 24, 27, 20, 2, 11, 30, 30, 10, 26, 8, 8, 6, 3, 3, 18, 34, 2, 11, 0, 2, 10, 1, 13, 1, 0, 30, 16, 25, 14, 25, 32, 31, 14, 26, 6, 15, 25, 30, 10, 10, 17, 32, 35, 20, 18, 4, 35, 17, 33, 33, 9, 36, 5, 1, 32, 3, 5, 19, 26, 34, 5, 14, 3, 8, 17, 15, 4, 30, 8, 30, 6, 1, 16, 26, 36, 8, 24, 29, 29, 7, 21, 1, 32, 20, 13, 33, 24, 35, 10, 33, 16, 14, 28, 28, 21, 20, 11, 24, 4, 12, 2, 7, 34, 29, 35, 1, 1, 4, 1, 35, 17, 16, 25, 1, 6, 15, 26, 7, 30, 24, 0, 29, 25, 8, 18, 27, 19, 23, 0, 12, 25, 8, 15, 29, 16, 31, 8, 2, 32, 11, 13, 17, 6, 15, 30, 36, 23, 11, 31, 22, 0, 17, 25, 18, 10, 17, 26, 26, 14, 1, 20, 28, 7, 14, 16, 1, 23, 32, 36, 22, 5, 19, 20, 10, 3, 18, 31, 35, 19, 22, 11, 6, 4, 22, 34, 19, 22, 31, 11, 17, 1, 16, 31, 32, 10, 18, 34, 22, 34, 22, 33, 31, 4, 33, 3, 12, 5, 3, 28, 22, 17, 25, 29, 0, 33, 19, 10, 35, 24, 19, 17, 34, 8, 13, 35, 27, 18, 30, 5, 11, 10, 19, 2, 30, 3, 33, 13, 24, 30, 2, 34, 24, 22, 27, 8, 36, 10, 31, 27, 33, 23, 3, 5, 3, 24, 16, 17, 28, 30, 27, 16, 5, 29, 28, 18, 1, 10, 1, 11, 15, 32, 13, 12, 12, 2, 1, 15, 24, 16, 22, 14, 25, 19, 8, 8, 31, 26, 21, 31, 3, 15, 13, 33, 6, 4, 28, 16, 36, 6, 7, 29, 35, 28, 15, 5, 18, 9, 27, 19, 33, 25, 4, 18, 31, 31, 21, 19, 14, 6, 4, 9, 19, 35, 3, 15, 29, 26, 5, 8, 0, 14, 15, 21, 7, 32, 24, 16, 11, 36, 20, 33, 35, 16, 8, 0, 27, 14, 29, 24, 19, 23, 22, 33, 29, 3, 6, 10, 36, 11, 5, 19, 27, 33, 28, 28, 22, 12, 3, 20, 15, 14, 19, 2, 3, 24, 34, 9, 26, 1, 9, 28, 7, 5, 1, 18, 2, 0, 35, 15, 17, 0, 9, 10, 33, 19, 12, 10, 33, 23, 29, 4, 10, 3, 1, 28, 10, 1, 29, 33, 28, 11, 20, 18, 29, 32, 22, 34, 22, 33, 18, 0, 20, 25, 2, 5, 25, 28, 16, 6, 27, 20, 26, 25, 1, 25, 35, 0, 32, 6, 21, 5, 5, 15, 17, 4, 22, 16, 36, 21, 5, 36, 34, 32, 19, 13, 22, 17, 16, 17, 1, 26, 10, 20, 22, 26, 32, 30, 17, 10, 13, 29, 24, 24, 17, 33, 20, 14, 26, 23, 7, 25, 20, 35, 24, 26, 12, 25, 8, 30, 30, 25, 31, 7, 4, 3, 21, 26, 22, 33, 9, 20, 0, 21, 9, 24, 23, 4, 23, 11, 28, 35, 31, 1, 22, 30, 28, 2, 21, 13, 12, 32, 15, 27, 6, 21, 1, 32, 31, 36, 0, 22, 22, 30, 24, 10, 14, 33, 2, 6, 3, 11, 11, 3, 4, 21, 15, 31, 21, 8, 2, 15, 10, 1, 19, 25, 15, 25, 31, 16, 21, 13, 30, 29, 36, 2, 2, 27, 6, 16, 13, 30, 28, 19, 28, 21, 8, 9, 0, 30, 26, 12, 17, 9, 21, 13, 6, 15, 30, 17, 23, 20, 23, 20, 31, 1, 34, 7, 16, 25, 35, 21, 19, 23, 5, 12, 19, 12, 33, 6, 25, 9, 7, 22, 12, 32, 11, 22, 22, 4, 35, 30, 34, 19, 24, 8, 20, 32, 15, 4, 30, 18, 15, 24, 16, 11, 28, 19, 11, 3, 7, 36, 12, 10, 1, 16, 11, 2, 20, 15, 6, 7, 6, 31, 33, 32, 0, 25, 7, 10, 16, 12, 26, 11, 19, 1, 12, 31, 34, 28, 30, 3, 30, 14, 36, 5, 29, 36, 22, 24, 6, 17, 12, 32, 25, 20, 11, 15, 20, 18, 25, 12, 24, 28, 2, 5, 1, 32, 32, 3, 34, 20, 8, 15, 20, 12, 30, 10, 32, 31, 32, 15]
        self.color= {0:'NoColor',32:'black', 19:'black', 21:'black', 25:'black', 34:'black', 27:'black', 36:'black', 30:'black', 23:'black', 5:'black', 16:'black', 1:'black', 14:'black', 9:'black', 18:'black', 7:'black', 12:'black', 3:'black',15:'red', 4:'red', 2:'red', 17:'red', 6:'red', 13:'red', 11:'red', 8:'red', 10:'red', 24:'red', 33:'red', 20:'red', 31:'red', 22:'red', 29:'red', 28:'red', 35:'red', 26:'red'}
        self.cntr_odd=1
        self.c = 2

    def display(self):
        print(self.list)
        self.logicKick()

    def logicKick(self):

        a=self.c-2
        b=self.c-1
        #####################
        while self.c<1450:      ####### this value is most important
            x=self.list[a] ; y=self.list[b]; z=self.list[self.c]
            a+=1; b+=1; self.c+=1
            print(x, y, z)

            # EVEN
            if (x)%2==0 and (y)%2==0 and (z)%2==0: # even bet on odd
                print("This are even")
                self.oddgain()
            # ODD
            elif (x)%2!=0 and (y)%2!=0 and (z)%2!=0: # odd bet on even
                print("This are odd")
                self.evengain()

            # #Red
            elif self.color[x]=='red' and self.color[y]=='red' and self.color[z]=='red':
                print("RED numbers")
                self.blackGain()

            # #Black
            elif self.color[x] == 'black' and self.color[y] == 'black' and self.color[z] == 'black':
                print("Black numbers")
                self.redGain()

            # 3 Halfs 1:3 ratio Logic part1_3
            elif x < 13 and y < 13 and z < 13:
                print("Part 1 in 3 halfs")
                self.part1_3gain()

            elif x > 12 and x < 22 and y > 12 and y < 22 and z > 12 and z < 22:
                print("Part 2 in 3 halfs")
                self.part2_3gain()

            elif x > 24 and x < 37 and y > 24 and y < 37 and z > 24 and z < 37:
                print(" 3rd in 3 halfs")
                self.part3_3gain()

            # 2 halfs 1:2
            elif x<19 and y<19 and z<19: #1st half bet on 2nd half
                print("1st half")
                self.onehalfgain()

            elif x>18 and y>18 and z>18: # 2nd half bet on 1st half
                print("2nd half")
                self.scndhalfgain()

            else:
                pass



################# ODD Gain #####################

    def oddgain(self):

        if (self.list[self.c]) % 2 != 0:
            self.cash += 5; print("Gain", self.cash); self.logicKick()
        else:
            self.cash -= 5;print("loss", self.cash);self.oddloss1()

    def oddloss1(self):
        self.c+=1
        if (self.list[self.c]) % 2 != 0:
            self.cash += 10; print("Gain", self.cash);   self.logicKick()
        else:
            self.cash -= 10; print("loss", self.cash);  self.oddloss2()

    def oddloss2(self):
        self.c += 1
        if (self.list[self.c]) % 2 != 0:
            self.cash += 20;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 20;
            print("loss", self.cash);
            self.oddloss3()

    def oddloss3(self):
        self.c += 1
        if (self.list[self.c]) % 2 != 0:
            self.cash += 40;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 40;
            print("loss", self.cash);
            self.oddloss4()

    def oddloss4(self):
        self.c += 1
        if (self.list[self.c]) % 2 != 0:
            self.cash += 80;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 80;
            print("loss", self.cash);
            self.oddloss5()

    def oddloss5(self):
        self.c += 1
        if (self.list[self.c]) % 2 != 0:
            self.cash += 160;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 160;
            print("loss", self.cash);
            self.oddloss6()

    def oddloss6(self):
        self.c += 1
        if (self.list[self.c]) % 2 != 0:
            self.cash += 320;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 320;
            print("loss", self.cash);
            self.oddloss7()

    def oddloss7(self):
        self.c += 1
        if (self.list[self.c]) % 2 != 0:
            self.cash += 640;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 640;
            print("loss", self.cash);
            self.logicKick()

    ################# Even Gain #####################
    def evengain(self):
        if (self.list[self.c]) % 2 == 0:
            self.cash += 5; print("Gain", self.cash); self.logicKick()
        else:
            self.cash -= 5;print("loss", self.cash);self.evenloss1()

    def evenloss1(self):
        self.c+=1
        if (self.list[self.c]) % 2 == 0:
            self.cash += 10; print("Gain", self.cash);   self.logicKick()
        else:
            self.cash -= 10; print("loss", self.cash);  self.evenloss2()

    def evenloss2(self):
        self.c += 1
        if (self.list[self.c]) % 2 == 0:
            self.cash += 20;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 20;
            print("loss", self.cash);
            self.evenloss3()

    def evenloss3(self):
        self.c += 1
        if (self.list[self.c]) % 2 == 0:
            self.cash += 40;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 40;
            print("loss", self.cash);
            self.evenloss4()

    def evenloss4(self):
        self.c += 1
        if (self.list[self.c]) % 2 == 0:
            self.cash += 80;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 80;
            print("loss", self.cash);
            self.evenloss5()

    def evenloss5(self):
        self.c += 1
        if (self.list[self.c]) % 2 == 0:
            self.cash += 160;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 160;
            print("loss", self.cash);
            self.evenloss6()

    def evenloss6(self):
        self.c += 1
        if (self.list[self.c]) % 2 == 0:
            self.cash += 320;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 320;
            print("loss", self.cash);
            self.evenloss7()

    def evenloss7(self):
        self.c += 1
        if (self.list[self.c]) % 2 == 0:
            self.cash += 640;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 640;
            print("loss", self.cash);
            self.logicKick()

###################### Black Gain #################################
    def blackGain(self):

        if self.color[self.list[self.c]]=='black':
            self.cash += 5; print("Gain", self.cash); self.logicKick()
        else:
            self.cash -= 5;print("loss", self.cash); self.blackloss1()

    def blackloss1(self):
        self.c+=1
        if self.color[self.list[self.c]]=='black':
            self.cash += 10; print("Gain", self.cash);   self.logicKick()
        else:
            self.cash -= 10; print("loss", self.cash);  self.blackloss2()

    def blackloss2(self):
        self.c += 1
        if self.color[self.list[self.c]]=='black':
            self.cash += 20;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 20;
            print("loss", self.cash);
            self.blackloss3()

    def blackloss3(self):
        self.c += 1
        if self.color[self.list[self.c]]=='black':
            self.cash += 40;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 40;
            print("loss", self.cash);
            self.blackloss4()

    def blackloss4(self):
        self.c += 1
        if self.color[self.list[self.c]]=='black':
            self.cash += 80;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 80;
            print("loss", self.cash);
            self.evenloss5()

    def blackloss5(self):
        self.c += 1
        if self.color[self.list[self.c]]=='black':
            self.cash += 160;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 160;
            print("loss", self.cash);
            self.blackloss6()

    def blackloss6(self):
        self.c += 1
        if self.color[self.list[self.c]]=='black':
            self.cash += 320;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 320;
            print("loss", self.cash);
            self.blackloss7()

    def blackloss7(self):
        self.c += 1
        if self.color[self.list[self.c]]=='black':
            self.cash += 640;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 640;
            print("loss", self.cash);
            self.logicKick()

###################### Red Gain #################################
    def redGain(self):

        if self.color[self.list[self.c]] == 'red':
            self.cash += 5;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 5;
            print("loss", self.cash);   self.redloss1()

    def redloss1(self):
        self.c += 1
        if self.color[self.list[self.c]] == 'red':
            self.cash += 10;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 10;
            print("loss", self.cash);
            self.redloss2()

    def redloss2(self):
        self.c += 1
        if self.color[self.list[self.c]] == 'red':
            self.cash += 20;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 20;
            print("loss", self.cash);
            self.redloss3()

    def redloss3(self):
        self.c += 1
        if self.color[self.list[self.c]] == 'red':
            self.cash += 40;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 40;
            print("loss", self.cash);
            self.redloss4()

    def redloss4(self):
        self.c += 1
        if self.color[self.list[self.c]] == 'red':
            self.cash += 80;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 80;
            print("loss", self.cash);
            self.redloss5()

    def redloss5(self):
        self.c += 1
        if self.color[self.list[self.c]] == 'red':
            self.cash += 160;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 160;
            print("loss", self.cash);
            self.redloss6()

    def redloss6(self):
        self.c += 1
        if self.color[self.list[self.c]] == 'red':
            self.cash += 320;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 320;
            print("loss", self.cash);
            self.redloss7()

    def redloss7(self):
        self.c += 1
        if self.color[self.list[self.c]] == 'red':
            self.cash += 640;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 640;
            print("loss", self.cash);
            self.logicKick()

################# 1st half Gain #####################
    def onehalfgain(self):

        if (self.list[self.c]) >18 :
            self.cash += 5; print("Gain", self.cash); self.logicKick()
        else:
            self.cash -= 5;print("loss", self.cash);self.onehalfloss1()

    def onehalfloss1(self):
        self.c+=1
        if (self.list[self.c]) >18 :
            self.cash += 10; print("Gain", self.cash);   self.logicKick()
        else:
            self.cash -= 10; print("loss", self.cash);  self.onehalfloss2()

    def onehalfloss2(self):
        self.c += 1
        if (self.list[self.c]) > 18:
            self.cash += 20;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 20;
            print("loss", self.cash);
            self.onehalfloss3()

    def onehalfloss3(self):
        self.c += 1
        if (self.list[self.c]) >18 :
            self.cash += 40;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 40;
            print("loss", self.cash);
            self.onehalfloss4()

    def onehalfloss4(self):
        self.c += 1
        if (self.list[self.c]) >18 :
            self.cash += 80;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 80;
            print("loss", self.cash);
            self.onehalfloss5()

    def onehalfloss5(self):
        self.c += 1
        if (self.list[self.c]) > 18:
            self.cash += 160;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 160;
            print("loss", self.cash);
            self.onehalfloss6()

    def onehalfloss6(self):
        self.c += 1
        if (self.list[self.c]) <19 :
            self.cash += 320;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 320;
            print("loss", self.cash);
            self.onehalfloss7()

    def onehalfloss7(self):
        self.c += 1
        if (self.list[self.c]) <19:
            self.cash += 640;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 640;
            print("loss", self.cash);
            self.logicKick()

    ################# 2nd half Gain #####################
    def scndhalfgain(self):

        if (self.list[self.c]) <19 :
            self.cash += 5; print("Gain", self.cash); self.logicKick()
        else:
            self.cash -= 5;print("loss", self.cash);self.onehalfloss1()

    def scndhalfloss1(self):
        self.c+=1
        if (self.list[self.c]) <19:
            self.cash += 10; print("Gain", self.cash);   self.logicKick()
        else:
            self.cash -= 10; print("loss", self.cash);  self.onehalfloss2()

    def scndhalfloss2(self):
        self.c += 1
        if (self.list[self.c]) <19:
            self.cash += 20;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 20;
            print("loss", self.cash);
            self.onehalfloss3()

    def scndhalfloss3(self):
        self.c += 1
        if (self.list[self.c]) <19 :
            self.cash += 40;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 40;
            print("loss", self.cash);
            self.onehalfloss4()

    def scndhalfloss4(self):
        self.c += 1
        if (self.list[self.c]) <19 :
            self.cash += 80;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 80;
            print("loss", self.cash);
            self.onehalfloss5()

    def scndhalfloss5(self):
        self.c += 1
        if (self.list[self.c]) <19:
            self.cash += 160;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 160;
            print("loss", self.cash);
            self.onehalfloss6()

    def scndhalfloss6(self):
        self.c += 1
        if (self.list[self.c]) <19 :
            self.cash += 320;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 320;
            print("loss", self.cash);
            self.onehalfloss7()

    def scndhalfloss7(self):
        self.c += 1
        if (self.list[self.c]) <19 :
            self.cash += 640;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 640;
            print("loss", self.cash);
            self.logicKick()

  #################### part1 3gain #####################
    def part1_3gain(self):

        if (self.list[self.c]) >12 and (self.list[self.c])<22 :
            self.cash += 15; print("Gain", self.cash); self.logicKick()

        elif (self.list[self.c]) >24 and (self.list[self.c])<37 :
            self.cash += 15; print("Gain", self.cash); self.logicKick()
        else:
            self.cash -=10;print("loss", self.cash);self.part1_3loss1()


    def part1_3loss1(self):
        self.c += 1
        if (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 30;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 30;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 20;
            print("loss", self.cash);
            self.part1_3loss2()


    def part1_3loss2(self):
        self.c += 1
        if (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 60;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 60;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 40;
            print("loss", self.cash);
            self.part1_3loss3()


    def part1_3loss3(self):
        self.c += 1
        if (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 120;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 120;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 80;
            print("loss", self.cash);
            self.part1_3loss4()


    def part1_3loss4(self):
        self.c += 1
        if (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 120;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 120;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 80;
            print("loss", self.cash);
            self.part1_3loss5()


    def part1_3loss5(self):
        self.c += 1
        if (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 240;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 240;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 160;
            print("loss", self.cash);
            self.part1_3loss6()


    def part1_3loss6(self):
        self.c += 1
        if (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 480;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 480;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 320;
            print("loss", self.cash);
            self.part1_3loss7()


    def part1_3loss7(self):
        self.c += 1
        if (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 960;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 960;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 640;
            print("loss", self.cash);
            self.logicKick()

########################## part2_3gain ##############################
    def part2_3gain(self):

        if (self.list[self.c]) >0 and (self.list[self.c])<13 :
            self.cash += 15; print("Gain", self.cash); self.logicKick()

        elif (self.list[self.c]) >24 and (self.list[self.c])<37 :
            self.cash += 15; print("Gain", self.cash); self.logicKick()
        else:
            self.cash -=10;print("loss", self.cash);self.part2_3loss1()


    def part2_3loss1(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 30;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 30;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 20;
            print("loss", self.cash);
            self.part2_3loss2()


    def part2_3loss2(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 60;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 60;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 40;
            print("loss", self.cash);
            self.part2_3loss3()


    def part2_3loss3(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 120;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 120;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 80;
            print("loss", self.cash);
            self.part2_3loss4()


    def part2_3loss4(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 120;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 120;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 80;
            print("loss", self.cash);
            self.part2_3loss5()


    def part2_3loss5(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 240;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 240;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 160;
            print("loss", self.cash);
            self.part2_3loss6()


    def part2_3loss6(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 480;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 480;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 320;
            print("loss", self.cash);
            self.part2_3loss7()


    def part2_3loss7(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 960;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 24 and (self.list[self.c]) < 37:
            self.cash += 960;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 640;
            print("loss", self.cash);
            self.logicKick()

########################## Part3_3gain ##############################
    def part3_3gain(self):

        if (self.list[self.c]) >0 and (self.list[self.c])<13 :
            self.cash += 15; print("Gain", self.cash); self.logicKick()

        elif (self.list[self.c]) >12 and (self.list[self.c])<22 :
            self.cash += 15; print("Gain", self.cash); self.logicKick()
        else:
            self.cash -=10;print("loss", self.cash);self.part3_3loss1()


    def part3_3loss1(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 30;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 30;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 20;
            print("loss", self.cash);
            self.part3_3loss2()


    def part3_3loss2(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 60;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 60;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 40;
            print("loss", self.cash);
            self.part3_3loss3()


    def part3_3loss3(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 120;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 120;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 80;
            print("loss", self.cash);
            self.part3_3loss4()


    def part3_3loss4(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 120;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 120;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 80;
            print("loss", self.cash);
            self.part3_3loss5()


    def part3_3loss5(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 240;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 240;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 160;
            print("loss", self.cash);
            self.part3_3loss6()


    def part3_3loss6(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 480;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 480;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 320;
            print("loss", self.cash);
            self.part3_3loss7()


    def part3_3loss7(self):
        self.c += 1
        if (self.list[self.c]) > 0 and (self.list[self.c]) < 13:
            self.cash += 960;
            print("Gain", self.cash);
            self.logicKick()
        elif (self.list[self.c]) > 12 and (self.list[self.c]) < 22:
            self.cash += 960;
            print("Gain", self.cash);
            self.logicKick()
        else:
            self.cash -= 640;
            print("loss", self.cash);
            self.logicKick()

    def finalgain(self):
        print("final gain of your Roulette casino", self.cash)
        print("You have profit of",(self.cash)-1000)
        print("Do festival.....!")


obj=roulette()
obj.display()
obj.finalgain()
