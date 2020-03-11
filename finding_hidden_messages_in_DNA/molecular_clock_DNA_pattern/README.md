

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


# gibbs_sampler.py

**normalize(probabilities)**

    To rescale a collection of probabilities so that these probabilities sum to 1.
    This function takes a dictionary <probabilities> whose keys are k-mers and whose values are the probabilities of these k-mers (which do not necessarily sum to 1).
    The function should divide each value in <probabilities> by the sum of all values in  <probabilities>, then return the resulting dictionary.
    
    Output:
        - dictionary of k-mers probabilities
    
**weighted_die(probabilities)**

    To simulate rolling a die so that "ccgG" has probability 4/80, "cgGC" has probability 8/80, and so on.
    Function is generating a random number p between 0 and 1. If p is between 0 and 4/80, then it corresponds to "ccgG". If p is between 4/80 and 4/80 + 8/80, then it corresponds to "cgGC", etc.
    This function takes a dictionary <probabilities> whose keys are k-mers and whose values are the <probabilities> of these k-mers.
    
    Output:
        - string (randomly chosen k-mer key with respect to the values in <probabilities>)

**profile_generated_string(text, profile, k)**

    Range over all possible k-mers in Text, computing the probability of each one and placing this probability into a dictionary.
    Normalize these probabilities using the normalize(probabilities) function, and then return the result of rolling a weighted die over this dictionary to produce a k-mer.
    
    Output:
        - string (k-mer)
    
**gibbs_sampler(dna, k, t, N)**

    GibbsSampler(Dna, k, t, N)
        randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
        BestMotifs ← Motifs
        for j ← 1 to N
            i ← Random(t)
            Profile ← profile matrix constructed from all strings in Motifs except for Motifi
            Motifi ← Profile-randomly generated k-mer in the i-th sequence
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        return BestMotifs
    
    Output:
        - list of strings (motifs with approximate best score)
