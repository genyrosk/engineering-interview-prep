"""
The Floyd-Warshall algorithm finds the shortest path between nodes in a
weighted graph with positive or negative values.

It is a slower but more general algorithm than Dijkstra's, which only works
for graphs with positive weights.

A single execution of the algorithm will find the lengths (summed weights)
of shortest paths between all pairs of vertices. Although it does not
return details of the paths themselves, it is possible to reconstruct the
paths with simple modifications to the algorithm.

"""


def floyd_warshall(graph: [[int]], V):
    dists = [[float("inf")] * V for _ in range(V)]

    for u in range(V):
        for v in range(V):
            if graph[u][v] is not None:
                dists[u][v] = graph[u][v]
        dists[u][u] = 0

    print(dists)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dists[i][j] > dists[i][k] + dists[k][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]
            print(dists)

    print(dists)
    return dists


if __name__ == "__main__":
    graph = [
        [None, 3, None, None],
        [3, None, 1, 5],
        [None, 1, None, 2],
        [None, 5, 2, None],
    ]
    dists = floyd_warshall(graph, 4)
    result = [[0, 3, 4, 6], [3, 0, 1, 3], [4, 1, 0, 2], [6, 3, 2, 0]]
