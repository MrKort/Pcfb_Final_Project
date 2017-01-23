#! /usr/bin/env python

import sys
import os

# Please use the proper extentions for the DNA sequences (000.fnt) and the Amino Acid sequences (000.faa)
string=sys.argv[1]
print string[:-7]


string="%s*.fnt" % (string[:-7])
print string
#rm analysis.fnt
#rm analysis.faa
#cat string***.fnt > analysis.fnt
#cat *.faa > analysis.faa
os.system('grep ">" -h '+string+" | sort | uniq -c") 

