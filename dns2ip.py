#!/usr/bin/python3
import re
import os
import csv
import sys

f = open(sys.argv[1], "r")
fw = open(sys.argv[2], "w")
raw_host=f.read().splitlines()

for host in raw_host:
	raw = os.popen('host ' + host).read()

	ip = re.sub(r'[a-zA-Z ]', "", raw)

	ip = re.findall(r'([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', ip)

	for i in ip:
		ips = re.sub(r'[()\' ]', "", str(i))
		ips = ips.replace(",", ".")
		fw.write("{:<40s}{:<10s}{:>10s}".format(host, ":", ips)+"\n")
		print("{:<40s}{:<10s}{:>10s}".format(host, ":", ips))
f.close()
fw.close()