"""
Problem: https://leetcode.com/problems/snakes-and-ladders/?envType=study-plan-v2&envId=top-interview-150

"""

from typing import List


def map_cell_to_coords(cell: int, n: int):
    cell = cell % (n * n + 1)
    cell = cell - 1

    row_idx = cell // n
    row = (n - 1) - row_idx

    col = cell % n
    if (n - 1 - row) % 2 == 1:
        col = (n - 1) - col

    return row, col


def map_coords_to_cell(r: int, c: int, n: int):
    move_left = (n - 1 - r) % 2 == 0
    col = c if move_left else (n - 1) - c
    cell = ((n - 1) - r) * n + col + 1

    return cell


def find_min_in_dict(d: dict):
    _min = float("inf")
    min_vertex = -1

    for v, dist in d.items():
        if dist < _min:
            _min = dist
            min_vertex = v

    return min_vertex, _min


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # build the graph
        n = len(board)
        print("n", n)

        # adjacency graph
        graph = {cell: [] for cell in range(1, n * n + 1)}  # n**2 entries or less

        move_left = True
        curr_cell = 0
        for r in range(n - 1, -1, -1):
            # toggle
            move_left = not move_left
            for c in range(n):
                curr_cell += 1
                if move_left:
                    c = (n - 1) - c

                for next_cell in range(curr_cell + 1, min(curr_cell + 6, n * n) + 1):
                    r, c = map_cell_to_coords(next_cell, n)
                    if board[r][c] != -1:
                        next_cell = board[r][c]

                    if next_cell not in graph[curr_cell]:
                        graph[curr_cell].append(next_cell)

        for key, cells in graph.items():
            print("from:", key, " => ", cells)

        # dijkstra
        visited = []
        source = 1
        target = n * n
        prev = {v: None for v in range(1, n * n + 1)}

        distances = {v: float("Inf") for v in range(1, n * n + 1)}
        distances[1] = 0
        q = [v for v in range(1, n * n + 1)]

        while len(q) > 0:
            # pop shortest distance from unvisited set of vertices

            unvisited_dists = {
                v: dist for v, dist in distances.items() if v not in visited
            }
            vertex, min_dist = find_min_in_dict(unvisited_dists)
            if min_dist == float("inf"):  # means there's no path to the end
                return -1
            q.remove(vertex)

            if vertex == target:
                break

            for to_vertex in graph[vertex]:
                if to_vertex in visited:
                    continue
                dist = 1
                alt = distances[vertex] + dist
                if distances[to_vertex] > alt:
                    distances[to_vertex] = alt
                    prev[to_vertex] = vertex

            visited.append(vertex)

        def shortest_path(prev, source, target):
            path = []
            while target is not None:
                path.append(target)
                target = prev[target]
            return path

        path = shortest_path(prev, 1, n * n)
        print("path", path)

        shortest_dist = len(path) - 1
        print("shortest_dist", shortest_dist)

        return shortest_dist


if __name__ == "__main__":
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]
    expected_dist = 4
    solution = Solution()
    dist = solution.snakesAndLadders(board)

    assert (dist == expected_dist, f"Wrong solution, expected {expected_dist}")
