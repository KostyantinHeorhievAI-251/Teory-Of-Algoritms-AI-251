from dataclasses import dataclass

@dataclass
class Edge:
    u: int
    v: int
    weight: int

class DSU: #Disjoint Set Union
    def __init__(self, size: int) -> None:
        self.parent: list[int] = list(range(size+1)) # initially each vertex is its own parent

    def find(self, vertex: int) -> int:
        # find the root of the vertex
        if self.parent[vertex] != vertex: 
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u: int, v: int) -> bool:
        root_u = self.find(u) # find the roots of both vertices
        root_v = self.find(v)
        if root_u == root_v: # if roots are equal, adding the edge creates a cycle, dismissing
            return False
        self.parent[root_v] = root_u #Merging
        return True

class Graph:
    def __init__(self, vertices: int) -> None:
        self.vertices: int = vertices
        self.edges: list[Edge] = []

    def add_edge(self, u: int, v: int, weight: int) -> None:
        self.edges.append(Edge(u,v,weight))

    def kruskal(self) -> tuple[list[Edge], int]:
        dsu = DSU(self.vertices)
        mst: list[Edge] = []
        total_weight = 0
        sorted_edges = sorted(self.edges, key=lambda edge: edge.weight) #Sorting edges by weight in ascending
        for edge in sorted_edges:
            if dsu.union(edge.u, edge.v): # if the edge doesnt create a cycle then add it
                mst.append(edge)
                total_weight += edge.weight
            if len(mst) == self.vertices - 1: # stop if MST contains V-1 edges
                break
        if len(mst) != self.vertices - 1: #Check if all veritces are connected
            raise Exception("Граф не є зв'язаним")
        return mst, total_weight

graph = Graph(8)
graph.add_edge(1, 2, 2)
graph.add_edge(1, 3, 5)
graph.add_edge(1, 4, 1)
graph.add_edge(1, 7, 7)
graph.add_edge(2, 4, 3)
graph.add_edge(3, 5, 2)
graph.add_edge(3, 6, 4)
graph.add_edge(3, 7, 4)
graph.add_edge(4, 5, 5)
graph.add_edge(4, 6, 4)
graph.add_edge(4, 7, 9)
graph.add_edge(5, 6, 3)
graph.add_edge(6, 8, 1)
graph.add_edge(7, 8, 6)

mst, total = graph.kruskal()
for edge in mst:
    print(f"({edge.u},{edge.v}) = {edge.weight}")
print(f"Total weight: {total}")
