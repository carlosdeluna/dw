import pickle
import pdb
from dwave.system import EmbeddingComposite, DWaveSampler
import dwave.inspector
import scipy.io

mat = scipy.io.loadmat('inVars.mat')

#FM = mat["FM"]
#print(FM)
#scipy.io.savemat('outVars.mat', mdict={'FM': FM})


mat = scipy.io.loadmat('inVars.mat')
ag=len(mat['Gt'])
bg=len(mat['Gt'][0])
cg=len(mat['Gt'][0][0])
dg=len(mat['Gt'][0][0][0])

G = [ [0]*bg for i in range(ag)]
for aa in range(ag):
    for bb in range(bg):
        G[aa][bb] = mat['Gt'][aa][bb][0][0]

af=len(mat['Ft'])
bf=len(mat['Ft'][0])
cf=len(mat['Ft'][0][0])
df=len(mat['Ft'][0][0][0])

F = [ [0]*bf for i in range(af)]
for aa in range(af):
    for bb in range(bf):
        F[aa][bb] = mat['Ft'][aa][bb][0][0]

pdb.set_trace()



with open('sampleset16.pkl', 'rb') as file:
    result = pickle.load(file)
  
    print(result)
input("Press Enter to continue...")
