#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python program to show us how we can use the Functions
                    in Python
================================================================================'''

#-------------------------------------------#
#               void Function
#-------------------------------------------#

def Normal_Fun():
    print("Noraml Function")

Normal_Fun()

#-------------------------------------------#
#               Return Function
#-------------------------------------------#

print("-------------------")

def Mul_Fun(x):
    return (x * 3)

print( Mul_Fun(5) )
print( Mul_Fun(3) )


#-------------------------------------------#
#       Assign Value to the parameter
#-------------------------------------------#

print("-------------------")

def Youngest_Fun(Child1 , Child2 , Child3):
    print("The Youngest Child is {}" .format(Child3))

Youngest_Fun(Child3 = "Malek" , Child2 = "Youssef" , Child1 = "Ahmed")


#-------------------------------------------#
#       Default Value parameter
#-------------------------------------------#

print("-------------------")

def fruit_Fun(default_Fruit = "Banana"):
    print("i love to eat a/an  {}" .format(default_Fruit))

fruit_Fun()
fruit_Fun("Cherry")