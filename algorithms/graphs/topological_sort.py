"""
In computer science, a topological sort or topological
ordering of a directed graph is a linear ordering of
its vertices such that for every directed edge uv from
vertex u to vertex v, u comes before v in the ordering.

The usual algorithms for topological sorting have running
time linear in the number of nodes plus the number of edges,
asymptotically O(V+E) where V are vertices (nodes) and E are edges.
"""
from collections import deque


class Graph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[] for _ in range(V)]

    def add_edge(self, u, v):  # from `u` to `v`
        self.adj[u].append(v)
        self.E += 1

    def __repr__(self):
        s = ""
        for from_vertex, to_vertices in enumerate(self.adj):
            s += f"{from_vertex} -> {to_vertices}\n"
        return s


def calc_indegrees(graph):
    indegrees = dict()

    for from_vertex, to_vertices in enumerate(graph):
        if not indegrees.get(from_vertex):
            indegrees[from_vertex] = 0
        for to_vertex in to_vertices:
            degs = indegrees.get(to_vertex)
            if not degs:
                indegrees[to_vertex] = 0
                degs = indegrees[to_vertex]
            indegrees[to_vertex] = degs + 1

    return indegrees


def kahns_algorithm(graph):
    """
    One of these algorithms, first described by Kahn (1962), works by
    choosing vertices in the same order as the eventual topological sort.
    First, find a list of "start nodes" which have no incoming edges and
    insert them into a set S; at least one such node must exist in a
    non-empty acyclic graph

    A `graph` represents an adjacency list ie. the vertices that the current
    indexed vertex connects to.

    eg. [[1,2], [2], [3], []]
    represents

    [0] -> [1]
      |     |
      |     v
       --> [2] -> [3] -> []
    """

    # Sometimes you'll be given the number of vertices and edges
    # but we will calculate them based on the graph

    indegrees = calc_indegrees(graph)
    print("indegrees", indegrees)

    V = len(indegrees)
    print("number of vertices:", V)

    # create a Queue and put the elements with zero indegrees in it
    q = deque([])
    for vertex, degs in indegrees.items():
        if degs == 0:
            q.append(vertex)

    # You can sort topologically and detect cycles in the same way
    vertex_counter = 0
    topo_sort_list = []

    while len(q) > 0:
        vertex = q.popleft()
        topo_sort_list.append(vertex)
        vertex_counter += 1

        for node in graph[vertex]:
            indegrees[node] -= 1
            if indegrees[node] == 0:
                q.append(node)

    has_cycle = vertex_counter != V

    return topo_sort_list, has_cycle


def dfs_sort(graph):
    visited = []
    topo_sort_list = []
    has_cycle = False

    def visit(vertex, stack: list, topo_sort_list: list, has_cycle: bool):
        nonlocal graph
        nonlocal visited

        # if there's a cycle, just return
        if has_cycle:
            return [], True

        if vertex in visited:
            return topo_sort_list, has_cycle
        if vertex in stack:
            return [], True

        # temporary mark
        stack.append(vertex)

        for node in graph[vertex]:
            topo_sort_list, has_cycle = visit(node, stack, topo_sort_list, has_cycle)
            if has_cycle:
                return [], True

        # remove temporary mark and add permanent mark
        stack.remove(vertex)
        visited.append(vertex)
        # add to the head (or to the tail and later reverse)
        topo_sort_list.append(vertex)

        return topo_sort_list, has_cycle

    for from_vertex, to_verteces in enumerate(graph):
        if from_vertex not in visited:
            topo_sort_list, has_cycle = visit(
                from_vertex, [], topo_sort_list, has_cycle
            )

    topo_sort_list.reverse()
    return topo_sort_list, has_cycle


if __name__ == "__main__":
    V = 5  # vertices
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(4, 1)
    graph.add_edge(4, 2)
    print(graph)
    print()

    topo_sort_list, has_cycle = kahns_algorithm(graph.adj)
    print("Kahn's algorithm (BFS)")
    print("has_cycle", has_cycle)
    print(topo_sort_list)
    print()

    topo_sort_list, has_cycle = dfs_sort(graph.adj)
    print("DFS algorithm")
    print("has_cycle", has_cycle)
    print(topo_sort_list)
    print()
    print("-------------------------------------------")

    # Graph with cycle
    V = 5  # vertices
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(4, 1)
    graph.add_edge(4, 2)
    graph.add_edge(3, 0)
    print(graph)
    print()

    topo_sort_list, has_cycle = kahns_algorithm(graph.adj)
    print("Kahn's algorithm (BFS)")
    print("has_cycle", has_cycle)
    print(topo_sort_list)
    print()

    topo_sort_list, has_cycle = dfs_sort(graph.adj)
    print("DFS algorithm")
    print("has_cycle", has_cycle)
    print(topo_sort_list)
    print()
