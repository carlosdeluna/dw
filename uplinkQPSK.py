from collections import defaultdict
from dwave.system import EmbeddingComposite, DWaveSampler
import dwave.inspector
import pdb
import scipy.io


# Define the problem as two Python dictionaries:
#   h for linear terms, J for quadratic terms
A=[[        0,   -2.2548,    0.5563,    0.1623,   -0.0000,   -2.0171,    0.8219,   -0.4384],
[         0,         0,    0.4556,   -2.5310,    2.0171,    0.0000,    0.5133,    2.4097],
[         0,         0,         0,   -0.8106,   -0.8219,   -0.5133,   -0.0000,    1.3508],
[         0,         0,         0,         0,    0.4384,   -2.4097,   -1.3508,    0.0000],
[         0,         0,         0,         0,         0,   -2.2548,    0.5563,    0.1623],
[         0,         0,         0,         0,         0,         0,    0.4556,   -2.5310],
[         0,         0,         0,         0,         0,         0,         0,   -0.8106],
[         0,         0,         0,         0,         0,         0,         0,         0]]
print(A)

B=[[   9.2944,   14.7516,   11.1967,    8.9874,    7.0880,    2.6874,    7.0396,    2.6443,    4.3041,   14.2505,  -12.1294,    5.7417,  -14.5928,   11.4992,   11.0956,    5.2850],
[    0.8802,  -13.5257,   -1.0194,   -2.8761,   -3.7379,    4.0113,    3.5030,    1.8777,   -0.8992,  -10.6252,    9.7708,    2.5132,    8.1542,   -2.1646,    2.0191,    0.4271],
[   -1.2717,    1.4314,    5.6615,    5.2730,    3.8998,    3.6633,   -2.3616,   -2.3771,   -5.2516,   -4.3171,    1.0850,    3.2520,    0.9245,    5.2226,    4.7397,    5.3301],
[   -4.8089,    4.7555,    5.5055,   -7.7151,    6.6200,    1.9467,   -7.0774,    4.6623,    1.9838,    8.8324,    5.2583,    1.3528,  -11.8809,   -8.8321,   -8.9170,   -0.8427],
[    9.3588,  -14.7562,   -7.0840,  -18.2536,    4.5724,    9.6681,   13.7682,    8.8908,    8.3552,   -6.9323,   13.7000,    7.8488,    6.2498,  -14.4652,    5.9074,   -8.7126],
[   -1.1781,    3.8039,   -9.5508,    4.4586,   -5.1919,   -5.9037,   -0.1888,   -4.2520,    1.6493,   -4.0608,   -8.4620,   -5.6490,    9.1260,    3.7606,    0.4431,   -1.5717],
[    4.5762,    2.0647,    0.1237,   -2.0611,   -3.6500,    1.5948,    7.4329,   -3.2679,   -1.3794,    0.9393,   -4.4207,   -2.1866,    0.6952,    3.5641,    5.3855,   -3.6594],
[   -2.0662,  -12.8543,    8.5363,    2.5323,    3.3830,    6.4302,   -4.7698,    3.6698,   -6.0198,   -6.5680,   11.8648,    6.0604,   -4.4536,    1.1462,    0.8463,    8.1838]]
#print(B)   

h = defaultdict(float)
J = defaultdict(float)
d = 8
blk = 16
for bb in range(blk):
  for r in range(d):
    for c in range(d):
      J[(bb*d+r,bb*d+c)] = A[r][c]

vec = 16
for vv in range(vec):
  for r in range(d):
    h[vv*d+r] = B[r][vv]

    

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler(solver={'qpu':True}))

# Run the problem on the sampler and print the results
sampleset = sampler.sample_ising(h, J,
                                 num_reads = 20,
                                 label='Example - Simple Ocean Programs: Ising')
print(type(sampleset))
print(sampleset)

dwave.inspector.show(sampleset)
pdb.set_trace()
input("Press Enter to continue...")