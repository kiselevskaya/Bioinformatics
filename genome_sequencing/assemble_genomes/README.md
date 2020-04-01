

# composition.py

**composition(text, k)**
    
    Function generates the k-mer composition of a string
        Compositionk(Text) is the collection of all k-mer substrings of Text (including repeated k-mers).
        Eg. Composition3(TATGGGGTGC) = {ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG}
        k-mers in lexicographic order because the correct ordering of the reads (shorter DNA fragments called reads) is unknown when they are generated.
      
    Output:
        - list of k-mers in lexicographic order


**path_to_genome(path)**
    
    Reconstructs a string from its genome path.
    Given a sequence path of k-mers where each next k-mer overlaps previous but the last nucleotide. 
    
    Output:
        - string represented reconstructed genome
        

**overlap(pattern)**

    Finds overlaps in patterns.
    Terms prefix and suffix refer to the first k − 1 nucleotides and last k − 1 nucleotides of a k-mer, respectively.
        eg. Suffix(TAA) = Prefix(AAT) = AA
    
    Output:
        - dictionary (network of nodes connected by edges)
