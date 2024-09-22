import numpy as np

class Tableau:

    def __init__(self, G, h, u):

        # This is building the tableau
        self.c, self.d = G.shape
        self.Tableau = np.zeros(((G.shape[0] + 1), G.shape[1]+1+self.c))
        self.currentBasis = list(range(self.c,2*self.c))
        self.d += self.c
        for i, x in enumerate(G):
            for j, y in enumerate(x):
                self.Tableau[i][j] = y
        for i in range(len(h)):
            self.Tableau[i][-1] = h[i]
        for j in range(len(u)):
            self.Tableau[-1][j] = u[j]

        for i in range(self.c):
            self.Tableau[i][i+self.c] = 1
        print("Initial Tableau is the following:")
        print(self.Tableau)
        print(f"Initial Basis is: {self.currentBasis}")

    def ChangeBasis(self, l, e):
        ind = self.currentBasis.index(l)
        self.Tableau[ind] = self.Tableau[ind]/self.Tableau[ind][e]
        for i in range(self.c):
            if i != ind:
                self.Tableau[i] = self.Tableau[i] - self.Tableau[ind]*self.Tableau[i][e]
        self.currentBasis[ind] = e
        print(self.Tableau.__str__())

    def PickVariables(self):
        un, ub = [], []
        map_n = {}
        map_b = {}
        N = []
        
        n, b = 0, 0
        for i in range(self.d):
            if i not in self.currentBasis:
                un.append(self.Tableau[-1][i])
                map_n[n] = i
                n+=1
            else:
                ub.append(self.Tableau[-1][i])
                map_b[b] = i
                b+=1
        
        for j in range(self.d):
            if j not in self.currentBasis:
                #Stacking a column
                col = []
                for i in range(self.c):
                    col.append(self.Tableau[i][j])
                N.append(col)
        N = np.array(N)
        un = np.array(un)
        ub = np.array(ub)
        print(N.__str__())

        val = un - N.dot(ub)

        if (np.all(val >= 0)):
            print("Optimal reached!!")
        else:
            leaving_var = np.argmin(val)
            print(val)
            print(f"Entering variable is {map_n[leaving_var]}")

def __main__():
    np.set_printoptions(linewidth=150)

    G = np.array([
        [2,3,4],
        [3,4,5],
        [10,11,13],
    ])

    h = np.array([1,2,3])
    u = np.array([5,6,7])

    T = Tableau(G,h,u)
    T.ChangeBasis(3,0)
    T.ChangeBasis(4,1)
    T.ChangeBasis(5,2)
    T.PickVariables()


if __name__ == "__main__":
    __main__()

