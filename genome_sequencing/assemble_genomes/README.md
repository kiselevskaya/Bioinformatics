

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
