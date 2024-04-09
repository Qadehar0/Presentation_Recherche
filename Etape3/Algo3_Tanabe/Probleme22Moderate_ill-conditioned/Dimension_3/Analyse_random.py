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

# On lie les données des instances du fichier
file_path = 'Etape3/Algo3_Tanabe/Probleme22Moderate_ill-conditioned/Dimension_3/bbob-biobj_f22_d03_hyp.tdat'
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

# On agrège les données pour chaque évaluation de la fonction
aggregated_data = {'x': [], 'y': []}
for data in instances_data.values():
    aggregated_data['x'].extend(data['x'])
    aggregated_data['y'].extend(data['y'])

#  On calcule la mediane pour chaque évaluation de la fonction distincte
distinct_x_values = np.unique(aggregated_data['x'])
medians = []
for x in distinct_x_values:
    y_values = [aggregated_data['y'][i] for i in range(len(aggregated_data['x'])) if aggregated_data['x'][i] == x]
    medians.append(np.median(y_values))

# On affiche chaque instance avec une couleur différente
for i, (instance_name, data) in enumerate(instances_data.items()):
    plt.scatter(data['x'], data['y'], label=instance_name, color=colors[i])

# On affiche les points médians
plt.scatter(distinct_x_values, medians, color='red', marker='x', label='Median')

plt.xscale('log')
plt.yscale('log')
plt.xlabel('Function Evaluation')
plt.ylabel('Indicator Value')
plt.title('Instances')


plt.legend(handles=[plt.Line2D([], [], color='red', marker='x', linestyle='None', label='Median')])
plt.show()
