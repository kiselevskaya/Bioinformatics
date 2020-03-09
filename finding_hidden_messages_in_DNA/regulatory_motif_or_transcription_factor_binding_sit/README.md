

# exhaustive_search.py
**motif_enumeration(dna, k, d)**

    Given a collection of strings Dna and an integer d, a k-mer is a (k,d)-motif if it appears in every string from Dna with at most d mismatches.
    Brute force (also known as exhaustive search) is a general problem-solving technique that explores all possible solution candidates and checks whether each candidate solves the problem.
    
    MotifEnumeration(Dna, k, d)
        Patterns ← an empty set
        for each k-mer Pattern in the first string in Dna
            for each k-mer Pattern’ differing from Pattern by at most d mismatches
                if Pattern' appears in each string from Dna with at most d mismatches
                    add Pattern' to Patterns
        remove duplicates from Patterns
        return Patterns
    
    (Pattern’ meeans comparing neighbors not the origin kmers)
    
    1. d-mismatch kmers from a string in Dna
          a. Get a list of kmers from a string (string list)
          b. Get a list of d-mismatch kmers from above kmers (also string list)
    
    2. Repeat step 1 in every strings in Dna
        Smaple input (Step 7)
           'ATTTGGC'    => first list of kmers from this string   =>  first list of d-neighbors
           'TGCCTTA'    => second list of kmers from this string   =>  second list of d-neighbors
           'CGGTATC'   => third list of kmers from this string   =>  third list of d-neighbors
           'GAAAATT'    => fourth list of kmers from this string   =>  fourth list of d-neighbors
    
    3. Get a list of common elements from step 2
    
    Output:
        - list of (k,d)-motifs (from neighbors list)


#   score_motifs.py

**get_count(motifs)**

    Function takes a list of strings motifs as input and returns the count matrix of motifs.
    Output: 
         - dictionary where keys are nucleotides(A, C, G, T), values are lists with counted motif nucleotides
    
**get_score(motifs)**

    Compare the i-th nucleotide of each k-mer of motifs with i-th nucleotide of consensus string.
    Output: 
        - number of all mismatches

**profile_matrix(motifs)**

    Profile matrix is the number of occurrences of the i-th nucleotide (each nucleotide at each position of k-mer) divided by t, the number of nucleotides in the column (the number of k-mers in motifs);
    Output: 
        - profile matrix as a dictionary where keys are nucleotides(A, C, G, T), values are lists

**get_consensus(motifs)**

    Consensus string is a string of most popular nucleotides in each column of the motif matrix
    Output: 
        - consensus string(motif)
    
**get_entropy(motifs)**

    Entropy is a measure of the uncertainty of a probability distribution.
    The entropy of the completely conserved column of the profile matrix is 0, which is the minimum possible entropy.
    On the other hand, a column with equally-likely nucleotides (all probabilities equal to 1/4) has maximum possible entropy 4 · 1/4 · log2 (1/4) = 2.
    In general, the more conserved the column, the smaller its entropy.
        
    Output:
        - float number
        

# median_sorting.py

**median_sorting(dna, k)**

    MedianString(Dna, k)
        distance ← ∞
        for each k-mer Pattern from AA…AA to TT…TT
            if distance > d(Pattern, Dna)
                 distance ← d(Pattern, Dna)
                 Median ← Pattern
        return Median
        
        
# profile_most_probable_kmer.py

**probability(motif, profile)**

    Multiplication of values from profile for each nucleotide in the given motif.

**profile_most_probable_kmer(text, k, profile)**

    Finds the most probable k-mer motif according to the given profile.
