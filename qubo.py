import dimod


# Créez un objet BQM à partir de la fonction d'énergie quadratique
bqm = dimod.BinaryQuadraticModel.from_qubo(Q, offset=0.0)
sampler = dimod.SimulatedAnnealingSampler()
response = sampler.sample(bqm, num_reads=100)
