#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python program to show us how we can use the Tuple
                    Data Type in Python
================================================================================'''

Tu = (1.5 , 12 , "Ahmed" , [1 , 5.2])

for i in Tu:
    print(i)

#-------------------------------------------#
#        You Can't Update the Tuple
#-------------------------------------------#

# Tu(1) = "Youssef"

#-------------------------------------------#
#        Use slicing with Tuple
#-------------------------------------------#

print("-------------------")

x = (1,2,3,4,5,6,7,8,9)
print(x[0:9:2])
print(x[0:9:1])
print(x[::1])
print(x[::-1])
print(x[-1])