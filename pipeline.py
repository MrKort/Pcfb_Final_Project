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
os.system("clear")
print "Showing all", seq_num, "individual sequences from", string, "files:"
os.system('grep ">" -h '+string+" | sort | uniq -c") 

# Concatenate all files into a single inputfile for the pipeline
print
print "Concatenating all", string, "files."
os.system('cat '+string+" > workdir/input.fas")
print "Starting Multiple Sequence Alignment."

# Sed to get clear sequence headers to numbers only (01234)
os.system("sed -r -e 's/>accession:(\w+.*)\|/>\\1/' -i workdir/input.fas")
os.system("sed -r -e 's/[A-Z]{2}\_//g' -i workdir/input.fas")
os.system("sed -r -e 's/\.//g' -i workdir/input.fas")
os.system("sed -r -e 's/\|/ /g' -i workdir/input.fas")

# Start the Multiple Sequence Alignments
os.system('mafft --localpair --maxiterate 1000 --lop 15 --lexp 5 --clustalout workdir/input.fas > workdir/mafft_output.fas')

# Open MSA output files, readlines, and store in lists
Format_mafft = open("workdir/mafft_output.fas")
mafft = Format_mafft.readlines()

# While loop to select all lines per sequence from the outputfiles
i = 0
dictio={}
out=open("test.txt", "w")
while i < seq_num:
	dictio[i] = [mafft[i+3::seq_num+2]]
	i += 1
print dictio[0]
#out.write(dictio[0])


# Need to count the characters in the aligned sequences


# Need to print in format:
# Sequence number ##whitespace## Characters in sequence
# Y (for screenout functionality)
# ##blank line##
# First block (Names sequences)
# Second block (Names sequences)
#
# rm phylip files first! - clean up last run
# phylip dnadist < input > screenout
# phylip protdist < input > screenout
# mv outfile > workdir/distance.dat
# write "Y" in distance.dat header for screenout
# phylip neighbor < workdir/distance.dat > screenout
