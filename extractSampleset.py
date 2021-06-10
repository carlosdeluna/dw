import pickle
from dwave.system import EmbeddingComposite, DWaveSampler
import dwave.inspector

with open('sampleset16.pkl', 'rb') as file:
    res = pickle.load(file)
  
    print(res)
input("Press Enter to continue...")
