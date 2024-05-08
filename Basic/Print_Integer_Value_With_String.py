#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python program to show us how we can print integer
                    value with string
================================================================================'''

Number = int(input("Please Enter Value : "))

print(f"The Value is {Number}")
print("The Value is %d" %Number)
print("The Value is {}".format(Number))
print("The Value is "+str(Number))

# It works only with print
print("The Value is",Number)