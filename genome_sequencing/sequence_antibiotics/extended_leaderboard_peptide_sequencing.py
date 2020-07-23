

def extended_spectrum(peptide, alphabet, type):
    mass = {0: 0}
    for i in range(len(peptide)):
        try:
            mass[i+1] = mass[i] + alphabet[peptide[i]]
        except Exception as e:
            print('error:', e)
    spectrum = [0]
    if type == 'cyclo':
        peptide_mass = mass[len(peptide)]
        for i in range(len(peptide)):
            for j in range(i+1, len(peptide)+1):
                spectrum.append(mass[j]-mass[i])
                if i > 0 and j < len(peptide):
                    spectrum.append(peptide_mass - (mass[j]-mass[i]))
    else:
        for i in range(len(peptide)):
            for j in range(i+1, len(peptide)+1):
                spectrum.append(mass[j]-mass[i])
    return sorted(spectrum)


def extended_score_peptide(peptide, spectrum, alphabet, type):
    score = 0
    peptide_spectrum = extended_spectrum(peptide, alphabet, type)
    unique = list(set(peptide_spectrum))
    for i in range(len(unique)):
        score += min([peptide_spectrum.count(unique[i]), spectrum.count(unique[i])])
    return score


def extended_leaderboard_peptide_sequencing(spectrum, n, alphabet):
    leaderboard = {'': [0, 1]}
    leader_peptide = ['', 0, 1]
    n_leaderboard = {}
    while leaderboard:
        extract = dict(leaderboard)
        leaderboard = {}
        for k, v in extract.items():
            for key, value in alphabet.items():
                peptide = k+key
                mass = v[0]+value
                if mass <= spectrum[-1]:
                    score = extended_score_peptide(peptide, spectrum, alphabet, 'linear')
                    leaderboard[peptide] = [mass, score]
                    if mass == spectrum[-1]:
                        cycloscore = extended_score_peptide(peptide, spectrum, alphabet, 'cyclo')
                        n_leaderboard[peptide] = [mass, cycloscore]
                        if cycloscore > leader_peptide[2]:
                            leader_peptide = [peptide, mass, cycloscore]
        try:
            trim = sorted(leaderboard.items(), key=lambda item: item[1][1])[-n][1][1]
            leaderboard = {k: v for k, v in leaderboard.items() if v[1] >= trim}
        except IndexError:
            continue
    return [leader_peptide, n_leaderboard]


if __name__ == '__main__':
    import timeit
    import os
    start = timeit.default_timer()
    data_dir = os.path.abspath('..\\sequence_antibiotics\\text_files')
    dataset = open(data_dir+'\\LeaderboardCyclopeptideSequencing\\dataset_103_2.txt', 'r')
    data = [string.strip('\n') for string in dataset.readlines()]
    dataset.close()
    spectrum = [int(x) for x in data[1].split()]
    n = int(data[0])
    extended_alphabet = dict((str(chr(i)), i) for i in range(57, 201))

    a = extended_leaderboard_peptide_sequencing(spectrum, n, extended_alphabet)
    m = max([v[1] for v in a[1].values()])
    c = {k: v for k, v in a[1].items() if v[1] == m}
    print('\n', 'score:', m, 'matches:', len(c), '\n')
    for k in c.keys():
        print('-'.join([str(extended_alphabet[x]) for x in k]))

    print('\n', 'LeaderPeptide:', '-'.join([str(extended_alphabet[x]) for x in a[0][0]]))

    stop = timeit.default_timer()
    print('\n', "Program Executed in", stop-start)
