

import os


def rna_into_amino_acids(rna, GeneticCode):
    peptide = ''
    codon_size = 3
    for i in range(len(rna)//codon_size):
        codon = rna[i*codon_size:i*codon_size+codon_size]
        peptide += (GeneticCode[codon] if GeneticCode[codon] != '' else '0')
        # peptide += GeneticCode[codon]
    return peptide


if __name__ == '__main__':
    import os
    data_dir = os.path.abspath('..\\sequence_antibiotics\\text_files')
    dataset = open(data_dir+'\\RNA_codon_table_1.txt', 'r')
    GeneticCode = [string.strip('\n') for string in dataset.readlines()]
    dataset.close()
    GeneticCode = dict((y[0], y[1] if len(y)!=1 else '') for y in(x.split() for x in GeneticCode))

    dataset = open(data_dir+'\\RNAintoAminoAcids\\inputs\\dataset_96_4.txt', 'r')
    rna = [string.strip('\n') for string in dataset.readlines()][0]
    dataset.close()

    print(rna_into_amino_acids(rna, GeneticCode))
