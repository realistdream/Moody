# Moody

README 

*Overview*

The moody.py script is a simulation of emotional contagion within a network graph. It models how emotions, represented by valence and arousal, spread across a connected network of nodes. This can be useful for understanding phenomena such as the spread of moods or attitudes in social networks.

*Features*
 - Generates a random graph of 100 nodes using NetworkX.
 - Each node is initialized with random valence (emotion) and arousal (intensity of emotion) values.
 - Simulates the spread of emotional states across nodes based on their valence.
 - Uses a simple contagion model where emotions can spread from one node to its neighbors with a small probability.
 - Animates the process using Matplotlib, showing nodes changing color and size based on their current emotional state.

*Key Functions*

 - Initialization: Nodes are created and connected randomly with initial states (valence and arousal) assigned.
 - Simulation Update: The update function changes the state of the nodes based on the emotional contagion model.  -Positive or negative valence influences neighboring nodes, and arousal levels change slightly with each update.
 - Animation: The animation is created using Matplotlib's FuncAnimation to visually depict the emotional states changing over time.

*Dependencies*

Ensure you have the following Python libraries installed:

- networkx
- matplotlib

You can install these libraries using pip: 

> bash pip install networkx matplotlib

*Usage*

To run the simulation, execute the Python script: 

> bash python emotionalcontagion2.py

This will display a window with an animated graph where nodes change their color and size, representing the dynamic spread of emotions across the network. Nodes will appear red for negative valence, green for positive valence, and are sized according to their arousal level.

*Customization*

You can adjust:
 - The number of nodes and the connection probability by modifying the parameters in the nx.fast_gnp_random_graph() function.
 - The probability of emotion spreading (p_spread) can also be adjusted to see its effect on the contagion process.
 - The animation duration and frame count can be changed in the FuncAnimation setup.

*Explanation*

This simulation provides a basic framework to explore network dynamics in the context of emotional contagion and might be extended for more complex analyses and applications. If you integrate this into your programs or expand on the code, I would be happy to hear about it!
