# Pcfb_Final_Project
Course: Bioinformatics
Owner: K. Kort
Contributor: H. Kruize
Aim of this Git: Store scripts and programs for the "Multiple Sequence Alignment - Phylogenetic tree" pipeline

Our pipeline is written in a python wrapper so that we can better handle program arguments.

Data retrieval:
To test the pipeline four toy datasets were retrieved from the MiST2.2 database.
File 1: DNA sequences for CheZ of 10 different species (.fnt)
File 2: protein sequences for CheZ of 10 different species (.faa)

Search RefSeq genename for CheZ, was used to retrieve the data.
These sequences were retrieved manually and the species included are the first ten in the list.

To find the names of the sequences and to check for unique entries do:
In command line: 
grep ">" -h (\*).fas | sort | uniq -c

In python script:
print "Showing all individual sequences from ", string, " files:"
os.system('grep ">" -h '+string+" | sort | uniq -c")

Piping this to wc -l gives the number of different species in our case.
Next all the input sequences files are combined to generate one general input file. This will make calling arguments less tedious and more general , the number of inputfiles given by the user can vary in number.


Since the number of inputfiles can vary, combine the given inputfiles to one inputfile with cat:
print "Concatenating all ", string, "files"
os.system('cat '+string+" > input.fas")

In this file the sequences are spread over multiple lines. The line endings could be removed with an advanced search and replace in gedit (Search: ([ACGT])\n({ACGT]), Replace: \1\2). 
However this seems not to be an issue for the multiple sequence alignment with the following two aligners:
We test the multiple sequence alignment methods muscle and mafft.
os.system('mafft input.fas > mafft(\_)output.fas')
os.system('muscle -in input.fas -out muscle(\_)output.fas')


Started working on pipeline. - Kort
