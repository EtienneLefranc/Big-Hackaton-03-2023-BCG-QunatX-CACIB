import qiskit
from qiskit_finance.applications import GaussianConditionalIndependenceModel as GCI
import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumRegister, QuantumCircuit, Aer, execute
from qiskit.circuit.library import IntegerComparator
# from qiskit.aqua.algorithms import IterativeAmplitudeEstimation


# set problem parameters
n_z = 2
z_max = 2
z_values = np.linspace(-z_max, z_max, 2**n_z)
p_zeros = [0.15, 0.25]
rhos = [0.1, 0.05]
lgd = [1, 2]
K = len(p_zeros)
alpha = 0.05


u = GCI(n_z, z_max, p_zeros, rhos)

u.draw()
