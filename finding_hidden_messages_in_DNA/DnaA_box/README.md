

#   pattern_count.py
**pattern_count(text, pattern)**

    Counts how many times the given pattern appears in the text.    
    Output:
        -integer
    
**frequency_map(text, k)**

    Slides through the text and counts all patterns length k.    
    Output:
        - dictionary where keys are patterns and values are their count

**frequent_words(text, k)**

    Finds the most frequent patterns in the frequency_map dictionary.    
    Output:
        - list of the most common patterns

**faster_frequent_words(text, k)**

    Imports computing_frequencies function.
    Initializes frequent_patterns list.
    Sets list of patterns numbers and they count (frequency_array). Finds max count in this list.
    For each pattern number (index in frequency_array) if the count is maximal than the number (index) is transcribed to pattern and remembered to frequent_patterns.
    Note: the faster_frequent_words is fast for small k only.
    
    Output:
        - list of the most common patterns

**frequent_words_by_sorting(text, k)**

    Imports pattern_to_number_and_back.
    Adds the index of each pattern to index_array and sort the list.
    Counts and adds to count_array what number of times the index appeared. Finds the maximum number of times.
    Transcribes the most frequent number (index) to patterns.
    
    Output:
        - list of the most frequent patterns


#   reverse_complement.py
**reverse_complement(pattern)**

    Writes the complement of each nucleotide in the pattern into a string, then reversing the resulting string.
    Output:
        - string that is a reverse complement of the given pattern


#   pattern_matching.py
**pattern_matching(pattern, genome)**

    Slides through the genome and if finds a match with the pattern remembers index of started position.
    Output:
        - list of integers specifying all starting positions


#   clump_finding.py
**clump_finding(genome, k, l, t)**

    Task: Slides a window of fixed length L along the genome, looking for a region where a k-mer appears t times in short succession.
    Solution:
    Using frequency_map(text, k) function slides through the genome and counts all patterns length k.
    Remembers all patterns that appears t or more times through the genome in a list variable words.
    Using pattern_matching(pattern, genome) function for each pattern in words create list of integers specifying all starting positions of the pattern.
    Slides through the pattern matching list of indexes checks if pattern appears t times on length l.
    If gets positive result (remembers patter in variable output) or all possibilities are checked, function breaks the loop to the next pattern.
    
    Output:
        - list of k length strings, each of that appears t times on some l length part of the genome.

**clump_finding_efficient(genome, k, l, t)**

    Task: Slides a window of fixed length L along the genome, looking for a region where a k-mer appears t times in short succession.
    Solution:
    Slides through the text and remember each pattern length k as key in a dictionary with a list of all starting positions as a value.
    For each key (pattern) with the length of value t or more slides through the value (matching list of indexes) checks if the pattern appears t times on length l.
    If gets positive result (remembers patter in variable patters) or all possibilities are checked, function breaks the loop to the next pattern.
    
    Output:
        - list of k length strings, each of that appears t times on some l length part of the genome.


#   pattern_to_number_and_back.py
**pattern_to_number(pattern)**

    We need to form different possible combinations using bases. There are 4 bases - A, C, G, T.
    These are 4 different possibilities for each position.
    'k' in the k-mer indicates the number of positions. In this question, the k-mer is of length 6.
    Hence the total possible k-mers are 4^6 = 4096.
    For finding the index of the required pattern, it is mentioned to arrange the bases lexically.
    So, A is assigned 0, C is assigned 1, G is assigned 2 and T is assigned 3. So, the number sequence would look like,
    0 - AAAAAA ([0*(4^5)] + [0*(4^4)] + [0*(4^3)] + [0*(4^2)] + [0*(4^1)] + [0*(4^0)])
    1 - AAAAAC ([0*(4^5)] + [0*(4^4)] + [0*(4^3)] + [0*(4^2)] + [0*(4^1)] + [1*(4^0)])
    2 - AAAAAG ([0*(4^5)] + [0*(4^4)] + [0*(4^3)] + [0*(4^2)] + [0*(4^1)] + [2*(4^0)])
    3 - AAAAAT ([0*(4^5)] + [0*(4^4)] + [0*(4^3)] + [0*(4^2)] + [0*(4^1)] + [3*(4^0)])
    4 - AAAACA ([0*(4^5)] + [0*(4^4)] + [0*(4^3)] + [0*(4^2)] + [1*(4^1)] + [0*(4^0)])
    5 - AAAACC ([0*(4^5)] + [0*(4^4)] + [0*(4^3)] + [0*(4^2)] + [1*(4^1)] + [1*(4^0)])
    6 - AAAACG ([0*(4^5)] + [0*(4^4)] + [0*(4^3)] + [0*(4^2)] + [1*(4^1)] + [2*(4^0)])
    7 - AAAACT ([0*(4^5)] + [0*(4^4)] + [0*(4^3)] + [0*(4^2)] + [1*(4^1)] + [3*(4^0)])
    
    Output:
        - integer corresponding to nucleotide pattern

**number_to_pattern(number, k)**

    When computing pattern (eg. number_to_pattern(9904, 7)), divide 9904 by 4 to obtain a quotient of 2476 and a remainder of 0.
    This remainder represents the final nucleotide of pattern, or NumberToSymbol(0) = A.
    Then iterate this process, dividing each subsequent quotient by 4, overall times dividing equal k.
    The symbols in the nucleotide column, read upward from the bottom, yield pattern 'GCGGTAA'.

    To go backward from a base-anything number, you divide the final number (5437  in this case) by the base, 4,  k = 7 times, keeping track of the remainder: ﻿﻿
    5437 / 4 = 1359 R 1
    1359 / 4 = 339 R 3
    339 / 4 = 84 R 3
    84 / 4 = 21 R 0
    21/4 = 5 R 1
    5/4 = 1 R 1
    1/4 = 0 R 1
    Take the remainders from the bottom up and you get: 1110331, corresponding lexicographically to ﻿CCCAGGC
    
    Output:
        - string of nucleotide pattern 

**pattern_to_number_recursion(pattern)**

    If removed the final symbol from all lexicographically ordered DNA 3-mers, obtain a lexicographic order of 2-mers, where each 2-mer is repeated four times.
    Thus, the number of 3-mers occurring before AGT is equal to four times the number of 2-mers occurring before AG plus the number of 1-mers occurring before T.
    Therefore,
    PatternToNumber(AGT) = 4 · PatternToNumber(AG) + SymbolToNumber(T) = 8 + 3 = 11

    If removed the final symbol of pattern, denoted LastSymbol(Pattern), then will be obtained a (k − 1)-mer that denoted as Prefix(Pattern).
    The observation above therefore generalizes to the following formula:
    PatternToNumber(Pattern) = 4 · PatternToNumber(Prefix(Pattern)) + SymbolToNumber(LastSymbol(Pattern))
    
    Output:
        - integer corresponding to nucleotide pattern


#   computing_frequencies.py
**computing_frequencies(text, k)**

    Initialises every element in the frequency array to zero (4k operations).
    Slides through the text and for each k-mer pattern that encountered, adds 1 to the value of the frequency array corresponding to pattern
    
    Output:
        - frequency array as a list where index corresponds to pattern number.


#   skew_array.py
Replication of a reverse half-strand proceeds quickly, it lives double-stranded for most of its life.
Forward half-strand spends a much larger single-stranded and has a much higher mutation rate.

C is more frequent on the reverse half-strand than on the forward half-strand.
    C (cytosine) has a tendency to mutate into T (thymine) through **deamination** process.
G (guanine) is less frequent on the reverse half-strand than on the forward half-strand.
    Since C-G base pairs eventually change into T-A, deamination results in the decrease in guanine (G) on the reverse half-strand.
A and T are practically identical.

Finds the differences in G and C into skew_array starting with first i nucleotides of genome as 0.
Next in skew_array will be +1 if G, -1 if C, the same if A or T.
Skew should achieve a minimum at the position where the reverse half-strand ends and the forward half-strand begins, which is exactly the location of ori!

**skew_array(genome)**       
    
    Counts differences in G and C in each position of a genome.    
    Output:
        - list of skew

**minimum_skew(genome)**

    Finds all minimizing skew among all values of i (from 0 to |Genome|).    
    Output:
        - list of positions with a minimum amount of G (guanine), the location of ori.


#   hamming_distance.py
Position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ≠ qi.
Eg. CGAAT and CGGAC have 2 mismatches (**Hamming distance**).

**hamming_distance(p, q)**

    Compute the Hamming distance between two strings (p and q).    
     Output: 
        - integer number of mismatches
        
**approximate_pattern_matching(text, pattern, d)**
    
    Slides a window pattern length through the text and compare patterns considering number of mismatches (d).
    Finds all approximate occurrences of a pattern.    
    
    Output:
        - list of all started positions of approximate pattern
    
**approximate_pattern_count(text, pattern, d)**

    Couns approximate matching(no more than d) patterns.    
    Output:
         - integer


#   neighbors.py
The goal is to generate the d-neighborhood Neighbors(Pattern, d), the set of all k-mers whose Hamming distance from Pattern does not exceed d.

**immediate_neighbors(pattern)**

    Generates the 1-neigborhood of Pattern using the following pseudocode.
    
    ImmediateNeighbors(Pattern)
        Neighborhood ← the set consisting of single string Pattern
        for i = 1 to |Pattern|
            symbol ← i-th nucleotide of Pattern
            for each nucleotide x different from symbol
                Neighbor ← Pattern with the i-th nucleotide substituted by x
                add Neighbor to Neighborhood
        return Neighborhood
        
    Output:
        - set of all k-mers whose Hamming distance is 1

**neighbors(pattern, d)**
    
    For generating Neighbors(Pattern, d) remove the first symbol of Pattern (denoted FirstSymbol(Pattern)), then obtain a (k − 1)-mer that we denote by Suffix(Pattern).
    Consider a (k − 1)-mer Pattern’ belonging to Neighbors(Suffix(Pattern), d).
    By the definition of the d-neighborhood Neighbors(Suffix(Pattern), d), we know that HammingDistance(Pattern′, Suffix(Pattern)) is either equal to d or less than d.
    In the first case, add FirstSymbol(Pattern) to the beginning of Pattern’ in order to obtain a k-mer belonging to Neighbors(Pattern, d).
    In the second case, add any symbol to the beginning of Pattern’ and obtain a k-mer belonging to Neighbors(Pattern, d).
    
    The notation symbol • Text to denote the concatenation of a character symbol and a string Text, e.g., A•GCATG = AGCATG.
    
    Neighbors(Pattern, d)
        if d = 0
            return {Pattern}
        if |Pattern| = 1 
            return {A, C, G, T}
        Neighborhood ← an empty set
        SuffixNeighbors ← Neighbors(Suffix(Pattern), d)
        for each string Text from SuffixNeighbors
            if HammingDistance(Suffix(Pattern), Text) < d
                for each nucleotide x
                    add x • Text to Neighborhood
            else
                add FirstSymbol(Pattern) • Text to Neighborhood
        return Neighborhood
    
    Output:
        - set of all k-mers whose Hamming distance is d


#   search_frequent_words.py    
**frequent_words_with_mismatches(text, k, d)**

    Finds most frequent k-mer with up to d mismatches in text simply counting approximate patterns for each possiable patterns (4**k) and finding the maximizing  count.
    Pattern does not need to actually appear as a substring of text.
    
    Output:
        - list of patterns (lexicographical)
        
**frequent_words_with_mismatches_and_reverse(text, k, d)**

    Finds most frequent k-mer with up to d mismatches and reverse matches in the text.
    Count(pattern)+count(reverse pattern) and finding the maximizing  count.
    Pattern does not need to actually appear as a substring of text.
    
    Output:
        - list of patterns (lexicographical)
        

**frequent_words_with_mismatches_sorting(text, k, d)**

    Reduces the Frequent Words with Mismatches Problem to sorting.
    It first generates all neighbors (with up to d mismatches) for all k-mers in Text and combines them all into an array
    Then sort this array, count how many times each k-mer appears in the sorted array, and then return the k-mers that occur the maximum number of times.
    
     FrequentWordsWithMismatches(Text, k, d)
        FrequentPatterns ← an empty set
        Neighborhoods ← an empty list
        for i ← 0 to |Text| − k
            add Neighbors(Text(i, k), d) to Neighborhoods
        form an array NeighborhoodArray holding all strings in Neighborhoods
        for i ← 0 to |Neighborhoods| − 1
            Pattern ← NeighborhoodArray(i) 
            Index(i) ← PatternToNumber(Pattern)
            Count(i) ← 1
        SortedIndex ← Sort(Index)
        for i ← 0 to |Neighborhoods| − 2 
            if SortedIndex(i) = SortedIndex(i + 1)
                Count(i + 1) ← Count(i) + 1
       maxCount ← maximum value in array Count
       for i ← 0 to |Neighborhoods| − 1
           if Count(i) = maxCount
               Pattern ← NumberToPattern(SortedIndex(i), k)
               add Pattern to FrequentPatterns
       return FrequentPatterns
