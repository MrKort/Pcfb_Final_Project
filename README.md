# Pcfb_Final_Project
Course: Bioinformatics
Owner: K. Kort
Contributor: H. Kruize
Aim of this Git: Store scripts and programs for the "Multiple Sequence Alignment - Phylogenetic tree" pipeline

To run the script the following programs are needed:
Python
Biopython
python-networkx
MAFFT
Phylip

Our pipeline is written in a python wrapper so that we can better handle program arguments.

Data retrieval:
To test the pipeline two toy datasets were retrieved from the MiST2.2 database.
File 1: DNA sequences for CheZ of 10 different species (.fnt)
File 2: protein sequences for CheZ of 10 different species (.faa)

Search RefSeq genename for CheZ, was used to retrieve the data.
These sequences were retrieved manually and the species included are the first ten in the list. If there is time left, an automatic data retrieval code could be written to retrieve specific species for a given protein (may be a challenge if we want to use the MiST database).

To find the names of the sequences and to check for unique entries do:
In command line: 
grep ">" -h (\*).fas | sort | uniq -c

In python script:
print "Showing all individual sequences from ", string, " files:"
os.system('grep ">" -h '+string+" | sort | uniq -c")

Piping this to wc -l gives the number of different species in our case.
Next all the input sequences files are combined to generate one general input file. This will make calling arguments less tedious and more general. Additionally  the number of inputfiles given by the user can vary in number.


Since the number of inputfiles can vary, combine the given inputfiles to one inputfile with cat:
print "Concatenating all ", string, "files"
os.system('cat '+string+" > input.fas")

In this file the sequences are spread over multiple lines. The line endings could be removed with an advanced search and replace in gedit (Search: ([ACGT])\n({ACGT]), Replace: \1\2). However we prefer to make this an automated process if possible.  
However this seems not to be an issue for the multiple sequence alignment with the following two aligners: MUSCLE and MAFFT.

We test the multiple sequence alignment methods muscle and mafft with default settings first.
os.system('mafft input.fas > mafft(\_)output.fas')
os.system('muscle -in input.fas -out muscle(\_)output.fas')

The multiple sequence alignments were visualized with Aliview, to investigate and test the different arguments available for the aligners. The default parameters of both muscle and mafft are usefull already. The gap penalties for the aligners was changed to obtain the best alignment possible for the toy set. After visualization it was decided that we would work with mafft and gap penalty 25, both openening and extending. Once the pipeline is completed, we should test the settings with a different protein.


Two freely available methods/packages were tried to construct the phylogenetic tree: Phylip and MEGA. MEGA claims to have command line functionality, yet when we want to run a function it opens a GUI. This is not what we want, because we want a fully automated pipeline. So we decided to continue with Phylip.

USING PHYLIP:
First a distance matrix has to be made based on the multiple sequence alignment.
For protein sequences the command phylip protdist has to be used, for dna sequences the command phylip dnadist needs to be used to generate the distance matrix.
The distance matrix will be fed to phylip neighbor to generate the tree. In turn, the output file from this will be given to a visualizer to visualize the tree, the phylip drawgram with default settings is good for now.

Still working on pipeline. - Kort

Trying to refine msa by muscle and mafft - H
Looking into how to make phylogenetic trees - Kort

Good morning! Look into phylogeny methods, will work with manually adapted files for now. - H

Today we have to finish the pipeline, for now I will start with the presentation. - H
