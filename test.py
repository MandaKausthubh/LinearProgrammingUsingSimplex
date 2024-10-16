from src.simplex import *

G = np.array([
    [1,7,8,1,0,0,],
    [2,1,0,0,1,0,],
    [3,5,1,0,0,1,],
])

h = [1,2,3]
u = [-6,-13,-9,0,0,0]
basis = [3,4,5]

np.set_printoptions(linewidth=100,precision=3)

S = Simplex(G, h, u, basis=np.array(basis), initialSum=-6, isFirst=True)
print("Current Entering Var: ", S.EnteringVar())
print("Current Leaving Var: ", S.LeavingVar(S.EnteringVar()))
S.BasisChange(3, 1)
print("Current Entering Var: ", S.EnteringVar())
print("Current Leaving Var: ", S.LeavingVar(S.EnteringVar()))
S.BasisChange(5, 0)
print("Current Entering Var: ", S.EnteringVar())
print("Current Leaving Var: ", S.LeavingVar(S.EnteringVar()))
S.BasisChange(4, 2)
print("Current Entering Var: ", S.EnteringVar())


Mat = np.array([
    [1,7,8],
    [2,1,0],
    [3,5,1],
])
U_new = [3,4,5]
H_Mat = [1,2,3]

S_new = Simplex(Mat,H_Mat,H_Mat)
