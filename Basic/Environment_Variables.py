#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Program to access environment variables
================================================================================'''

import os

# Access All Environment Variables
print(os.environ)

# Access a Particular Environment Variables
print(os.environ['HOME'])
print(os.environ['PATH'])