import iptools
from netaddr import IPNetwork
import sys
FILE = open(sys.argv[1],'r')
ips = []
i = 0
for line in FILE:
	for ip in IPNetwork(line):
	    i=i+1
print i
