
# hypothesis: smaller values of p make the statement
# "less than M(1-2p) of M tosses of a coin with probability 1-p of heads are heads" 
# less likely to be true

#  need to make sure that p isnt too small, or there is a decent failure probability for the statement

# if p is small, the statement has high failure probability

import numpy as np
import matplotlib.pyplot as plt

M = 100
NUM_EXPERIMENTS = 1000

def fail_pr(p):
    coin_tosses = np.random.random((NUM_EXPERIMENTS, M)) < 1-p
    row_sums = np.sum(coin_tosses, axis=1)
    bad_row_sum = row_sums <= M*(1-2*p)
    return np.sum(bad_row_sum)/NUM_EXPERIMENTS

print(fail_pr(0.05))
print(fail_pr(0.01))

