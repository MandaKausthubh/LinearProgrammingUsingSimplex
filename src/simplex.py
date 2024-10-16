import numpy as np

class Simplex:

    def __init__(self, ConstMatrix, ConstVec, Weights, basis = np.array([]), initialSum = 0, isFirst = False):

        self.c , self.d = ConstMatrix.shape
        self.basis = np.zeros(self.c)
        self.Tableau = np.zeros((self.c+1, self.d+1))

        # Standard Usage
        if not isFirst:
            #We need to generate the initial matrix first
            c,d = self.c, self.d
            NewMatr = np.zeros((c,c+d))
            #Copying the Matrix
            for i in range(c):
                for j in range(d):
                    NewMatr[i][j] = ConstMatrix[i][j]
            for i in range(c):
                NewMatr[i][i+d] = 1

            # Calculating the augmented weights
            AugW = np.zeros(d+c)
            for i in range(c):
                for j in range(d):
                    AugW[j] -= NewMatr[i][j]
            AugSum = 0
            for i in range(c):
                AugSum -= ConstVec[i]

            InitialBFS = Simplex(NewMatr, ConstVec, AugW, basis = np.array(range(d,d+c)), initialSum = AugSum, isFirst=True)
            InitialBFS.LinearOptimize()
            print("Final Matrix:")
            print(InitialBFS.Tableau)
            print(InitialBFS.basis)


        # For initial BFS
        else:
            for i in range(self.c):
                for j in range(self.d):
                    self.Tableau[i][j] = ConstMatrix[i][j]
            for j in range(self.d):
                self.Tableau[-1][j] = Weights[j]
            for i in range(self.c):
                self.Tableau[i][-1] = ConstVec[i]
            self.Tableau[-1][-1] = initialSum 
            self.basis = basis
            print("Initial Tableau:")
            print(self.Tableau)
            print(self.basis)

    def EnteringVar(self):
        index = -1
        for i in range(self.d):
            if i not in self.basis and self.Tableau[-1][i] <= 0:
                if index == -1:
                    index = i
                index = i if self.Tableau[-1][index] > self.Tableau[-1][i] else index
        return index

    def LeavingVar(self, entering):
        # Searching for Unbounded condition:
        index_col = -1
        for i in range(self.c):
            if self.Tableau[i][entering] > 0:
                index_col = i
        if index_col == -1:
            print("UNBOUNDED")
            return -1
        for i in range(self.c):
            if self.Tableau[i][entering] > 0:
                index_col = index_col if (
                        self.Tableau[index_col][-1]/self.Tableau[index_col][entering] <= self.Tableau[i][-1]/self.Tableau[i][entering]
                        ) else i
        return self.basis[index_col]

    def BasisChange(self, leaving, entering):
        if leaving not in self.basis:
            print("This is not a valid leaving variable!!")
            return -1
        if entering in self.basis:
            print("This is not a valid entering variable!!")
            return -1

        row = np.where(self.basis == leaving)[0][0]
        self.Tableau[row] /= self.Tableau[row][entering]
        for i,r in enumerate(self.Tableau):
            if i != row:
                r -= self.Tableau[row] * r[entering]
        self.basis[row] = entering 
        print("Basis after the Swap:")
        print(self.Tableau)
        print(self.basis)

    def LinearOptimize(self):
        entering = self.EnteringVar()
        if entering == -1:
            print("OPTIMUM ACHIEVED")
            return -1
        leaving = self.LeavingVar(entering)
        if leaving == -1:
            print("UNBOUNDED")
            return -1
        print("Leaving Var:", leaving)
        print("Entering Var:", entering)
        self.BasisChange(leaving, entering)
        self.LinearOptimize()
        pass
