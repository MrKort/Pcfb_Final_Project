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
print "Starting Multiple Sequence Alingment"

# Start the Multiple Sequence Alignments
os.system('mafft --localpair --maxiterate 1000 --op 5 --lop 1 workdir/input.fas > workdir/mafft_output2.fas')
os.system('mafft --localpair --maxiterate 1000 --op 15 --lop 5 workdir/input.fas > workdir/mafft_output3.fas')
os.system('mafft --localpair --maxiterate 1000 --op 25 --lop 15 workdir/input.fas > workdir/mafft_output4.fas')
os.system('mafft --localpair --maxiterate 1000 --op 25 --lop 25 workdir/input.fas > workdir/mafft_output5.fas')
os.system('mafft --localpair --maxiterate 1000 --op 250 --lop 150 workdir/input.fas > workdir/mafft_output6.fas')
os.system('muscle -gapopen -15 -gapextend -5 -in workdir/input.fas -out workdir/muscle_output2.fas')
os.system('mafft --localpair --maxiterate 1000 workdir/input.fas > workdir/mafft_output.fas')
os.system('muscle -in workdir/input.fas -out workdir/muscle_output.fas')

os.system('python stable.py workdir/input.fas workdir/muscle_output.fas > workdir/muscle_output_stable.fas')
os.system('python stable.py workdir/input.fas workdir/muscle_output2.fas > workdir/muscle_output_stable2.fas')

os.system('cat workdir/muscle_output_stable.fas workdir/muscle_output_stable2.fas > workdir/muscle.fas')
os.system('cat workdir/mafft_output.fas workdir/mafft_output2.fas workdir/mafft_output3.fas workdir/mafft_output4.fas workdir/mafft_output5.fas workdir/mafft_output6.fas > workdir/mafft.fas')
