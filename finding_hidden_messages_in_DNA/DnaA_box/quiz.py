

from neighbors import *
from hamming_distance import *
from skew_array import *


print(len(set(neighbors('ACGT', 3))))

print(approximate_pattern_count('CATGCCATTCGCATTGTCCCAGTGA', 'CCC', 2))

print(hamming_distance('CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA', 'CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG'))

print(skew_array('CATTCCAGTACTTCATGATGGCGTGAAGA'))
