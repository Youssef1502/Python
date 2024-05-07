#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python program to show us how we can use the Set
                    Data Type in Python
================================================================================'''

import time

Set_Values = {"Cherry" , "Banana" , "apple"}
print(Set_Values)


#-------------------------------------------#
#   A set is faster than a list in search
#-------------------------------------------#

print("-------------------")

# Creating a list of numbers
Numbers_List = list(range(1,1000001))

# Creating a Set of numbers
Numbers_Set = set(Numbers_List)

# Searching for a number in a list
Start_Time = time.time()
print(1000000 in Numbers_List)
End_Time = time.time()
print("The Taken Time to Search in List : " , End_Time - Start_Time , "Seconds")

# Searching for a number in a Set
Start_Time = time.time()
print(1000000 in Numbers_Set)
End_Time = time.time()
print("The Taken Time to Search in Set : " , End_Time - Start_Time , "Seconds")


