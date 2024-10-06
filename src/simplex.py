import numpy as np

class Simplex:

    def __init__(self, G, h, u) -> None:
        self.Tableau = np.zeros(G.shape[0]+1, G.shape[1]+1)
        self.c, self.d = G.shape

        for i, row in G:
            for j, elem in row:
                self.Tableau[i][j] = elem
            self.Tableau[i][-1] = h[i]

        for i in range(self.d):
            self.Tableau[-1][i] = u[i]

        print("Initial Tableau:")
        print(self.Tableau)
        
