

def pattern_matching(pattern, genome):
    positions = []
    for i in range(len(genome)-len(pattern)+1):
        if genome[i:i+len(pattern)] == pattern:
            positions.append(i)
    return positions
