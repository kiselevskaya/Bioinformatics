

# change_money_problem.py

**min_number_of_coins(change:int, coins:list)**
    
    Creates list of minimum number of coins for each amount of money from 0 to change.
        Change is integer number representing money that should be returned as change.
        Coins are of all possible coins nominal for a particular currency, in descending order. In this case [5, 4, 1].
        
    Output:
        - Integer represented minimal number of coins for change


# manhattan_tourist.py

**manhattan_tourist(n, m, down, right)**
    
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
