#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python code to explain the difference between 
                    function pass by value and function pass by reference.
================================================================================'''

def modify_value(x):
    print("Inside modify_value function, before modifying:", x)
    x = 10
    print("Inside modify_value function, after modifying:", x)

def modify_list(lst):
    print("Inside modify_list function, before modifying:", lst)
    lst.append(4)
    print("Inside modify_list function, after modifying:", lst)

#-------------------------------------------#
#              Passed by value
#-------------------------------------------#

a = 5
print("Before calling modify_value: function", a)
modify_value(a)
print("After calling modify_value function:", a)

print("\n")

#-------------------------------------------#
#              Passed by reference
#-------------------------------------------#

b = [1, 2, 3]
print("Before calling modify_list function:", b)
modify_list(b)
print("After calling modify_list function:", b)
