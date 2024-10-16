from src.simplex import *

G = np.array([
    [1,7,8,1,0,0,],
    [2,1,0,0,1,0,],
    [3,5,1,0,0,1,],
])

h = [1,2,3]
u = [0,0,0,1,1,1]
basis = [3,4,5]

np.set_printoptions(linewidth=100,precision=3)
S = Simplex(G=G, u=u, h=h, basis=np.array(basis))
# S.PickingEnteringVar()
# S.SwappingLeavingEnteringVar(leaving=0,entering=3)
# entering = S.PickingEnteringVar()
# leaving = S.PickLeavingVar(entering)
S.Optimize()
print("Final Basis: ", S.basis)
