#!/usr/bin/python

# Written by Erik Tews <erik@datenzone.de>

# Utility to parse alfred data and extract node and client count

import json
import sys

def cfile(s):
	"""Read a file with alfred data and extract node and client count"""
	f = open(s)
	r = count(f)
	f.close()
	return r
	

def count(f):
	"""Parse JSON data and extract node and client count"""
	j = json.load(f)
	nodes = len(j)

	# Loop through all nodes, sum up client counts
	wifi = 0
	total = 0
	for i in j:
		try:
			t = j[i]['clients']
			wifi += t['wifi']
			total += t['total']
		except KeyError:
			pass
	return [nodes, wifi, total]

if __name__ == '__main__':
	[ nodes, wifi, total ] = cfile(sys.argv[1])
	print str(nodes) + "\t" + str(wifi) + "\t" + str(total)

