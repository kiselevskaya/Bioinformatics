

# randomized_motif_search.py

Calls randomized_motif_search(dna, k, t) N times, storing the best-scoring set of motifs resulting from this algorithm in a variable called best_motifs.
The code stops running as soon as the score of the motifs that we generate stops improving.
It can be dangerous to use such a loop, since it could lead to an infinite loop in which a program never terminates.
However, in this particular case, the motif score must eventually stop improving, so that function must eventually terminate.


**motifs(dna, profile)**

    Takes a profile matrix corresponding to a list of strings DNA as input and returns a list of the profile-most probable k-mers in each string from DNA.
    Output:
        - list of t strings (motifs corresponding to profile matrix)
    
**random_motifs(dna, k, t)**

    Uses random integer in range [0 to (length DNA string - k)] to choose a random k-mer from each of t different strings DNA.
    Output:
        - list of t strings (random motifs)

**randomized_motif_search(dna, k, t)**
    
    Begins from a collection of randomly chosen k-mers Motifs in Dna,
     construct Profile(Motifs), and use this profile to generate a new collection of k-mers: 
     **Motifs(Profile(Motifs), Dna)** hoping that is has better score than the original collection of k-mers Motifs.
    Then form the profile matrix of these k-mers, **Profile(Motifs(Profile(Motifs), Dna))**
    Continue to iterate... **...Profile(Motifs(Profile(Motifs(Profile(Motifs), Dna)), Dna))...** as long as the score of the constructed motifs keeps improving

    Output:
        - list of strings (motifs)
        
**loop(n, dna, k, t)**

    Calls randomized_motif_search(dna, k, t) N times, storing the best-scoring set of motifs resulting from this algorithm in a variable called best_motifs.
    The code stops running as soon as the score of the motifs that we generate stops improving.
    It can be dangerous to use such a loop, since it could lead to an infinite loop in which a program never terminates.
    However, in this particular case, the motif score must eventually stop improving, so that function must eventually terminate.
    
    Output:
        - list of strings (motifs with approximate best score)
