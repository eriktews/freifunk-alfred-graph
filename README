# Scripts to generate graphs from alfred data

This repository contains scripts that generate graphs from freifunk alfred data in json format.

## Organization of the data

*genstats.py* assumes that the data is stored in a git repository, which contains commits that update the same file again and again. It loops through all revisions of a specific branch and parses that file.

Should your data not be formatted in that way, you may use or modify the *parse.py* script to adopt to the way your data is stored.

## Example

Assuming that you store your data in */data/git/alfred/* in a file named *159.json*. Simply run *python genstats.py /data/git/alfred/* and the output will be written to *all.dat*.

You can plot your data with *gnuplot clients.gnuplot*. However, you might want to modify the *set xrange ...* line to match the time when you started to collect your data. The output will be written to *client.png*.




