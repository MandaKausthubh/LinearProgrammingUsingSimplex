import numpy as np
import pandas as pd


def 


class Tabluea:

    def __init__(self, G_Matrix, h_bar, Cost_vector, c, d) -> None:
        self.G = G_Matrix
        self.h = h_bar
        self.cost = Cost_vector
        self.Basis = []
        self.c,self.d = c, d
        pass

    def FindIntialBFS(self):
        pass

    def ReducetoBFS(self, Basis):
        E = np.identity(self.c)
        B_1 = []
        
        for i in range(self.c):
            j = -1
            for k in Basis:
                if self.G[i][k] != 0:
                    j = k
                    break
            if ( j != -1 ):
                B_1.append(j)
                Basis.remove(j)
            else:
                # Find another element
                for k in range(0,self.d):
                    if self.G[i][k] != 0:
                        j = k
                        B_1.append(j)
                        break
                pass
            
            E[j] = E[j]/self.G[i][j]
            for r in range(0,self.c):
                E[r] = E[r] - self.G[r][i] * E[j]
        # Process B_1 U B_2
        return (E,B_1)

    def ChangingBasis(self, entering_index, leaving_var):
        pass
