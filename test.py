from src.simplex import *
#
# G = np.array([
#     [1,7,8,1,0,0,],
#     [2,1,0,0,1,0,],
#     [3,5,1,0,0,1,],
# ])
#
# h = [1,2,3]
# u = [-6,-13,-9,0,0,0]
# basis = [3,4,5]
#
np.set_printoptions(linewidth=100,precision=3)
#
# S = Simplex(G, h, u, basis=np.array(basis), initialSum=-6, isFirst=True)
# print("Current Entering Var: ", S.EnteringVar())
# print("Current Leaving Var: ", S.LeavingVar(S.EnteringVar()))
# S.BasisChange(3, 1)
# print("Current Entering Var: ", S.EnteringVar())
# print("Current Leaving Var: ", S.LeavingVar(S.EnteringVar()))
# S.BasisChange(5, 0)
# print("Current Entering Var: ", S.EnteringVar())
# print("Current Leaving Var: ", S.LeavingVar(S.EnteringVar()))
# S.BasisChange(4, 2)
# print("Current Entering Var: ", S.EnteringVar())
#

Mat = np.array([
    [1,7,8, 13, 1, 0, 0],
    [2,1,17,11, 0, 1, 0],
    [3,5,1, 7, 0, 0, 1],
])
U_new = [-6,-13,-26,-31,0,0,0]
H_Mat = [1,2,3]
basis = [4,5,6]
S = Simplex(Mat, H_Mat, U_new, basis=np.array(basis) ,initialSum=-6, isFirst=True)

# print(S.EnteringVar())
# print(S.LeavingVar(S.EnteringVar()))
# S.BasisChange(4, 3)
# print(S.EnteringVar())
# print(S.LeavingVar(S.EnteringVar()))
# S.BasisChange(6, 0)
# S.BasisChange(5, 2)
# S_new = Simplex(ConstMatrix = Mat, ConstVec = H_Mat, Weights=U_new)
# S_new.BasisChange(4, 1)
S.LinearOptimize()


Mat = np.array([
    [1, -5, 1, 0],
    [1, -0.55, 0, 1],
])
U_new = [2,3,0,0]
H_Mat = [1,1]

S = Simplex(Mat, H_Mat, U_new)
S.LinearOptimize()
