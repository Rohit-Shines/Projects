import random
import sys
sys.setrecursionlimit(5000) # this will help to ignore error of recursion 1245

class roulette():

    def __init__(self):
        self.cash = 1000
        self.cntr = 0
        self.list  = []
        for i in range(5000):self.list.append(random.randint(0, 36)) # Generates 2000 Random numbers everytime it executes
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
        while self.c<4000:      ####### this value is most important
            x=self.list[a] ; y=self.list[b]; z=self.list[self.c]
            a+=1; b+=1; self.c+=1
            print(x, y, z)

            #zero
            # if self.list[self.c]

            # EVEN
            if (x)%2==0 and (y)%2==0 and (z)%2==0 and x!=0:# even bet on odd
                print("This are even")
                self.oddgain()
            # ODD
            elif (x)%2!=0 and (y)%2!=0 and (z)%2!=0 and x!=0:# odd bet on even
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


