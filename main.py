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


        # Calculating the entering variable

        entering_var = -1
        leaving_var = -1
        x = -1
        if (np.all(val >= 0)):
            print("Optimal reached!!")
            return (0,-1,-1)
        else:
            x = np.argmin(val)
            print(val)
            entering_var = map_n[x]
            print(f"Entering variable is {entering_var}")

        # Calculating the leaving variable 
        if (np.all([N[x][i] < 0 for i in range(self.c)])):
            print("UNBOUNDED!!")
            return (-1,-1,-1)
        else:
            rat_leaving = []
            for i in range(self.c):
                if(N[x][i] > 0):
                    rat_leaving.append(self.Tableau[-1][i]/N[x][i])
                else:
                    rat_leaving.append(np.Infinity)
            leaving_var = map_b[np.argmin(rat_leaving)]
            print(f"Leaving variable is {leaving_var}")
            return (1,entering_var, leaving_var)
    
    def FindOptimum(self):
        status, entering_var, leaving_var = self.PickVariables()
        if (status == 0):
            print(f"Optimum reached")
            # Print the variables with the values
            vars = []
            for i in range(self.d):
                if i in self.currentBasis:
                    # NOTE: fill this out
                    vars.append(self.Tableau[self.currentBasis.index(i)][-1])
                    pass
                else:
                    vars.append(0)
            print("The variable values are:", vars)
            print(f"The optimal value is: {np.array(vars).dot(self.Tableau[-1][:-1])}")
        if (status == -1):
            print("UNBOUNDED!!")
        if (status == 1):
            self.ChangeBasis(leaving_var, entering_var)
            self.FindOptimum()
        pass

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
    T.FindOptimum()

if __name__ == "__main__":
    __main__()

