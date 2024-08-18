import networkx as nx
import matplotlib.pyplot as plt

def check_edges_in_interval_graph_v3(sequence, n):
    edges_between_vertices = []
    
    # Find the position of each vertex in the sequence
    positions = {v: i for i, v in enumerate(sequence)}
    
    # Check each pair of vertices to see if their intervals overlap
    for i in range(len(sequence)):
        vi = sequence[i]
        
        # Determine the intervals [Li, Ri] for vi
        if vi <= n:
            Li = positions[vi]
            Ri = positions[vi + n]
            
            # Compare with each subsequent vertex vj
            for j in range(i + 1, len(sequence)):
                vj = sequence[j]
                
                if vj <= n:
                    Lj = positions[vj]
                    Rj = positions[vj + n]
                    
                    # Check if the intervals [Li, Ri] and [Lj, Rj] overlap
                    if max(Li, Lj) <= min(Ri, Rj):
                        edges_between_vertices.append((vi, vj))
    
    return edges_between_vertices

# Test with the given sequence
sequence = [1, 2, 10, 3, 11, 4, 12, 5, 13, 6, 14, 7, 15, 8, 9, 16]
n = 8
# Create a graph object
G = nx.Graph()
e=check_edges_in_interval_graph_v3(sequence, n)
print(e)
G.add_edges_from(e)

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700, font_size=12)
plt.title("Interval Graph for the Given Sequence")
plt.show()