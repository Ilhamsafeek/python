class Family:

    #inbuild initial function - executes automatically
    def __init__(self,familyname):
            self.name=familyname

    #user defined function
    def Ismail(self,x):
        print("Iam Ismail "+self.name)
        y=x*5
        print("answer is "+str(y))
    
    def Ishhaq(self):
        print("Iam Ishhaq "+self.name)


Family("Ziyam").Ismail(10)
