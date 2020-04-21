

Alphabet = {57: 'G', 71: 'A', 87: 'S', 97: 'P', 99: 'V', 101: 'T', 103: 'C', 113: 'I/L', 114: 'N', 115: 'D', 128: 'K/Q', 129: 'E', 131: 'M', 137: 'H', 147: 'F', 156: 'R', 163: 'Y', 186: 'W'}


def counting_mass(mass, masslist):
    if mass == 0:
        return 1, masslist
    if mass < 57:
        return 0, masslist
    if mass in masslist:
        return masslist[mass], masslist
    n = 0
    for i in Alphabet:
        k, masslist = counting_mass(mass - i, masslist)
        n += k
    masslist[mass] = n
    return n, masslist
