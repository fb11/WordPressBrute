#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

"""
dorkMaker.py, generate dorks for Wordpress.

Usage:
	~$ python2 dorkMaker.py 100

	// 100 dork will be here
"""



import urllib2
import random
import sys

wordPressDorks = ['("Just another WordPress site")', '("Comment on Hello world!")', '("Mr WordPress on Hello world!")', '("uncategorized")', '("author/admin")', '("Comentarios en Hello world!")']
wordsSite      = "http://dpaste.com/1RGD1MK.txt"
words = urllib2.urlopen(wordsSite).read().split("\n")
dorks = []


def getRandomWord():
	''' Get random words '''

	return random.choice(words)

def generateDork(x):
	''' Generate Dorks'''

	for i in range(1, int(x)+1):
		dork = random.choice(wordPressDorks) + getRandomWord()
		dorks.append(dork)

	return dorks

if __name__ == "__main__":
	''' When script runs directly '''
	
	if len(sys.argv) == 2:
		print "\n" + "-"*60
		for dork in generateDorks(sys.argv[1]):
			print dork
		print "\n" + "-"*60
		print "\n[+] %s dork generated!"%(len(dorks))

	else:
		sys.exit()
