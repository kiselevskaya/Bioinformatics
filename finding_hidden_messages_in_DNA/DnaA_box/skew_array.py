

def skew_array(genome):
    skew = {}
    n = len(genome)
    extended_genome = genome + genome[0:n//2]
    skew[0] = 0
    for i in range(1, n+1):
        skew[i] = skew[i-1]
        if extended_genome[i-1] == "G":
            skew[i] = skew[i-1]+1
        if extended_genome[i-1] == "C":
            skew[i] = skew[i-1]-1
    return list(skew.values())


def minimum_skew(genome):
    positions = []
    skew = skew_array(genome)
    lowest = min(skew)
    for i in range(len(skew)):
        if skew[i] == lowest:
            positions.append(i)
    return positions
