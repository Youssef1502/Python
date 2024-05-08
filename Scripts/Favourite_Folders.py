#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Choose Number of the folder you need to open
================================================================================'''

import os

Favourite_Floader = [
    "/home/youssef/Documents",
    "/home/youssef/Pictures"
]

print("\n0:Documents \n1:Pictures ")
Val = int(input("Please Select Your Dir :"))


os.popen(r"nautilus {}".format(Favourite_Floader[Val]))