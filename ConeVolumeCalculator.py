# ConeVolumeCalculator.py
# Your job is to write a function in ConeVolumeCalculator.py (call
# it **calculateConeVolume()** that calculates the volume of a cone
# factor based on the Volume Calculator
# Calculator.net (http://www.calculator.net/volume-calculator.html)
import math
# Define Function below
# be sure to return an integer
def calculateConeVolume(r, h) :
    volume = 1/3*math.pi*r**2*h
    volume = round(volume, 2)
    return volume

if __name__ == '__main__':
    print("Hello user.")
    radius = float(input("What is the radius of your cone?"))
    height = float(input("What is the height of your cone?"))
    volume = calculateConeVolume(radius, height)
    volume = round(volume, 2)
    
    print("The volume of your cone is " + str(volume))
