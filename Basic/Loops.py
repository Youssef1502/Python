#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python program to show us how we can use Loops,
                    Break and Continue
================================================================================'''

for i in range(1,10) :
    if i %2 == 0 :
        break
    print(i , "Odd")

print("-------------------")

j=0
while j<10 :
    if j%2 == 0 :
        j+=1
        continue
    print(j , "Odd")
    j+=1

#-------------------------------------------#
#               Shorthand For
#-------------------------------------------#

print("-------------------")

[print(i) for i in range(5) if i %2 == 0]
[print(i) for i in "Youssef" ]