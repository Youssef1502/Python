#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Handle the login system by Name and password
================================================================================'''

Login_Keys = {
"ahmed" : 1394,
"ali" : 6078,
"amr" : 9345    
}

Name = input("Please Enter Your Name :")
Key = int(input("Please Enter Your Password :"))

Parsing_Name = Name.strip().lower()

if Parsing_Name in Login_Keys:
    if Login_Keys[Parsing_Name] == Key:
        print("Welcome {}".format(Parsing_Name))
    else:
        print("Wrong Password")
else:
    print("Name '{}' is not found in the database".format(Name))