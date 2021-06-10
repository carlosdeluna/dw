from dwave.system import EmbeddingComposite, DWaveSampler
import dwave.inspector


# Define the problem as two Python dictionaries:
#   h for linear terms, J for quadratic terms
#h = {}
#J = {('A','K'): -0.5,
#    ('B','C'): -0.5, 
#    ('A','C'): 0.5}
h = {0:-9.7940,1:-3.5884,2:18.2811,3:-5.8098}
J = {(0,1):-1.6681,
    (0,2): -2.5494, 
    (0,3): -0.9975,
    (1,2): 5.4732,
    (1,3): -0.3386,
    (2,3): -3.5938}

    

# Define the sampler that will be used to run the problem
sampler = EmbeddingComposite(DWaveSampler(solver={'qpu':True}))

# Run the problem on the sampler and print the results
sampleset = sampler.sample_ising(h, J,
                                 num_reads = 20,
                                 label='Example - Simple Ocean Programs: Ising')
print(sampleset)
dwave.inspector.show(sampleset)
input("Press Enter to continue...")