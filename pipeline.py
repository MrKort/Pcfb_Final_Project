#! /usr/bin/env python

import os
import sys

# Please use the proper extentions for the DNA sequences (000.fnt) and the Amino Acid sequences (000.faa)
# sys.argv takes the file name you want to search. 
#Be sure to enclose it in apostorphes like: "file*.faa", if you wish to select all files of a certain type
string=sys.argv[1]

print "Showing all individual sequences from ", string, " files:"
os.system('grep ">" -h '+string+" | sort | uniq -c") 
os.system('grep ">" -h '+string+" | sort | uniq -c > workdir/seq_names.txt")

# Concatenate all files into a single inputfile for the pipeline
print "Concatenating all ", string, "files"
os.system('cat '+string+" > workdir/input.fas")
print "Starting Multiple Sequence Alignment"

# Start the Multiple Sequence Alignments
os.system('mafft workdir/input.fas > workdir/mafft_output.fas')
os.system('muscle -in workdir/input.fas -out workdir/muscle_output.fas')


