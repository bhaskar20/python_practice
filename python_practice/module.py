''' this is a module for practice of modules'''

import os
import sys
import urllib
def list_files(director):
	print os.error
	print os.name
	print os.getcwd()
	result={}
	for i in os.listdir(director):
		a=i.split('.')
		result[a[1]]=result.get(a[1],0)+1
	return result

#print list_files(sys.argv[1])

def download(url):
	response=urllib.urlopen(url)
	content=response.readlines()
	print content
	return response.headers

#print download(sys.argv[1])

def wget(url):
	response=urllib.urlopen(url)
	content=response.read()

wget([sys.argv[1]])