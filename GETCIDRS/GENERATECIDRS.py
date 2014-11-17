import sys
import subprocess
from netaddr import IPNetwork
import os
COUNTRY = sys.argv[1]

FILECIDR = open(str(sys.argv[1])+".CIDR",'a')
FILEIPS = open(str(sys.argv[1])+".IPS",'a')
FILERANGES = open(str(sys.argv[1])+".RANGES",'a')
i = 0
def iplist(FILECIDR):
	global i
	FILEIPS = open(str(sys.argv[1])+".IPS",'a')
	FILECIDR = open(str(sys.argv[1])+".CIDR",'r')
	for line in FILECIDR:
		for ip in IPNetwork(line):
			i=i+1
			FILEIPS.write(str(ip)+"\n")

def main():
	print "[-]Doing the cleanup"
	try:
		os.remove(str(sys.argv[1])+".CIDR")
		os.remove(str(sys.argv[1])+".IPS")
		os.remove(str(sys.argv[1])+".RANGES")
	except:
		print "FILES DONT EXIST MOVING ON"
	print "[+]Generating ranges for " +str(COUNTRY)
	first = subprocess.call("bash genRANGE2TLD.sh " + str(COUNTRY) + " > "+ str(COUNTRY) +".RANGES", shell=True)
	print "[+]Transforming ranges into CIDRS for " +str(COUNTRY)
	second = subprocess.call("python range2cidr.py "+ str(COUNTRY) + ".RANGES > "+ str(COUNTRY) + ".CIDR", shell=True)
	FILECIDR.close()
	FILEIPS.close()
	print "[+]Transforming CIDRS into IP List for " +str(COUNTRY)
	iplist(FILECIDR)
	print "[+]DONE[+] " +str(COUNTRY) +" has "+ str(i) +" IPAddresses"
main()