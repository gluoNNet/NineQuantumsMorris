import dimod
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
from board import Board
import numpy as np
import sys

num_spots = 9
max_checkers = 6
our = np.zeros(num_spots,dtype=int)
enemy = np.zeros(num_spots,dtype=int)
h_const = 100

b = Board()
# FOR BOARD MARKERS:
# OURS IS 1
# ENEMY IS 2
# FREE IS 0

stopped = False
while not stopped:
    num_checkers_on_board = np.sum(our) + np.sum(enemy)
    if num_checkers_on_board >= max_checkers:
        sys.exit('Switch to phase 2')
    num_checker_constraint = - num_spots + num_checkers_on_board + 2
    c = num_checker_constraint # just to simplify
    linear = {}
    for i in range(num_spots):
        if our[i] == 1:
            linear[i+1] = h_const
        elif enemy[i] == 1:
            linear[i+1] = -h_const
        else:
            linear[i+1] = 0
        #print(linear)

    # Adding quadratic terms
    quadratic = {}
    for i in range(1,num_spots):
        for j in range(i+1,num_spots+1):
            quadratic[(i,j)] = 2
    # Update linear
    for i in range(1,num_spots+1):
        linear[i] -= 2*c

    offset = 0#-(c**2+num_spots) # Think about sign

    vartype = dimod.SPIN

    bqm = dimod.BinaryQuadraticModel(
        linear,
        quadratic,
        offset,
        vartype)
    sampler = dimod.SimulatedAnnealingSampler()
    sample_set = sampler.sample(bqm,num_reads=10)
    next_state = sample_set.samples()[0] # Maybe do sampling instead??
    for i in range(1,num_spots+1):
        if next_state[i]==1:
            enemy[i-1]=1
            b.place_marker(pos=i-1,player_num=2)
    print(enemy)
    print(b)

    # Choose our input
    our_pos = int(input('Give position to place marker (1-9): '))
    our[our_pos-1] = 1
    b.place_marker(pos=our_pos-1,player_num=1)


    #stopped = True
