#coding:utf-8

import os
import sys
import random

def split(dataFileName,num):
	if not os.path.isfile(dataFileName):
		print sys.argv[0],'dataFileName:',dataFileName,'not exists'
		return
	fwList = [file(dataFileName+str(i),'wb') for i in range(num) ]
	for line in file(dataFileName,'rb'):
		index = random.randint(0,num-1)
		fwList[index].write(line)
	for item in fwList:
		item.close()

def main():
	argc=len(sys.argv)
	if argc<3:
		print sys.argv[0],'Usage:',sys.argv[0],' dataFileName num'
		return
	dataFileName = sys.argv[1]
	num = int(sys.argv[2])
	split(dataFileName,num)
main()		 
