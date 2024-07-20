adj = [[1, 2, 3], [4, 5], [6]]
src = 0

for i in range(len(adj[src])):
    node = adj[src][i]
    print(f"Node {node} is matched to node {src}")
