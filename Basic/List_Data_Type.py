#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python program to show us how we can use the List
                    Data Type in Python
================================================================================'''

ls = [1.5 , 12 , "Ahmed" , [1 , 5.2]]

for i in ls:
    print(i)

#-------------------------------------------#
#           Update the List
#-------------------------------------------#

print("-------------------")

ls[1] = "Youssef"
for i in ls:
    print(i)

#-------------------------------------------#
#        Use slicing with List
#-------------------------------------------#

print("-------------------")

x = [1,2,3,4,5,6,7,8,9]
print(x[0:9:2])
print(x[0:9:1])
print(x[::1])
print(x[::-1])
print(x[-1])