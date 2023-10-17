"""
Dijkstra's algorithm finds the shortest path between nodes in a weighted graph
with non-negative values.

It is not suitable for graphs with negative weights. For that, use the slower
but more generalized Floyd-Warshall algorithm.

"""
from collections import deque

from algorithms.graphs.topological_sort import Graph


# distances = [Infinity] * num_nodes
# visited = []
# curr = start with the starting node
# dist[curr] = 0

# next = choose an unvisited neighbor node
# dist = curr.dist + dist(curr, next)
# if dist < next.dist:
#   next.dist = dist
#

# visited.append(curr)

# if destination_node is visited
# or if smallest tentative distance for unvisited nodes is Infinity (which
# means the destination node is unreachable) then we're done.
# otherwise, select node with smallest distance and mark it as `curr`


def min_value_in_dict(d: dict):
    _min = float("Inf")
    min_key = -1
    for key, val in d.items():
        if val < _min:
            _min = val
            min_key = key
    return min_key, _min


def dijkstra(graph: Graph, source: int, target: int):
    V = graph.V
    adj = graph.adj

    distances = [float("Inf") for _ in range(V)]
    prev = [None for _ in range(V)]
    visited = dict()

    q = [v for v in range(V)]
    distances[source] = 0

    print("source", source)
    print("target", target)
    print("distances", distances)
    print("prev", prev)
    print("visited", visited)
    print("q", q)

    while len(q) > 0:
        print()
        print("q", q)

        unvisited_dists = {
            v: dist for v, dist in enumerate(distances) if visited.get(v) is None
        }
        print("unvisited_dists", unvisited_dists)
        vertex, min_dist = min_value_in_dict(unvisited_dists)
        print("min_dist", min_dist)

        if min_dist == float("inf"):  # there is no path to the target
            return distances, prev

        q.remove(vertex)
        print("vertex", vertex)

        if vertex == target:
            return distances, prev

        for node in adj[vertex]:
            if visited.get(node):
                continue
            dist_vertex_to_node = 1  # but in a weighed graph we would get the value
            alt = distances[vertex] + dist_vertex_to_node

            print(f"alt distance {vertex} to {node}: {alt}")

            if alt < distances[node]:
                distances[node] = alt
                prev[node] = vertex

        visited[vertex] = True

    return distances, prev


def shortest_path(prev: list[int], source: int, target: int):
    path = []

    curr = target
    if curr is not None or curr == source:
        while curr is not None:
            path.append(curr)
            curr = prev[curr]

    return path


if __name__ == "__main__":
    V = 5  # vertices
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(1, 3)
    print(graph)
    print()

    distances, prev = dijkstra(graph, 0, 3)
    print("distances", distances)
    print("prev", prev)
    path = shortest_path(prev, 0, 3)
    print("path", path)
    total = len(path)
    print("total ", total)
