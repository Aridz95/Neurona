import random as rd
import pandas as pd

def f(x):
        return .5 * x + 2


def generar_datos(N_Data = 100, Rango = [0, 10], name = 'data.csv'):

    x = [rd.uniform(Rango[0],Rango[1]) for _ in range(N_Data)]
    y = [rd.uniform(Rango[0],Rango[1]) for _ in range(N_Data)]

    target = []
    for _ in range(N_Data):
        if y[_] > f(x[_]):
            target.append('mayor')
        else:
            target.append('menor')
    data = {'x': x, 'y': y, 'target': target}

    df = pd.DataFrame(data)
    df.to_csv(name)