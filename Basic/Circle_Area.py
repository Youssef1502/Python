#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Receive the Radius and Compute the Circle area
================================================================================'''

from math import pi

Radius = float(input("Input the radius of the circle : "))
print("The Area of Radius " +str(Radius) + " is :" +str(pi*(Radius**2)))