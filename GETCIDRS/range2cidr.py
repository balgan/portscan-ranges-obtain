#!/usr/bin/env python
from netaddr import IPRange
from sys import argv

lst=open(argv[1],'r').readlines()
t=[]
for n in lst: t.append(n.strip())
lst=t
del t

for ipr in lst:
  ipr=IPRange(ipr[:ipr.find('-')],ipr[ipr.find('-')+1:])
  for cidr in ipr.cidrs():
    print cidr

