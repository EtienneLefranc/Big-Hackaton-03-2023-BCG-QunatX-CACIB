import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


M1 = 100
PD1 = 30/100
r1 = 0.5
LGD1 = 0.6
EAD1 = 10**8
nb_simulation = 100000

N_1_PD1 = norm.ppf(PD1)


def bool_X_i(Y):
    """simulate X_i and then return the bool X_i < N_1_PD1"""
    X_i = (r1*Y + np.sqrt(1-r1**2)*np.random.standard_normal(size=None))
    return X_i < N_1_PD1


def Calcul_L(nb_simulation):
    values_L_i = np.zeros((nb_simulation, M1))
    values_L = np.zeros(nb_simulation)
    for n in range(nb_simulation):
        Y = np.random.standard_normal(size=None)
        for i in range(M1):
            if bool_X_i(Y) == True:
                L_i = EAD1*LGD1
            else:
                L_i = 0
            values_L_i[n][i] = L_i
        values_L[n] = np.sum(values_L_i[n])
    return values_L_i, values_L


values_L_i, values_L = Calcul_L(nb_simulation)
counts, bins = np.histogram(values_L, bins=61)
print(bins)
print(counts)
bin_values = np.zeros(len(counts))
for i in range(len(counts)-1):
    bin_values[i] = (bins[i+1] + bins[i])/2


values_L_i_sorted = values_L_i[values_L.argsort()]


values_L_sorted = np.sort(values_L)
nb_points_right_of_VAR = int(0.01*nb_simulation) + 1
VAR = values_L_sorted[-nb_points_right_of_VAR]

values_TRC_i = np.zeros(M1)
values_L_i_right_of_VAR = values_L_i_sorted[-nb_points_right_of_VAR:]
for i in range(M1):
    values_TRC_i[i] = np.sum(np.transpose(values_L_i_right_of_VAR)[
                             i])/nb_points_right_of_VAR


# print(VAR)
# print(values_TRC_i)
#
plt.plot(values_TRC_i)
plt.show()
bin_width = bins[1]
plt.bar(VAR, width=bin_width/3, height=max(counts))
plt.bar(x=bins[:-1], height=counts, width=bin_width, align="edge")
plt.show()
