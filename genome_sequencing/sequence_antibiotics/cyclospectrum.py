

MassDictionary = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def cyclospectrum(peptide):
    mass = {0: 0}
    for i in range(len(peptide)):
        try:
            mass[i+1] = mass[i]+MassDictionary[peptide[i]]
        except Exception as e:
            print('error:', e)
    peptide_mass = mass[len(peptide)]
    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide)+1):
            spectrum.append(mass[j]-mass[i])
            if i > 0 and j < len(peptide):
                spectrum.append(peptide_mass - (mass[j]-mass[i]))
    return sorted(spectrum)