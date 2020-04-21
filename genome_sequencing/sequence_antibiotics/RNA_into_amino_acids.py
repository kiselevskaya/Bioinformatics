

def rna_into_amino_acids(rna, GeneticCode):
    peptide = ''
    codon_size = 3
    for i in range(len(rna)//codon_size):
        codon = rna[i*codon_size:i*codon_size+codon_size]
        peptide += (GeneticCode[codon] if GeneticCode[codon] != '' else '0')
        # peptide += GeneticCode[codon]
    return peptide
