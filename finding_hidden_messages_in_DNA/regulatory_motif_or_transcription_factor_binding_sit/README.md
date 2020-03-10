

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
        
    d(k-mer, collection of strings) -- where each string's length is at least equal to k.
    Say that Dna = {AGACCAGC, ACGTT, CACCCATGTCGG}.
    In this case, d(Pattern, Dna) is equal to the sum of distances:
        d(ACGT, AGACCAGC) + d(ACGT, ACGTT) + d(ACGT, CACCCATGTCGT) = 2 + 0 + 1 = 3.
         
    Output:
        - string (a k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers)
        
        
# profile_most_probable_kmer.py

**probability(motif, profile)**
        
    Multiplication of values from profile for each nucleotide in the given motif.
    Output:
        - float

**profile_most_probable_kmer(text, k, profile)**

    Generating a random string based on a profile matrix by selecting the i-th nucleotide in the string with the probability corresponding to that nucleotide in the i-th column of the profile matrix.
    The probability that a profile matrix will produce a given string is given by the product of individual nucleotide probabilities.
    
    Output:
        - string (k-mer most probable motif)

# greedy_motif_search.py

**greedy_motif_search(dna, k, t)**
    
    Greedy algorithms select the “most attractive” alternative at each iteration.
    
    GreedyMotifSearch(Dna, k, t)
        BestMotifs ← motif matrix formed by first k-mers in each string from Dna
        for each k-mer Motif in the first string from Dna
            Motif1 ← Motif
            for i = 2 to t
                **form Profile from motifs Motif1, …, Motifi - 1**
                Motifi ← Profile-most probable k-mer in the i-th string in Dna
            Motifs ← (Motif1, …, Motift)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        return BestMotifs
                
    http://www.mrgraeme.co.uk/greedy-motif-search/    
    
    Output:
        - list of motifs

**greedy_motif_search_with_pseudocounts(dna, k, t)**

    Profile matrix is generated using count with pseudocounts.

    GreedyMotifSearch(Dna, k, t)
        form a set of k-mers BestMotifs by selecting 1st k-mers in each string from Dna
        for each k-mer Motif in the first string from Dna
            Motif1 ← Motif
            for i = 2 to t
                **apply Laplace's Rule of Succession to form Profile from motifs Motif1, …, Motifi-1**
                Motifi ← Profile-most probable k-mer in the i-th string in Dna
            Motifs ← (Motif1, …, Motift)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        output BestMotifs
        
    Output:
        - list of motifs


# profile_matrix_with_pseudocounts.py

**count_with_pseudocounts(motifs)**

    Function takes a list of strings (motifs) as input and returns the count matrix of (motifs) with pseudocounts (added a small number) as a dictionary of lists.
    Output: 
        - dictionary where keys are nucleotides(A, C, G, T), values are lists (with counted motif nucleotides plus pseudocount)
    
    
**profile_matrix_with_pseudocounts(motifs)**

    Function takes a list of strings (motifs) as input and returns the profile matrix of (motifs) with pseudocounts as a dictionary of lists.
    The sum total of each column is the denominator of profile motifs is.
    Output: 
        - profile matrix as a dictionary where keys are nucleotides(A, C, G, T), values are lists


# distance_between_pattern_and_string.py

**distance_between_pattern_and_strings(pattern, dna)**

    DistanceBetweenPatternAndStrings(Pattern, Dna)
    k ← |Pattern|
    distance ← 0
    for each string Text in Dna
        HammingDistance ← ∞
        for each k-mer Pattern’ in Text
            if HammingDistance > HammingDistance(Pattern, Pattern’)
                HammingDistance ← HammingDistance(Pattern, Pattern’)
        distance ← distance + HammingDistance
    return distance
    
    Output:
        - integer
