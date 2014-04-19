#!/usr/bin/env python3
import os, random, sys

#TODO: this should be specified by command line argument
MAXIM_FILE=os.path.dirname(os.path.realpath(sys.argv[0])) + "/maxim.txt"

maxim=[]

f=open(MAXIM_FILE, "r")

s=f.readline()
tmpstr=''
while s!='':
	if s=='\n':
		maxim.append(tmpstr)
		tmpstr=''
	else:
		tmpstr+=s
	s=f.readline()

elem=random.randint(0, len(maxim)-1)
os.system("ttytter -ssl -keyf=.takahashi -status=\"%s\""%(maxim[elem]))
