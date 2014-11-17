import commands
import redis
import sys
import subprocess
import os
from subprocess import Popen, PIPE, STDOUT
IPS = "./list.txt"
port = sys.argv[1]

def main():


	r = redis.StrictRedis(host='172.16.124.1', port=6379, db=0)
	#comm1 = subprocess.Popen('cat ./list.txt',stdout=subprocess.PIPE,shell=True)
	command1 = 'cat ' +IPS+ ' | '
	command2 = command1 + './udpblast ' +port+' ../packets/'+port+'.pkt 20000'
	p = Popen(command2, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
	stdout, stderr = p.communicate()
	output = p.stdout.read()
	#comm2 = subprocess.Popen(command2,stdin=comm1.stdout
	#comm1.stdout.close()
	print "CLOSED"
	msg = {'result': str(stdout)} 
        r.publish("udpscan", msg)
	#comm1.stdout.close()
	#r.publish("udpscan", msg)
main()
