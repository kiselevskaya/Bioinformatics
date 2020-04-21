from RNA_into_amino_acids import *
import re


def reverse_complement(pattern):
    complement = ''
    complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for i in range(len(pattern)):
        complement += complements[pattern[i]]
    return complement[::-1]


def rna_to_substring(rna, peptide, GeneticCode):
    pattern = '0*'.join(list(peptide))
    aa = rna_into_amino_acids(rna, GeneticCode)
    pos = [list(i.span()) for i in re.finditer(pattern, aa)]
    rna_pos = [[(x*3) for x in pos] for pos in pos]
    sub = [rna[y[0]:y[1]].replace('U', 'T') for y in rna_pos]
    return sub


def find_encoded_peptide(dna, peptide, GeneticCode):
    mRNA = dna.replace('T', 'U')
    rDNA = reverse_complement(dna)
    rRNA = rDNA.replace('T', 'U')
    mRNAs = [mRNA[i:] for i in range(3)]
    rRNAs = [rRNA[j:] for j in range(3)]
    substrings = []
    for n in mRNAs:
        substrings.extend(rna_to_substring(n, peptide, GeneticCode))
    for m in rRNAs:
        for l in rna_to_substring(m, peptide, GeneticCode):
            substrings.append(reverse_complement(l))
    return substrings
