#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Python Script to Print Current Date and Time
================================================================================'''

import datetime

Now = datetime.datetime.now()
print("Current Date and Time : ")
print(str(Now)[0:-7])