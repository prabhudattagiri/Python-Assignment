# 6. WAP to compute simple interest and compound interest for differentbanks like SBI,UBI, AXIS having  
# individual rate of Interest using method overriding, multiple inheritence and abstract class.

from abc import ABC
class Bank(ABC): # Abstract class
    def __init__(self,p,t):
        self.p=p
        self.t=t
        self.r=10 # roi different for different bank
    # abstract method
    def simpleInterest(self):
        pass

    def comoundInterest(self):
        pass

class SBI(Bank):
    def __init__(self,p,t):
        self.p=p
        self.t=t
        self.r=5
    
    def simpleInterest(self):
        return (self.p * self.r * self.t)/100
    def comoundInterest(self):
        return ( self.p * (1+self.r/100)** self.t - self.p )
    
class UBI(Bank):
    def __init__(self,p,t):
        self.p=p
        self.t=t
        self.r=6
    
    def simpleInterest(self):
        return (self.p * self.r * self.t)/100
    def comoundInterest(self):
        return ( self.p * (1+self.r/100)** self.t - self.p )
    
class AXIS(Bank):
    def __init__(self,p,t):
        self.p=p
        self.t=t
        self.r=7
    
    def simpleInterest(self):
        return (self.p * self.r * self.t)/100
    def comoundInterest(self):
        return ( self.p * (1+self.r/100)** self.t - self.p )
    
# In Main
p=int(input("Enter the principal amount : "))
t=int(input("Enter the time perios : "))

sbi = SBI(p,t)
print("Simple Interest of SBI is ",sbi.simpleInterest())
print("Compound Interest of SBI is ",sbi.comoundInterest())

ubi = UBI(p,t)
print("Simple Interest of UBI is ",ubi.simpleInterest())
print("Compound Interest of UBI is ",ubi.comoundInterest())

axis = AXIS(p,t)
print("Simple Interest of Axis Bank is ",axis.simpleInterest())
print("Compound Interest of Axis Bank is ",axis.comoundInterest())