#!/usr/bin/env python3
#Learn   python  the  hard way p 74 ex20 
from sys import argv
import sys 
def print_all(f):
         print (f.read())


py_ver =  sys.version_info.major
print (" \n  Your python version is %d." % (py_ver))
current_file = open("ccc.txt")
print ("First let's print the whole file:\n")
print_all(current_file)         