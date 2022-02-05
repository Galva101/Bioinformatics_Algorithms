# Bioinformatics Algorithms

A repository to collect implemented Bioinformatics Algorithms

## Needleman Wunsch

This implementation is based on its description in the course BIO390 given by Prof. Dr. Christian von Mering at the University of Zurich.
It uses dynamic programming on an alignment table to generate an optimal alignment including gaps.
The input parameters are the two sequences, as well as a Match-, Mismatch- and Gap penalty value.
Upon completing the table, the script iterates backwards over it to find the alignment and introduce the gaps into the sequences.
