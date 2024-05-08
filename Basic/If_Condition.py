#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python program to show us how we can use If Condition
================================================================================'''

A = 5
B = 20
if A>B :
    print("A is greater than B")
elif A<B :
    print("B is greater than A")
else :
    print("A equal B")

#-------------------------------------------#
#               Shorthand If
#-------------------------------------------#

print("-------------------")

print("A") if A > B else print("=") if A == B else print("B")

#-------------------------------------------#
#        pass Keyword mean empty { }
#-------------------------------------------#

print("-------------------")

if A < B :
    pass


