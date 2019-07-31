import dimod
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
from board import Board

# Function to setup linear coupling strenghts
linear = {1:1,2:1,3:1}

print(linear)
# Setup quadratic coupling strengths MANUALLY
quadratic = {
}


offset = -1.0
vartype = dimod.SPIN

bqm = dimod.BinaryQuadraticModel(
    linear,
    quadratic,
    offset,
    vartype)
sampler = dimod.SimulatedAnnealingSampler()
sample_set = sampler.sample(bqm,num_reads=100)
print(sample_set)
