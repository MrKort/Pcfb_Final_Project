#! /usr/bin/env python

import os
import sys

# Please use the proper extentions for the DNA sequences (000.fnt) and the Amino Acid sequences (000.faa)
# sys.argv takes the file name you want to search. 
#Be sure to enclose it in apostorphes like: "file*.faa", if you wish to select all files of a certain type
string=sys.argv[1]

# Count number of sequences and write sequence names to seq_names.txt
os.system('grep ">" -ho '+string+" | wc -l > workdir/seq_names.txt")
os.system('grep ">" -h '+string+" | sort | uniq -c >> workdir/seq_names.txt")

# Obtain and store the number of sequences from seq_names.txt
Seq_count = open("workdir/seq_names.txt")
lines_file = Seq_count.readlines()
seq_num = int(lines_file[0])
Seq_count.close()

# Print sequences to screen
print
print "Showing all", seq_num, "individual sequences from", string, "files:"
os.system('grep ">" -h '+string+" | sort | uniq -c") 
os.system('grep ">" -h '+string+" | sort | uniq -c > workdir/seq_names.txt")

# Concatenate all files into a single inputfile for the pipeline
print
print "Concatenating all", string, "files."
os.system('cat '+string+" > workdir/input.fas")
print "Starting Multiple Sequence Alignment."

os.system("sed -r -e 's/>accession:(\w+.*)\|/>\\1/' -i workdir/input.fas")

# Start the Multiple Sequence Alignments
os.system('mafft --clustalout workdir/input.fas > workdir/mafft_output.fas')
#os.system('muscle -in workdir/input.fas -clw -out workdir/muscle_output.fas')

# Open MSA output files, readlines, and store in lists
#Format_muscle = open("workdir/muscle_output.fas")
Format_mafft = open("workdir/mafft_output.fas")
#muscle = Format_muscle.readlines()
mafft = Format_mafft.readlines()

# While loop to select all lines per sequence from the outputfiles
i = 0
dictio={}
while i < seq_num:
#	muscle[i+3::22]
	dictio[i] = [mafft[i+3::22]]
	i += 1
print dictio[0]
