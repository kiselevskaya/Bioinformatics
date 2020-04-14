

# RNA_into_amino_acids.py

**rna_into_amino_acids(rna, codon_table=None)**

    RNA strand is partitioned into non-overlapping 3-mers called codons.
    Codon is converted into one of 20 amino acids.
        Each of the 64 RNA codons encodes its own amino acid (some codons encode the same amino acid), with the exception of three stop codons that do not translate into amino acids and serve to halt translation.
    The "Stop" codon are not translated in this function.
    
    Output:
        - sting of amino acids(peptide)


# find_encoded_peptide.py

**find_encoded_peptide(dna, peptide, GeneticCode)**

    
