#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python program to show us how we can use the Range Function
                    in Python
================================================================================'''

for i in range(5):
    print(i , end=", ")
print()

#-------------------------------------------#
#       Range Function with Steps
#-------------------------------------------#

print("-------------------")

for i in range(2,8,2):
    print(i , end=", ")
print()

#-------------------------------------------#
#          Use Range with List
#-------------------------------------------#

print("-------------------")

ThisList = list(range(5))
print(ThisList)