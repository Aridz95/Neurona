from perceptron import Perceptron
import matplotlib.pyplot as plt
from plotregions import plot_decision_regions as pdg
import pandas as pd
import numpy as np


class Neurona():


    def __init__(self, file=None, headerPos=None, N_Data=100, ColumnsUse=[0, 2], Subtype='setosa', target=4):
        self.file = file
        self.headerPos = headerPos
        self.datos = N_Data
        self.columnsUse = ColumnsUse
        self.subtype = Subtype
        self.datafile = pd.read_csv(self.file, header=self.headerPos)
        self.d100 = self.datafile.iloc[:self.datos, target].values
        self.y = np.where(self.d100 == self.subtype, -1, 1)

        self.X = self.datafile.iloc[:self.datos, self.columnsUse].values

    def train(self, plot=False, eta=0.01, N_Iter=50):
        self.pt = Perceptron(eta, N_Iter)
        self.pt.fit(self.X, self.y)

        if plot:
            plt.plot(range(1, len(self.pt.errors_) + 1), self.pt.errors_, marker='o')
            plt.xlabel('Epochs')
            plt.ylabel('Number of updates')
            plt.show()

    def plot_regions(self):
        pdg(self.X, self.y, self.pt)
        plt.xlabel('sepal length [cm]')
        plt.ylabel('petal length [cm]')
        plt.legend(loc='upper left')
        plt.show()
