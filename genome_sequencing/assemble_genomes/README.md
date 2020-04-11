

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


**de_bruijnk(text, k)**

    Given a genome Text, PathGraphk(Text) is the path consisting of |Text| - k + 1 edges, where the i-th edge of this path is labeled by the i-th k-mer in Text and the i-th node of the path is labeled by the i-th (k - 1)-mer in Text.
    The de Bruijn graph DeBruijnk(Text) is formed by gluing identically labeled nodes in PathGraphk(Text).
    
    Output:
        - dictionary where keys are prefixes (the first nodes of the edge) and values are suffixes (the second nodes edge)


**de_bruijnk_graph(patterns)**

    Create the De Bruijnk graph from list of k-mers.
    Output:
        - dictionary where keys are prefixes (the first nodes of the edge) and values are suffixes (the second nodes edge)


**eulerian_cycle(graph)**
    
    EulerianCycle(Graph)
        form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
        while there are unexplored edges in Graph
            select a node newStart in Cycle with still unexplored edges
            form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking 
            Cycle ← Cycle’
        return Cycle
        
    http://www.graph-magics.com/articles/euler.php
    
    Output:
        - euler cycle as a list
    
    
**eulerian_path(graph)**    


    Eulerian cycles can begin from any arbitrary node in the graph,
     if the graph has an Eulerian cycle in it.
    However, Eulerian paths, if it exists in the graph, are limited to start from a special node, v,
     in the graph, having outdegree one greater than its indegree (out(v) - in(v) = 1),
      and limited to end at another special node, w,
       in the graph, having out-degree one smaller than its in-degree (in(w) - out(w) = 1).
    
    Output:
        - euler path as a list
        

**string_reconstruction(patterns)**  

    StringReconstruction(Patterns)
        dB ← DeBruijn(Patterns)
        path ← EulerianPath(dB)
        Text﻿ ← PathToGenome(path)
        return Text
        
    Output:
        - string of genome
        
        
**k_universal_circular_string(k)**

    Generate all (2^k) possible combinations of 0 and 1 of length k.
    Creates graph of patterns and eulerian cycle for this graph.
    Using this cycle creates a string.
    As string constructed from cycle the suffix len(k-1) is the prefix len(k-1).
    To make the final string circular and universal (include each pattern only ones) cuts prefix.
    
    Output:
        - binary string of length 2^k
    
    
**k_d_mer_composition(text, k, d)**

    Generates the (k,d)-mer composition (composition of all k-mer pairs with d nucleotides in between) of text in lexicographic order.
    Output:
        - dictionary, where key is first k-mer and value is list of all second k-mers if there are several


**paired_string_reconstruction(pairs, k, d)**

    Creates deBruijn graph from read pairs (similar to k-mers graph function except nodes are the concatenation of 2 nodes)
    Creates an eulerian path from that graph
    Reconstruct the string from the nodes.
    
    StringSpelledByGappedPatterns(GappedPatterns, k, d)
        FirstPatterns ← the sequence of initial k-mers from GappedPatterns
        SecondPatterns ← the sequence of terminal k-mers from GappedPatterns
        PrefixString ← StringSpelledByGappedPatterns(FirstPatterns, k)
        SuffixString ← StringSpelledByGappedPatterns(SecondPatterns, k)
        for i = k + d + 1 to |PrefixString|
            if the i-th symbol in PrefixString does not equal the (i - k - d)-th symbol in SuffixString
                return "there is no string spelled by the gapped patterns"
        return PrefixString concatenated with the last k + d symbols of SuffixString
    
    Output:
        - string


**maximal_non_branching_paths(patterns)**

    MaximalNonBranchingPaths(Graph)
        Paths ← empty list
        for each node v in Graph
            if v is not a 1-in-1-out node
                if out(v) > 0
                    for each outgoing edge (v, w) from v
                        NonBranchingPath ← the path consisting of single edge (v, w)
                        while w is a 1-in-1-out node
                            extend NonBranchingPath by the edge (w, u) 
                            w ← u
                        add NonBranchingPath to the set Paths
        for each isolated cycle Cycle in Graph
            add Cycle to Paths
        return Paths
        
    Output:
        - list of contigs (long, contiguous segments of the genome, non branching)
