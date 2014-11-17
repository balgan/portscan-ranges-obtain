import sys
import subprocess
from netaddr import IPNetwork
import os
from os import popen
import commands

FILECIDR = str(sys.argv[1])
port = str(sys.argv[2])
command = 'cat "' + FILECIDR +  '" | udpblast ' +port+' ./'+port+'.pkt 1'
#			call(["echo ",ip,"|","udpblast",port,"./53.pkt","20000"])
#			call(command,shell=True)
			#os.system('echo "' + ip +  '" | udpblast ' +port+' ./'+port+'.pkt 20000')
			#print subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).stdout.read()
p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in iter(p.stdout.readline, ''): 
	print line
