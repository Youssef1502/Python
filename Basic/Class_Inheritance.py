#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python program for class to describe class inheritance
================================================================================'''

class animal:
    name = ""
    
    def __init__(self) -> None:
        print("Constructor is Called")
        
    def eat(self):
        print("eat food")

    def __del__(self):
        print("Destructor is Called")
        
        
class cat(animal):
    
    def __init__(self):
        print("Constructor is Called")
        
    def sound(self):
        print("Meaouuu")

    def __del__(self):
        print("Destructor is Called")
        
mycat = cat()
mycat.eat()
mycat.sound()