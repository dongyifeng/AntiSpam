#coding:utf-8

import sys
import math

def run(dataFileName,outFileName,wordSetFileName):
	instanceList = []
	wordDesc={}
	articleId=1
	wordSet={}
	for line in file(dataFileName,"rb"):
		if len(line)==0 or line[0]=="#":continue
		items=line.strip().rsplit(" ")
		fw.write(items[0]+" ")
		instance={}
		for word in items[1:]:
			if word not in wordSet:
				wordSet[word]=len(wordSet)+1
			wordId=wordSet[word]
			if wordId not in wordDesc:
				wordDesc[wordId]=set()
			wordDesc[wordId].add(articleId)	
			instance[wordId]=instance.get(wordId,0)+1
		calcTF(instance)
		instanceList.append(instance)
		articleId+=1
	
	calcIDF(instanceList,wordDesc,articleId)
	save(outFileName,instanceList)
	saveWordSet(wordSetFileName,wordSet)

def calcTF(instance):
	length=len(instance)
	for key in instance.keys():
		instance[key]=instance[key]/length

def calcIDF(instanceList,desc,documentCount):
	for instance in instanceList:
		for key in instance.keys():
			instance[key]=instance[key]*math.log(documentCount/(len(desc[word])+1))
def save(outFileName,instanceList)
	fw=file(outFileName,'wb')
	for instance in instanceList:
		sortedInstance=sorted(instance.items(), key=lambda x:(x[0]),)
		for pair in sortedInstance:
			fw.write(str(pair[0])+":"+str(pair[1])+" ")
		fw.write('\n')
	fw.close()

def saveWordSet(fileName,wordSet):
	fw=file(fileName,'wb')
	for word in wordSet.keys():
		fw.write(word+'\t'+str(wordSet.get(word))+'\n')
	fw.close()

def main():
	arc=len(sys.argv)
	if arc==0:
		print "Usage:python "+sys.argv[0]+" dataFileName outFileName wordSetFileName"
		return
	dataFileName=sys.argv[1]
	outFileName=sys.argv[2]
	wordSetFileName=sys.argv[3]
	run(dataFileName,outFileName,wordSetFileName)

main()
