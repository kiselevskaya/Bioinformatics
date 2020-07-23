

def spectral_convolution(spectrum):
    spectr = sorted(spectrum)
    lst = []
    for i in range(len(spectr)):
        for j in range(len(spectr)):
            lst.append(spectr[i]-spectr[j])
    lst = [x for x in lst if x > 0]
    return lst


if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()

    import os
    data_dir = os.path.abspath('..\\sequence_antibiotics\\text_files')
    dataset = open(data_dir+'\\Convolution\\dataset_104_4.txt', 'r')
    data = [string.strip('\n') for string in dataset.readlines()]
    dataset.close()
    spectrum = [int(x) for x in data[0].split()]

    a = spectral_convolution(spectrum)
    print(' '.join([str(x) for x in a]))

    stop = timeit.default_timer()
    print('\n', "Program Executed in", stop-start)
