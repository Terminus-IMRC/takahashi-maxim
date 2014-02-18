#!/usr/bin/env python3
import os, random

#TODO: this should be specified by command line argument
MAXIM_FILE="maxim.txt"

maxim=[]

f=open(MAXIM_FILE, "r")

s=f.readline()
tmpstr=''
while s!="":
	if s=='\n':
		maxim.append(tmpstr)
		tmpstr=''
	else:
		tmpstr+=s
	s=f.readline()

elem=random.randint(0, len(maxim)-1)
os.system("ttytter -ssl -status=\"%s\""%(maxim[elem]))
