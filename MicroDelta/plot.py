import matplotlib.pyplot as plt
from load_data import column_names
def plot_measurements(measurements, save_fig=False, fig_name=""):
    plt.style.use("seaborn-v0_8")
    plt.figure(fig_name)
    plt.subplot(211)
    plt.xlabel("Sample")
    plt.ylabel("Current [mA]")
    plt.plot(measurements[column_names[0]].to_numpy(), label=column_names[0])
    plt.plot(measurements[column_names[1]].to_numpy(), label=column_names[1])
    
    plt.grid()
    plt.legend()
    
    plt.subplot(212)
    plt.xlabel("Sample")
    plt.ylabel("Position [°]")
    plt.plot(measurements[column_names[2]].to_numpy(), label=column_names[2])
    plt.plot(measurements[column_names[3]].to_numpy(), label=column_names[3])
    
    plt.grid()
    plt.legend()
    
    if save_fig:
        plt.savefig(fig_name)
    else:
        plt.show()
    
def plot_measured_position(measurements, labels, save_fig=False, fig_name="", title=""):
    # plt.style.use("seaborn-v0_8")
    plt.figure(fig_name, figsize=(16, 9))
    plt.title(title)
    plt.xlabel("Sample")
    plt.ylabel("Position [°]")
        
    for measurement, label in zip(measurements, labels):
        plt.plot(measurement[column_names[3]].to_numpy(), label=label)
    plt.plot(measurements[-1][column_names[2]].to_numpy(), label="target position")
    
    plt.grid()
    plt.legend()
    
    if save_fig:
        plt.savefig(fig_name)
    else:
        plt.show()
    