#! /usr/bin/env python
import os
import sys

# Please use the proper extentions for the DNA sequences (000.fnt) and the Amino Acid sequences (000.faa)
# sys.argv takes the file name you want to search. 
#Be sure to enclose it in apostorphes like: "file*.faa", if you wish to select all files of a certain type
string=sys.argv[1]
os.system("mkdir workdir/")

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
os.system("sed -r -e 's/>accession:(\w+.*)\|/>\\1/g' -i workdir/input.fas")
os.system("sed -r -e 's/[A-Z]{2}\_//g' -i workdir/input.fas")
os.system("sed -r -e 's/\.//g' -i workdir/input.fas")
os.system("sed -r -e 's/\|/ /g' -i workdir/input.fas")

# Run the Multiple Sequence Alignments
os.system("mafft --localpair --maxiterate 1000 --lop 15 --lexp 5 --clustalout workdir/input.fas > workdir/mafft_output.fas")

# Determine the amount of blocks of sequences
os.system("grep '^$' workdir/mafft_output.fas | wc -l > workdir/blocks.txt")
Blocks = open("workdir/blocks.txt")
blocks = Blocks.readlines()
Blocks.close()
seq_blocks = int(blocks[0])-1 # Minus 1 because of the extra line behind the header

# Open MSA output file, read lines, and store in list
Mafft = open("workdir/mafft_output.fas")
mafft = Mafft.readlines()
Mafft.close()

# While loop to select all lines per sequence from the outputfile list
i = 0
dictio={}
while i < seq_num:
	dictio[i] = mafft[i+3::seq_num+2]
	i += 1

# Remove the Sequence names from the MAFFT output so the sequence lenght can be calculated
os.system("sed -r -e 's/.+\s//g' -i workdir/mafft_output.fas")

# Open MSA output file, read lines, and store in list
Mafft = open("workdir/mafft_output.fas")
mafft2 = Mafft.readlines()
Mafft.close()

# While loop to select all lines per sequence for the outputfile list
i = 0
seqio={}
while i < seq_num:
	seqio[i] = mafft2[i+3::seq_num+2]
	i += 1

# While loop to count the sequence length of the alignment
i = 0
seq_len = 0
while i < seq_blocks:
	seq_len += len(seqio[0][i])
	i += 1

# Double while loop to write PHYLIP format to output file
out=open("workdir/mafft_output.phy", "w")
out.write(str(seq_num)+"\t"+str(seq_len)+"\n") # Write PHYLIP header
i = 0
while i < seq_blocks:
	j = 0
	while j < seq_num:
		out.write(dictio[j][i]) # Write blocks of sequences to file
		j += 1
	out.write('\n') # Give a newline in between blocks
	i += 1
out.close()

# rm phylip files first! - clean up last run
# if string[-3:] == "fnt"
# 	phylip dnadist < input > screenout
# elif string[-3:] == "faa"
# 	phylip protdist < input > screenout
# mv outfile > workdir/distance.dat
# write "Y" in distance.dat header for screenout
# phylip neighbor < workdir/distance.dat > screenout

# Instead of phylip draw function, biopython could be used for tree visualization
