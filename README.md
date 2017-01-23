# Pcfb_Final_Project
Course: Bioinformatics
Owner: K. Kort
Contributor: H. Kruize
Aim of this Git: Store scripts and programs for the "Multiple Sequence Alignment - Phylogenetic tree" pipeline


To find the names of the sequences do:
grep ">" -h (\*).fas | sort | uniq -c

Data retrieval:
To test the pipeline four toy datasets were retrieved from the MiST2.2 database.
File 1: DNA sequences for CheA of 10 different species
File 2: protein sequences for CheA of 10 different species
File 3: DNA sequences for CheZ of 10 different species
File 4: protein sequences for CheZ of 10 different species

Search RefSeq genename for CheA or CheZ, was used to retrieve the data.
These sequences were retrieved manually and the species included are the first ten in the list.
