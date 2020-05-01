

# RNA_into_amino_acids.py

**rna_into_amino_acids(rna, codon_table=None)**

    RNA strand is partitioned into non-overlapping 3-mers called codons.
    Codon is converted into one of 20 amino acids.
        Each of the 64 RNA codons encodes its own amino acid (some codons encode the same amino acid), with the exception of three stop codons that do not translate into amino acids and serve to halt translation.
    The "Stop" codons are not translated in this function.
        (for the purpose of find_encoded_peptide "Stop" codons are  translated as '0')
    
    Output:
        - sting of amino acids(peptide)


# find_encoded_peptide.py

**find_encoded_peptide(dna, peptide, GeneticCode)**

    For DNA and its reverse complement creates RNAs.
    For each RNA creates array with 3(codon size) sub RNAs which starts from 0, 1 or 2 index respectively.
    Translate RNAs to amino acids.
    For each RNA finds (start, end) positions where appears given peptide.
    Then multiplies positions on codon size getting real positions of encoded peptide in RNA.
    Translates sub RNA to sub DNA and remembers into substring array, for reverse comlement RNA firstly runs reverse_complement().
    
    Output:
        - list of substrings of DNA 


# count_peptides.py

**counting_mass(Mass, masslist)**

    Counts number of all possible peptides with given mass.               
    Output:
        - integer
        
        For large m, the number of peptides with given integer mass m can be approximated as k · C^m, where k and C are constants.
            If suppose k=1, m1 = 800, m2 = 1600
            C = (count_mass(m2)/count_mass(m1))**(1/(m2-m1))
            C = (109000330554114810/39575132)**(1/(1600-800)) 
               
        Number of all possible subpeptide cyclopeptide of peptide length n
            n = 17691   
            a = n*(n+1)/2 + 1   # == 156494587
    
    
# linear_spectrum.py

**linear_spectrum(peptide, MassDictionary)**

    LinearSpectrum(Peptide, Alphabet, AminoAcidMass)
    PrefixMass(0) ← 0
    for i ← 1 to |Peptide|
        for every symbol s in Alphabet
            if s = i-th amino acid in Peptide
                PrefixMass(i) ← PrefixMass(i − 1) + AminoAcidMass[s]
    LinearSpectrum ← a list consisting of the single integer 0
    for i ← 0 to |Peptide| − 1
        for j ← i + 1 to |Peptide|
            add PrefixMass(j) − PrefixMass(i) to LinearSpectrum
    return sorted list LinearSpectrum
    
    Output:
        - list of integers corresponding to mass spectrum


# cyclospecrum.py

**cyclospectrum(peptide, MassDictionary)**

    CyclicSpectrum(Peptide, Alphabet, AminoAcidMass)
    PrefixMass(0) ← 0
    for i ← 1 to |Peptide|
        for every symbol s in Alphabet
            if s = i-th amino acid in Peptide
                PrefixMass(i) ← PrefixMass(i − 1) + AminoAcidMass﻿[s]
    peptideMass ← PrefixMass(|Peptide|)
    CyclicSpectrum ← a list consisting of the single integer 0
    for i ← 0 to |Peptide| − 1
        for j ← i + 1 to |Peptide|
            add PrefixMass(j) − PrefixMass(i) to CyclicSpectrum
            if i > 0 and j < |Peptide|
                add peptideMass - (PrefixMass(j) − PrefixMass(i)) to CyclicSpectrum
    return sorted list CyclicSpectrum
    
    Output:
        - list of integers corresponding to mass spectrum


# cyclopeptide_sequencing.py

**cyclopeptide_sequencing(spectrum)**

    CyclopeptideSequencing(Spectrum)
        CandidatePeptides ← a set containing only the empty peptide
        FinalPeptides ← empty list of strings
        while CandidatePeptides is nonempty
            CandidatePeptides ← Expand(CandidatePeptides)
            for each peptide Peptide in CandidatePeptides
                if Mass(Peptide) = ParentMass(Spectrum)
                    if Cyclospectrum(Peptide) = Spectrum and Peptide is not in ﻿FinalPeptides
                        append Peptide to FinalPeptides
                    remove Peptide from CandidatePeptides
                else if Peptide is not consistent with Spectrum
                    remove Peptide from CandidatePeptides
        return FinalPeptides
        
    Output:
        - an array collection of peptides respective to the given spectrum
        
**expansion(candidate_peptides, aminoAcids)**

    Adds to each peptide from candidate_peptides each of peptides from aminoAcids
    Output:
        - an array of modified(expanded through adding one amino acid) peptides


**peptides_collection_as_amino_masses(collection)**

    Transfers peptide from an alphabetic form into the sequence of mass
    Output:
        - string of unique sequences of masses
        

# score_peptide.py   

**score_peptide(peptide, spectrum)**

    Counts matches of a theoretical spectrum of a peptide and experimental.
        Mass spectrometers generate "noisy" spectra that are far from ideal — they are characterized by having both **false masses** and **missing masses**.

    Output:
        - an integer number of matches


# leaderboard_cyclopeptide_sequencing.py

**leaderboard_cyclopeptide_sequencing(spectrum, n)**
    
    LeaderboardCyclopeptideSequencing(Spectrum, N)
        Leaderboard ← set containing only the empty peptide
        LeaderPeptide ← empty peptide
        while Leaderboard is non-empty
            Leaderboard ← Expand(Leaderboard)
            for each Peptide in Leaderboard
                if Mass(Peptide) = ParentMass(Spectrum)
                    if Score(Peptide, Spectrum) > Score(LeaderPeptide, Spectrum)
                        LeaderPeptide ← Peptide
                else if Mass(Peptide) > ParentMass(Spectrum)
                    remove Peptide from Leaderboard
            Leaderboard ← Trim(Leaderboard, Spectrum, N)
        output LeaderPeptide
            (A cut should include anyone who is tied with the Nth-place competitor. Thus, Leaderboard should be trimmed down to the “N highest-scoring linear peptides including ties”, which may include more than N peptides.)
    
    Output:
        - best suited peptide (multiple solutions may exist)
