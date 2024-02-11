from __future__ import print_function
from __future__ import division
import numpy as np


class ART:
    def __init__(self, n=5, m=10, rho=.5):
        self.F1 = np.ones(n)  # Comparison layer
        self.F2 = np.ones(m)  # Recognition layer
        self.Wf = np.random.random((m, n))  # Feed-forward weights
        self.Wb = np.random.random((n, m))  # Feed-back weights
        self.rho = rho  # Vigilance 0<p<1
        self.active = 0  # Number of active units in F2

    def learn(self, X):
        # Compute F2 output and sort them (I)
        self.F2[...] = np.dot(self.Wf, X)
        I = np.argsort(self.F2[:self.active].ravel())[::-1]

        for i in I:
            # Check if nearest memory is above the vigilance level
            d = (self.Wb[:, i] * X).sum() / X.sum()
            if d >= self.rho:
                # Learn data
                self.Wb[:, i] *= X
                self.Wf[i, :] = self.Wb[:, i] / (0.5 + self.Wb[:, i].sum())
                return self.Wb[:, i], i

        # No match found, increase the number of active units
        # and make the newly active unit to learn data
        if self.active < self.F2.size:
            i = self.active
            self.Wb[:, i] *= X
            self.Wf[i, :] = self.Wb[:, i] / (0.5 + self.Wb[:, i].sum())
            self.active += 1
            return self.Wb[:, i], i

        return None, None


if __name__ == '__main__':

    np.random.seed(1)
    network = ART(5, 10, rho=0.5)
    data = ["   O ",
            "  O O",
            "    O",
            "  O O",
            "    O",
            "  O O",
            "    O",
            " OO O",
            " OO  ",
            " OO O",
            " OO  ",
            "OOO  ",
            "OO   ",
            "O    ",
            "OO   ",
            "OOO  ",
            "OOOO ",
            "OOOOO",
            "O    ",
            " O   ",
            "  O  ",
            "   O ",
            "    O",
            "  O O",
            " OO O",
            " OO  ",
            "OOO  ",
            "OO   ",
            "OOOO ",
            "OOOOO"]
    X = np.zeros(len(data[0]))
    for i in range(len(data)):
        for j in range(len(data[i])):
            X[j] = (data[i][j] == 'O')
        Z, k = network.learn(X)
        print("|%s|" % data[i], "-> class", k)
