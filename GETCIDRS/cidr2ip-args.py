import iptools
from netaddr import IPNetwork
import sys
FILE = open(sys.argv[1],'r')
FILE2 = open(sys.argv[2],'a')
ips = []
i = 0
for line in FILE:
	for ip in IPNetwork(line):
		FILE2.write(str(ip)+"\n")
