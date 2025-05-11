import numpy as np

R = 8.314 # J/(mol*K)

def zero_order(a0, k, time):
    return a0 -(k * time)

def first_order(a0, k, time):
    return a0 * np.exp(-k * time)

def second_order(a0, k, time):
    return 1 / (1/a0 + k * time)

def get_default_af(order):
    defaults = {
        0: 1e5,
        1: 1e12,
        2: 1e10
    }
    return defaults[order]

def calculate_k_arrhenius(af, ea, temp, order):
    if Af is None:
        Af = get_default_af(order)
    k = Af * np.exp((-ea *1000) / (R * temp))
    return k