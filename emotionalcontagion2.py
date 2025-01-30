import networkx as nx
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a network of 100 nodes and add edges to randomly connect nodes
G = nx.fast_gnp_random_graph(100, 0.1)

# Set the initial state of the network
state = {node: {'valence': random.uniform(-1, 1), 'arousal': random.uniform(0, 1)} for node in G.nodes()}

# Randomly select a node to start the contagion
start_node = random.choice(list(G.nodes()))
state[start_node] = {'valence': random.uniform(0, 1), 'arousal': random.uniform(0, 1)}

# Define the probability of the behavior spreading from infected to susceptible nodes
p_spread = 0.00000034537453

# Create a function to update the state of the network in each time step
def update(frame):
    for node in G.nodes():
        if state[node]['valence'] < 0:  # Negative valence
            for neighbor in G.neighbors(node):
                if state[neighbor]['valence'] >= 0 and random.random() < p_spread:
                    state[neighbor]['valence'] -= 0.1  # Emotionally contagious
        elif state[node]['valence'] > 0:  # Positive valence
            for neighbor in G.neighbors(node):
                if state[neighbor]['valence'] <= 0 and random.random() < p_spread:
                    state[neighbor]['valence'] += 0.1  # Emotionally contagious
        # Update arousal level
        state[node]['arousal'] += random.uniform(-0.1, 0.1)
        state[node]['arousal'] = max(0, min(1, state[node]['arousal']))  # Ensure arousal stays within [0, 1]
        
    pos = nx.spring_layout(G)
    color_map = ['red' if state[node]['valence'] < 0 else 'green' if state[node]['valence'] > 0 else 'blue' for node in G.nodes()]
    node_size = [100 * state[node]['arousal'] for node in G.nodes()]  # Node size proportional to arousal level
    nx.draw(G, pos, node_color=color_map, with_labels=False, node_size=node_size)

# Create the animation using the matplotlib FuncAnimation class
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=5, interval=200, repeat=False)
plt.show()
