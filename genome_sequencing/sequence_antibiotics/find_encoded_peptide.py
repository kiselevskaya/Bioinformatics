

from RNA_into_amino_acids import *
import re


def complement(pattern):
    complement = ''
    complements = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    for i in range(len(pattern)):
        complement += complements[pattern[i]]
    return complement


def encoded_substrings(dna, peptide, GeneticCode):
    codon_size = 3
    substrings = []
    rna = dna.replace('T', 'U')
    positions = []
    for i in range(codon_size):
        # if 0 interrupts peptide the length of substring will be longer than 3*|peptide|
        amino_acid = rna_into_amino_acids(rna[i:], GeneticCode)
        match = ([x.start() for x in re.finditer(peptide, amino_acid)])
        positions.extend([(x+i)*codon_size for x in match])
    for pos in positions:
        substrings.append(dna[pos:pos+(len(peptide)*codon_size)])
    return substrings


def find_encoded_peptide(dna, peptide, GeneticCode):
    dna_substrings = encoded_substrings(dna, peptide, GeneticCode)
    complement_dna = complement(dna)
    complement_dna_substrings = encoded_substrings(complement_dna[::-1], peptide, GeneticCode)
    substrings = dna_substrings + complement_dna_substrings
    return substrings


if __name__ == '__main__':
    import os
    data_dir = os.path.abspath('..\\sequence_antibiotics\\text_files')
    dataset = open(data_dir+'\\RNA_codon_table_1.txt', 'r')
    GeneticCode = [string.strip('\n') for string in dataset.readlines()]
    dataset.close()
    GeneticCode = dict((y[0], y[1] if len(y) != 1 else '') for y in(x.split() for x in GeneticCode))

    # print(find_encoded_peptide('ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA', 'MA', GeneticCode))

    data_dir = os.path.abspath('..\\sequence_antibiotics\\text_files')
    dataset = open(data_dir+'\\EncodedPeptide\\inputs\\dataset_96_7.txt', 'r')
    input = [string.strip('\n') for string in dataset.readlines()]
    dataset.close()
    dna = input[0]
    peptide = input[1]

    # data_dir = os.path.abspath('..\\sequence_antibiotics\\text_files')
    # dataset = open(data_dir+'\\EncodedPeptide\\outputs\\dataset.txt', 'r')
    # output = [string.strip('\n') for string in dataset.readlines()]
    # dataset.close()

    print('\n'.join(find_encoded_peptide(dna, peptide, GeneticCode)))
    # print(sorted(output))
    # print(sorted(find_encoded_peptide(dna, peptide, GeneticCode)) == sorted(output))



