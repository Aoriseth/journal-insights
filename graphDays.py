import os
import re
import csv

def addFiles(directory):
	directories = directory.getChildren()
	for direct in directories:
		if direct.isDir():
			addFiles(direct)
		else:
			fileList.append(direct)
		
def getPath(directory):
	return os.path.abspath(directory)

class File(object):
	"""docstring for File"""
	def __init__(self, arg):
		super(File, self).__init__()
		self.name = os.path.basename(arg)
		self.fullpath = arg

	def getChildren(self):
		children = []
		filedirs = os.listdir(self.fullpath)
		for file in filedirs:
			fileFile = File(self.fullpath+"\\"+file)
			children.append(fileFile)
		return children

	def isDir(self):
		return os.path.isdir(self.fullpath)

	def __str__(self):
		return self.fullpath


def wordCount(word,paragraph):
	return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), paragraph))

def saveToCsv(countMap):
	with open('output.csv','w',newline='') as output:
		writer = csv.writer(output)
		for key,value in countMap.items():
			writer.writerow([key,value])


fileList = []
file = File(getPath("notes"))
addFiles(file)
		
countDict = {}
for day in fileList:
	entry = open(day.fullpath)
	count = wordCount(" happy", entry.read())
	countDict[os.path.splitext(day.name)[0]] = count;
	print(str(count) + " " + day.name)

saveToCsv(countDict)

# for something in fileList:
# 	journalEntry = open(something.fullpath)
# 	print(journalEntry)