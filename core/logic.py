from core.kinetisc import zero_order, first_order, second_order
from core.plotter import plot_concentration
import numpy as np

def simulate(order, a0, k, t):
    time = np.linspace(0, t, 500)

    order_functions = {
        0: zero_order,
        1: first_order,
        2: second_order,
    }
    
    plot_concentration(time, order_functions[order](a0, k, time), order)