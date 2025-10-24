This Python project focuses on processing and analyzing DNA sequences , an essential part of research in genetics, molecular biology, and medicine. The program helps users understand genetic data by performing various operations such as validation, pattern searching, base counting, replacement, RNA conversion, and complementary strand generation.

Through this project, users can explore how DNA sequences are analyzed computationally and how small sequence changes can be detected and manipulated using programming logic.

Technologies Used:
Python 3
Basic concepts of strings, loops, conditionals, lists, and dictionaries

INPUT FORMAT:
The program accepts the following inputs from the user:
1.Number of DNA sequences (n)
2.The DNA sequences themselves (one per line)
3.Specific sequence to search (e.g., TATAAA)
4.Base to count (e.g., A)
5.Substring to replace (e.g., AT)
6.String to replace it with (e.g., X)
7.Characters to replace for RNA conversion:
    i)Character to replace (e.g., T)
    ii)Replacement character (e.g., U)
8.Pattern to find position (e.g., CGT)


The program performs the following operations on DNA sequences:

Validation:
Checks whether each DNA sequence contains only valid nucleotides — A, C, G, T.
    Displays Valid or Invalid accordingly.

Pattern Search:
Searches for the TATAAA sequence (a common promoter signal in genes) and displays whether it is a Match or No Match.

Base Count:
Counts the occurrences of the nucleotide A (adenine) in each sequence.

Unique Base Frequency:
Combines all sequences and stores the frequency of unique bases (A, T, G, C) in a dictionary.

Substring Replacement:
Replaces a user-specified substring (e.g., “AT”) with another character (e.g., “X”) within each DNA sequence.

DNA to RNA Conversion:
Converts each DNA sequence to its RNA equivalent by replacing T with U.

Pattern Position Search:
Finds and displays the position (index) of a specific pattern in each DNA sequence if it exists.

Complementary Strand Generation:
Computes the complementary strand for each DNA sequence, where:
      A ↔ T
      C ↔ G

HOW IT WORKS:
User Input Phase:
The program accepts multiple DNA sequences and related parameters.

Validation Phase:
Each DNA sequence is checked for valid nucleotide bases (A, C, G, T).
If any invalid base (e.g., X, Z, B) is found, it’s marked as Invalid, and other operations are skipped for that sequence.
Analysis Phase:
Searches for the “TATAAA” motif.
Counts occurrences of ‘A’.
Records frequency of unique bases (only from valid sequences).
Performs substring replacement.
Converts to RNA by replacing ‘T’ with ‘U’.
Searches for specific patterns and positions.

Result Phase:
Displays all processed results clearly for each DNA sequence, including complementary strands and overall statistics.

SAMPLE INPUT:
4  
ATCGTATAAA  
TTAAGCGT  
AGTXCGAT  
CCGTATTA  
TATAAA  
A  
AT  
X  
T  
U  
CG

SAMPLE OUTPUT:
DNA sequence 1: Valid  
DNA sequence 2: Valid  
DNA sequence 3: Invalid  
DNA sequence 4: Valid  

DNA sequence 1: Match  
DNA sequence 2: No Match  
DNA sequence 3: No Match  
DNA sequence 4: No Match  

DNA sequence 1: 3  
DNA sequence 2: 2  
DNA sequence 3: -  
DNA sequence 4: 2  

Frequency of Unique Bases: {'A': 7, 'T': 7, 'G': 4, 'C': 4}  

DNA sequence 1 after replacement: XCGXTAXAA  
DNA sequence 2 after replacement: TXAAGCGT  
DNA sequence 3 after replacement: Invalid Sequence  
DNA sequence 4 after replacement: CCGTXTXA  

DNA to RNA: ['AUCGAUAAA', 'UUAAUCGU', 'Invalid', 'CCGUAUUA'] 

Position of given pattern in DNA sequence 1: 2  
Position of given pattern in DNA sequence 2: 5  
Position of given pattern in DNA sequence 3: Invalid Sequence  
Position of given pattern in DNA sequence 4: Not Found  

Complementary strand of DNA sequence 1: TAGCATATTT  
Complementary strand of DNA sequence 2: AATTGCGA  
Complementary strand of DNA sequence 3: Invalid Sequence  
Complementary strand of DNA sequence 4: GGCATAAT  
