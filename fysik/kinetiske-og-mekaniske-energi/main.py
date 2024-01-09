import matplotlib.pyplot as plt
import numpy as np

def read_file():
    file = open("ting.csv", "r")
    data = file.readlines()
    file.close()
    return data

def make_lists(data):
    time = []
    y = []
    y_velocity = []
    for line in data[1:]:
        line = line.split(";")
        time.append(float(line[0].replace(',', '.')))
        y.append(float(line[2].replace(',', '.')))
        y_velocity.append(float(line[4].replace(',', '.')))
    return time, y, y_velocity

def calculate_potential_energy(y, mass=0.6, g=9.8):
    return [mass * g * height for height in y]

def make_graph(time, y, y_velocity, potential_energy):
    fig, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('tid (s)')
    ax1.set_ylabel('y (m)', color=color)
    ax1.plot(time, y, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  

    color = 'tab:red'
    ax2.set_ylabel('y-velocity (m/s)', color=color) 
    ax2.plot(time, y_velocity, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    ax3 = ax1.twinx()
    ax3.spines['right'].set_position(('outward', 60))  

    color = 'tab:green'
    ax3.set_ylabel('Potential Energi (J)', color=color) 
    ax3.plot(time, potential_energy, color=color)
    ax3.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  
    plt.show()

def main():
    data = read_file()
    time, y, y_velocity = make_lists(data)
    potential_energy = calculate_potential_energy(y)
    make_graph(time, y, y_velocity, potential_energy)

main()
