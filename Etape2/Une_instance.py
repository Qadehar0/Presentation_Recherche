import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#premier tdat de l'algorithme borg (thread 0) sur le probleme 3 separable-moderate de dimension 2 
def read_instance_data(file_path):
    with open(file_path, 'r') as file:
        instances = {}
        current_instance = None
        for line in file:
            if line.startswith('% index'):
                parts = line.split(',')
                current_instance = parts[1].strip().split('=')[-1].strip()
                instances[current_instance] = {'x': [], 'y': []}
            elif line.strip() and not line.startswith('%'):
                x, y = map(float, line.split())
                instances[current_instance]['x'].append(x)
                instances[current_instance]['y'].append(y)
        return instances

# Read instance data from the file
file_path = 'Etape2/bbob-biobj_f03_d02_hyp.tdat'
instances_data = read_instance_data(file_path)

# Extract data for the first instance
first_instance_data = instances_data[list(instances_data.keys())[0]]

# Plot the data for the first instance
plt.scatter(first_instance_data['x'], first_instance_data['y'], label=list(instances_data.keys())[0])

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Function Evaluation')
plt.ylabel('Indicator Value')
plt.title('Instance 1')
plt.show()


