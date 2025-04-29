import matplotlib.pyplot as plt

def plot_concentration(time, concentration, order):
    plt.plot(time, concentration)
    plt.title(f'{order} Order Reaction')
    plt.xlabel('Time [s]')
    plt.ylabel('Concentration [A] [mol/dm^3]')
    plt.grid()
    plt.show()