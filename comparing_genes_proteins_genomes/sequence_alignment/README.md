

# change_money_problem.py

**min_number_of_coins(change:int, coins:list)**
    
    Creates list of minimum number of coins for each amount of money from 0 to change.
        Change is integer number representing money that should be returned as change.
        Coins are of all possible coins nominal for a particular currency, in descending order. In this case [5, 4, 1].
        
    Output:
        - Integer represented minimal number of coins for change


# manhattan_tourist.py

**manhattan_tourist(n, m, down, right)**
    
    Tourist in Midtown Manhattan want to see as many sights as possible on their way from the corner of 59th Street and 8th Avenue to the corner of 42nd Street and 3rd Avenue.
    However, they are short on time, and at each intersection, they can only move south (↓) or east (→).
    They can choose from many different paths through the map, but no path will visit all the sights.
    The challenge of finding a legal path through the city that visits the most sights is called the Manhattan Tourist Problem.
    
    Finds the length of a longest path in a rectangular grid.
    
    ManhattanTourist(n, m, Down, Right)
        s0, 0 ← 0
        for i ← 1 to n
            si, 0 ← si-1, 0 + downi-1, 0
        for j ← 1 to m
            s0, j ← s0, j−1 + right0, j-1
        for i ← 1 to n
            for j ← 1 to m
                si, j ← max{si - 1, j + downi-1, j, si, j - 1 + righti, j-1}
        return sn, m
    
    Output:
        - integer representind the biggest weight in path from position 0,0 to n,m
        

# longest_common_subsequence_backtrack.py

**longest_common_subsequence_backtrack(v, w)**

    Assigns a weight of 1 to the edges in DAG (DirectedAlignmentGraph(v, w)) corresponding to matches and assign a weight of 0 to all other edges, then s|v|, |w| gives the length of an LCS.
    Algorithm maintains a record of which edge was used to compute each value si, j by utilizing backtracking pointers, which take one of the three values ↓ , →, or ↘. Backtracking pointers are stored in a matrix Backtrack.

    LCSBackTrack(v, w)
        for i ← 0 to |v|
            si, 0 ← 0
        for j ← 0 to |w| 
            s0, j ← 0
        for i ← 1 to |v|
            for j ← 1 to |w|
                match ← 0
                if vi-1 = wj-1
                    match ← 1
                si, j ← max{si-1, j , si,j-1 , si-1, j-1 + match }
                if si,j = si-1,j
                    Backtracki, j ← "↓"
                else if si, j = si, j-1
                    Backtracki, j ← "→"
                else if si, j = si-1, j-1 + match
                    Backtracki, j ← "↘"
        return Backtrack
    
    Output:
        - matrix of backtracking pointers, which take one of the three values ↓ , →, or ↘
        
        
**output_lcs(backtrack, v, i, j)**

    A string is a subsequence of a string v if it can be obtained by deleting some symbols from v. 
    For example, GC and GAT are both subsequences of GACT. 
    A string x is a common subsequence of strings v and w if it is a subsequence of both v and w.
    For example, G and AT are both common subsequences of GACT and ATG.
    The goal is to find a longest common subsequence (LCS) of two strings.
    Two strings may have more than one longest common subsequence.

    OutputLCS(backtrack, v, i, j)
        if i = 0 or j = 0
            return ""
        if backtracki, j = "↓"
            ﻿return OutputLCS(backtrack, v, i - 1, j)
        else if backtracki, j = "→"
            return OutputLCS(backtrack, v, i, j - 1)
        else
            return OutputLCS(backtrack, v, i - 1, j - 1) + vi
                    
    Output:
        - longest common subsequence of two strings
