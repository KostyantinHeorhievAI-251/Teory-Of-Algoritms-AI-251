 INF = float('inf') #infinity
V = 8 # graph size
graph = [ # weighted adjacency matrix of a graph
    [INF, 2, 5, 1, INF, INF, 7, INF],
    [2, INF, INF, 3, INF, INF, INF, INF],
    [5, INF, INF, INF, 2, 4, 4, INF],
    [1, 3, INF, INF, 5, 4, 9, INF],
    [INF, INF, 2, 5, INF, 3, INF, INF],
    [INF, INF, 4, 4, 3, INF, INF, 1],
    [7, INF, 4, 9, INF, INF, INF, 6],
    [INF, INF, INF, INF, INF, 1, 6, INF]
]

def prim(graph):
    selected = [False]*V # tracking vertices that are included in MST
    selected[0] = True # picking vertex 1 as starting

    total = 0 # total weight
    mst = []

    while len(mst) < V-1: # filling mst up until it contains V - 1 edges
        min_weight = INF
        x = y = -1

        for i in range(V): #checking vertices that are in the mst
            if selected[i]:
                for j in range(V): #checking vertices outside the mst
                    # if not in the mst and has the minimal weight - saving the edge
                    if not selected[j] and graph[i][j] < min_weight:  
                        min_weight = graph[i][j]                      
                        x, y = i, j
        if y == -1: 
            raise Exception("Граф не є зв'язаним")

        # adding the edge in the mst
        selected[y] = True
        mst.append((x+1, y+1, min_weight))
        total += min_weight

    for u, v, w in mst:
        print(f"({u},{v}) = {w}")
    print(f"Total weight: {total}")

prim(graph)
