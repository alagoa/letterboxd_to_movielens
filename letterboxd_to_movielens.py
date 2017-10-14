#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import imdb
import sys

if len(sys.argv) < 2:
	print "Usage: python letterboxd_to_movielens.py <filename>"
	sys.exit()

ia = imdb.IMDb()

out = "\"position\",\"const\",\"created\",\"modified\",\"description\",\"Title\",\"Title type\",\"Directors\",\"You rated\",\"IMDb Rating\",\"Runtime (mins)\",\"Year\",\"Genres\",\"Num. Votes\",\"Release Date (month/day/year)\",\"URL\"\n"

with open(sys.argv[1]) as fin:
    content = csv.reader(fin, delimiter=',')
    n_movies = len(list(content)[1:])
    fin.seek(0)
    content.next()
    for idx,row in enumerate(content):
		movie = ia.search_movie(row[1])[0]
		url = ia.get_imdbURL(movie)
		print str(idx+1) + "/" + str(n_movies)
		out += "\"" + str(idx+1) + "\",\"" + url.split('/')[4] + "\",\" \",\" \",\" \",\"" + row[1] + "\",\" \",\" \",\"" + str(int(float(row[4].strip())*2)) + "\",\" \",\" \",\"" + row[2] + "\",\" \",\" \",\" \",\"" + url + "\"\n"
with open("ratings.csv", "w") as fout:
    fout.write(out)
print "Done!"
