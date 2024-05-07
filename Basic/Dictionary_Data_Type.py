#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python program to show us how we can use the Dictionary
                    Data Type in Python
================================================================================'''

Dic = {
    "Brand" : "Ford",
    "Electric" : False,
    "Year" : 1964,
    "Colors" : ["Red" , "White" , "Blue"]
}

print(type(Dic))
print(Dic)
print(Dic.keys())
print(Dic.values())
print(Dic["Brand"])
print(len(Dic))

#-------------------------------------------#
#           Dictionary Trick
#-------------------------------------------#

print("-------------------")

Dictt = {
    "ID" : 123,
    "Name" : "Ahmed",
    "Name" : "Youssef",
    "Email" : "youssef.adel.elawady@gmail.com"
}

print(Dictt["Name"])