class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.edges = []    # List to store edges

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    # Function to find the root of a node
    def find(self, parent, node):
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])  # Path compression
        return parent[node]

    # Function to perform union of two subsets
    def union(self, parent, rank, x, y):
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)

        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    # Kruskal's algorithm
    def kruskal(self):
        # Sort edges by weight
        self.edges.sort(key=lambda edge: edge[2])
        parent = []
        rank = []
        mst = []  # To store the MST

        # Initialize parent and rank arrays
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Process edges
        for u, v, weight in self.edges:
            rootU = self.find(parent, u)
            rootV = self.find(parent, v)

            # If including this edge doesn't form a cycle
            if rootU != rootV:
                mst.append((u, v, weight))
                self.union(parent, rank, rootU, rootV)

        return mst

# Example Usage
g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

mst = g.kruskal()
print("Edges in MST:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")

