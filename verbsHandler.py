#!/bin/python3
import sys

def removeVerb(file):
	try:
		f = open(file,'r')
		contents = f.read()
		contents = contents.replace('http://','')
		contents = contents.replace('https://','')
		listContents = contents.split('\n')
		f.close()
	except:
		print('[*] File not found.')
	return listContents

def addVerb(file):
	try:
		f = open(file,'r')
		string = f.read()
		contents = string.split('\n')
		listAdd = []
		for i in range(len(contents)):
			if contents[i] != '':
				listAdd.append('http://'+contents[i])
				listAdd.append('https://'+contents[i])
	except:
		print('[*] File not found.')
	return listAdd

def set():
	if len(sys.argv) == 3:
		file = sys.argv[1]
		if sys.argv[-1] == '--add':
			listOfDomains = addVerb(file)
			get(listOfDomains,file)
		elif sys.argv[-1] == '--remove':
			listOfDomains = removeVerb(file)
			get(listOfDomains,file)
		else:
			print('[*] Invalid option provided.')
	else:
		if sys.argv[1] == '--help':
			printHelp()
		else:
			print('[*] Usage: verbsHandler.py <file-path> <options>')
def printHelp():
	help_file = open('help.txt','r')
	instruction = help_file.read()
	print(instruction)
def get(arrayFile,file):
	midList = []
	for i in range(len(arrayFile)):
		midList.append(arrayFile[i])
	name = 'result-'+file
	result = open(name,'a')
	for i in range(len(midList)):
		result.write(midList[i]+'\n')
	print('[*] Result saved in ',name)
	result.close()
set()
