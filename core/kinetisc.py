import numpy as np

def zero_order(a0, k, time):
    return a0 -(k * time)

def first_order(a0, k, time):
    return a0 * np.exp(-k * time)

def second_order(a0, k, time):
    return 1 / (1/a0 + k * time)