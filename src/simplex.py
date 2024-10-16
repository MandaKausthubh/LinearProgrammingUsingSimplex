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

    def EnteringVar(self):
        index = np.argmin(self.Tableau[-1])
        if (self.Tableau[-1][index] > 0):
            print("Optimal Found")
            return -1
        else:
            return index

    def LeavingVar(self, entering):
        # Searching for Unbounded condition:
        index_col = -1
        for i in range(self.c):
            if self.Tableau[self.basis[i]][entering] > 0:
                index_col = i
        if index_col == -1:
            print("UNBOUNDED")
            return -1
        for i in range(self.c):
            if self.Tableau[self.basis[i]][entering] > 0:
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

    def LinearOptimize(self):
        pass
