#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python code that contains favorite websites and has a function 
                    called Firefox that takes a URL and opens a website.
================================================================================'''

import favourites

def Print_Menu():
    print()
    print("********** Menu **********")
    print("0. Exit")
    print("1. Open Facebook")
    print("2. Open Twitter")
    print("3. Open Linkedin")
    

def Get_User_Choice():
    while True:
        choice = input("Enter your choice: ")
        try:
            return int(choice)
        except ValueError:
            print("That is a wrong choice. Please enter an integer value.")

def Handle_Choice(choice):
    if   choice == 0:
        return False
    elif choice == 1:
        favourites.Firefox("https://www.facebook.com/")
    elif choice == 2:
        favourites.Firefox("https://twitter.com/?lang=en")
    elif choice == 3:
        favourites.Firefox("https://www.linkedin.com/")
    else:
        print("Invalid choice. Please try again.")

    return True


while True:
    Print_Menu()
    user_choice = Get_User_Choice()
    if not Handle_Choice(user_choice):
        break