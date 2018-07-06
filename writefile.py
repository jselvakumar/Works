#!/usr/bin/python

staging = open("file.txt","w")
input = ["typical input given to new file \n", "next line 1 \n", "next line 2 \n"]
staging.writelines(input)
staging.close()
