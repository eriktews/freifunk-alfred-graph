#!/usr/bin/python

# Written by Erik Tews <erik@datenzone.de>
#
# Based on code posted by Adrian17 on
# http://codereview.stackexchange.com/questions/52198/base-for-iterating-over-git-history-is-this-code-clean
#
# Iterate through all commits of a git repository of alfred data and extract
# the nodes and client counts. The output is suiteable as a datafile for
# gnuplot.

import argparse
import os
import subprocess
import sys
import git
import json
from parse import cfile

def read_output(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    result = dict()
    for i in lines:
        [time, nodes, wifi, total ] = i.rstrip().split("\t")
	result[int(time)] = [int(nodes), int(wifi), int(total)]
    return result

def main(args):
    # Open the output file for READING, get previously written values
    data = dict()
    try:
        data = read_output(args.output)
    except:
        # happens, maybe the output file does not exist
        pass

    # Open the repository
    try:
        repo = git.Repo(args.path)
    except:
        sys.exit("no such repo")

    # Access the desired branch
    try:
        commit_ids = repo.git.rev_list(args.branch).splitlines()
    except:
        sys.exit("no such branch")

    # Iterate through all commits in forward order
    for commit_id in commit_ids:
	co = repo.commit(commit_id)
        date = co.authored_date
        # When the commit is not in the data already
	if not date in data.keys():
            if args.verbose:
                sys.stderr.write ("Updating commit ID " + commit_id + "\n")
            repo.git.checkout(commit_id)
            # Parse the file with alfred data, use the commit time as a date
	    try:
	        data[date] = cfile(args.path + "/" + args.file)
	    except:
	        if args.verbose:
                    sys.stderr.write ("Problem with commit ID " + commit_id + "\n")
        else:
            # If this commit is already known, skip all the following commits
            if args.fast:
                break

    # Open the output file for WRITING
    f = open(args.output, 'w')
    for k in sorted(data.keys()):
	# write time in epoc \t node count \t wifi count \t client count
        f.write("\t".join(map(str, [k] + data[k])) + "\n")
    f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', nargs="?", default=".", help='path to the git repository')
    parser.add_argument('--branch', '-b', default="master", help='brach in the repository')
    parser.add_argument('--file', '-f', default='159.json', help='name of the output file')
    parser.add_argument('--output', '-o', default='all.dat', help='name of the file with alfred json data in the git repository (relative to the repository root)')
    parser.add_argument('--verbose', '-v', action='store_true', help='be verbose, write additional info to stderr')
    parser.add_argument('--fast', action='store_true', help='when the first commit already parsed is encountered, skip processing of further commits')
    args = parser.parse_args()

    main(args)
    sys.exit(0)

