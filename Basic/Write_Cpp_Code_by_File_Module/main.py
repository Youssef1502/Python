#!/usr/bin/python3

'''================================================================================
--    Author    :   			YOUSSEF ADEL YOUSSEF

-- Description  :   Write an application to generate C++ code and compile the code 
                    to generate the executable file, After that run this executable file.
================================================================================'''

import os
fd = open("main.cpp" , "w")
MainCpp = ' #include<iostream> \n\
    int main(){ \n\
        std::cout <<"Hello World"<<std::endl;\n\
        return 0; \n\
    } \n\
\
'

fd.write(MainCpp)
fd.close()
os.system("g++ main.cpp")
os.system("./a.out")