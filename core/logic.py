from core.kinetisc import zero_order, first_order, second_order
from core.plotter import plot_concentration
import numpy as np

def simulate(data):
    order = data['reaction_order']
    a0 = data['initial_concentration']
    k = data['rate_constant']
    t = data['time']

    time = np.linspace(0, t, 500)

    match order:
        case 0:
            a_t = zero_order(a0, k, time)
        case 1:
            a_t = first_order(a0, k, time)
        case 2:
            a_t = second_order(a0, k, time)
    
    plot_concentration(time, a_t, order)