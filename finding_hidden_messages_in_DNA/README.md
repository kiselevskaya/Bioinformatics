

pattern_count.py
    pattern_count(text, pattern)
        Counts how many times the given pattern appears in the text.
        The output is an integer.

    frequency_map(text, k)
        Slides through the text and counts all patterns length k.
        The output is a dictionary where keys are patterns and values are their count.

    frequent_words(text, k)
        Finds the most frequent patterns in the frequency_map dictionary.
        The output is a list of the most common patterns.


reverse_complement.py
    reverse_complement(pattern)
        Writes the complement of each nucleotide in the pattern into a string, then reversing the resulting string.
        The output is a string that is a reverse complement of the given pattern.


pattern_matching.py
    pattern_matching(pattern, genome)
        Slides through the genome and if finds a match with the pattern remembers index of started position.
        The output is a list of integers specifying all starting positions.


clump_finding.py
    clump_finding(genome, k, l, t)
        Task: Slides a window of fixed length L along the genome, looking for a region where a k-mer appears t times in short succession.
        Solution:
        Using frequency_map(text, k) function slides through the genome and counts all patterns length k.
        Remembers all patterns that appears t or more times through the genome in a list variable words.
        Using pattern_matching(pattern, genome) function for each pattern in words create list of integers specifying all starting positions of the pattern.
        Slides through the pattern matching list of indexes checks if pattern appears t times on length l.
        If gets positive result (remembers patter in variable output) or all possibilities are checked, function breaks the loop to the next pattern.
        The output is a list of k length strings, each of that appears t times on some l length part of the genome.

    clump_finding_efficient(genome, k, l, t)
        Task: Slides a window of fixed length L along the genome, looking for a region where a k-mer appears t times in short succession.
        Solution:
        Slides through the text and remember each pattern length k as key in a dictionary with a list of all starting positions as a value.
        For each key (pattern) with the length of value t or more slides through the value (matching list of indexes) checks if the pattern appears t times on length l.
        If gets positive result (remembers patter in variable patters) or all possibilities are checked, function breaks the loop to the next pattern.
        The output is a list of k length strings, each of that appears t times on some l length part of the genome.


pattern_to_number_and_back.py
    pattern_to_number(pattern)
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

    number_to_pattern(number, k)
        To go backward from a base-anything number, you divide the final number (5437  in this case) by the base, 4,  k = 7 times, keeping track of the remainder: ﻿﻿
        5437 / 4 = 1359 R 1
        1359 / 4 = 339 R 3
        339 / 4 = 84 R 3
        84 / 4 = 21 R 0
        21/4 = 5 R 1
        5/4 = 1 R 1
        1/4 = 0 R 1
        Take the remainders from the bottom up and you get: 1110331, corresponding lexicographically to ﻿CCCAGGC


computing_frequencies.py
    computing_frequencies(text, k)
        Initialises every element in the frequency array to zero (4k operations).
        Slides through the text and for each k-mer pattern that encountered, adds 1 to the value of the frequency array corresponding to pattern
        The output is a frequency array as a list.
