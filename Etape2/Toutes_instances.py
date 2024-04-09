import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


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
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 
          'orange', 'purple', 'brown', 'pink', 'olive', 'navy', 'teal', 
          'coral', 'lime', 'lavender', 'turquoise', 'gold', 'maroon', 
          'salmon', 'peru', 'orchid', 'indigo', 'khaki', 'skyblue', 
          'plum', 'crimson', 'darkgreen', 'darkblue', 'darkred', 
          'darkcyan', 'darkmagenta', 'darkyellow', 'darkorange', 
          'darkviolet', 'darkgray', 'lightblue', 'lightgreen', 
          'lightred', 'lightcyan', 'lightmagenta', 'lightyellow', 
          'lightpink', 'lightcoral', 'lightgrey']

# Aggregate data for each function evaluation
aggregated_data = {'x': [], 'y': []}
for data in instances_data.values():
    aggregated_data['x'].extend(data['x'])
    aggregated_data['y'].extend(data['y'])

# Calculate median for each distinct function evaluation
distinct_x_values = np.unique(aggregated_data['x'])
medians = []
for x in distinct_x_values:
    y_values = [aggregated_data['y'][i] for i in range(len(aggregated_data['x'])) if aggregated_data['x'][i] == x]
    medians.append(np.median(y_values))

# Plot each instance with a different color
for i, (instance_name, data) in enumerate(instances_data.items()):
    plt.scatter(data['x'], data['y'], label=instance_name, color=colors[i])

# Plot median points
plt.scatter(distinct_x_values, medians, color='red', marker='x', label='Median')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Function Evaluation')
plt.ylabel('Indicator Value')
plt.title('Instances')


plt.legend(handles=[plt.Line2D([], [], color='red', marker='x', linestyle='None', label='Median')])
plt.show()



