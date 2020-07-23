

from spectral_convolution import *


def peptide_spectrum(peptide, alphabet, type):
    mass = {0: 0}
    for i in range(len(peptide)):
        try:
            mass[i+1] = mass[i] + alphabet[peptide[i]]
        except Exception as e:
            print('error:', e)
    spectrum = [0]
    peptide_mass = mass[len(peptide)]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide)+1):
            spectrum.append(mass[j]-mass[i])
            if type == 'cyclo' and i > 0 and j < len(peptide):
                spectrum.append(peptide_mass - (mass[j]-mass[i]))
    return sorted(spectrum)


def score_peptide_real_spectrum(peptide, spectrum, alphabet, type):
    score = 0
    peptide_spec = peptide_spectrum(peptide, alphabet, type)
    unique = list(set(peptide_spec))
    for i in range(len(unique)):
        score += min([peptide_spec.count(unique[i]), spectrum.count(unique[i])])
    return score


def real_peptide_sequencing(spectrum, n, alphabet):
    leaderboard = {'': [0, 1]}
    leader_peptide = ['', 0, 1]
    n_leaderboard = {}
    while leaderboard:
        extract = dict(leaderboard)
        leaderboard = {}
        for k, v in extract.items():
            for key, value in alphabet.items():
                if len(k+key) <= 10:
                    peptide = k+key
                    mass = v[0]+value
                    if mass <= spectrum[-1]:
                        score = score_peptide_real_spectrum(peptide, spectrum, alphabet, 'linear')
                        leaderboard[peptide] = [mass, score]
                        if spectrum[-1]-0.3 <= mass <= spectrum[-1]:
                            cycloscore = score_peptide_real_spectrum(peptide, spectrum, alphabet, 'cyclo')
                            n_leaderboard[peptide] = [mass, cycloscore]
                            if cycloscore > leader_peptide[2]:
                                leader_peptide = [peptide, mass, cycloscore]
        try:
            trim = sorted(leaderboard.items(), key=lambda item: item[1][1])[-n][1][1]
            leaderboard = {k: v for k, v in leaderboard.items() if v[1] >= trim}
        except IndexError:
            continue
    return [leader_peptide, n_leaderboard]


def extended_alphabet_real_spectrum(spectrum):
    convolution = [round(x, 2) for x in spectral_convolution(spectrum) if 57 <= x <= 200]
    unique = list(set(convolution))
    # print(convolution)
    frequency = dict((x, convolution.count(x)) for x in unique)
    trim = sorted(frequency.items(), key=lambda item: item[1])[-30][1]
    # print(trim)
    frequency = list(set([k for k, v in frequency.items() if v >= trim]))
    alphabet = dict((str(chr(i)), frequency[i]) for i in range(len(frequency)))
    return alphabet


def real_spectrum_sequencing(n, spectrum):
    spec = sorted([spectrum[i]-1 for i in range(len(spectrum))])
    # alphabet = dict((k, v) for k, v in MassDictionary.items() if k in list('VKLPWFNY'))
    alphabet = extended_alphabet_real_spectrum(spec)
    peptides = real_peptide_sequencing(spec, n, alphabet)
    print('-'.join([str(int(alphabet[x])) for x in peptides[0][0]]), '\n')

    # m = max([v[1] for v in peptides[1].values()])
    # c = {k: v for k, v in peptides[1].items() if v[1] == m}
    # print('\n', 'score:', m, 'matches:', len(c), '\n')
    # for k in peptides[1].keys():
    #     print('-'.join([str(int(round(alphabet[x], 0))) for x in k]))
    return peptides


if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()

    MassDictionary = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

    import os
    data_dir = os.path.abspath('..\\sequence_antibiotics\\text_files')
    dataset = open(data_dir+'\\RealSpectrumSequencing\\real_spectrum.txt', 'r')
    data = [string.strip('\n') for string in dataset.readlines()]
    dataset.close()
    spectrum = sorted([float(x) for x in data[0].split()])

    output = real_spectrum_sequencing(1000, spectrum)
    print(output)

    stop = timeit.default_timer()
    print('\n', "Program Executed in", stop-start)

