from math import pi
def vol_calc():
    r = input("What is the radium of the sphere?")
    volume = pi * (4/3) * float(r)**3
    print("The volume is : "+str(volume))

vol_calc()