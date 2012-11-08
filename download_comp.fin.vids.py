__author__ = 'fr'
"""
Coursera Computational finance course video downloader
this script process a text file links.txt with names and links to the videos and downloads them named with proper names
"""

import urllib
import re

filename ='links.txt'

links = []
names = []

lines = open(filename, 'r').read().strip().split('\n')
num_lines = lines.__len__()
x = range(1,num_lines)

# set of lines - it takes every third starting with the first
num_line_names = x[::3]
#num_line_links = x[1::3]

#for n in num_line_names:
#    m = re.search('fin', lines[n-1:n])
#    names += lines[n-1:n][:m.start()] + lines[n-1:n][m.end():]

#for n in num_line_links:
#    links += lines[n-1:n]

for n in num_line_names:
    line = lines[n-1:n][0]
    
    # remove the colons from file names:
    m = re.search(":", line) 
    name = line[:m.start()] + line[m.end():]

    link = lines[n:n+1][0]
    
    urllib.urlretrieve (link, name+".mp4")
