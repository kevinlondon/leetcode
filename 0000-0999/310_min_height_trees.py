import pytest
from collections import defaultdict
from typing import List


class Solution:
    """

    Tree: Undirected graph with any two vertices with one path (connected, no cycles)

    Each node is its own subtree right?
    So one option is to go through each tree and build its direct neighbors.

    Then iterate through the nodes and see which have which height.

    Intuition: Sorting by descending node edge count will get pretty close.
    """
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        edge_map = defaultdict(set)
        for left, right in edges:
            edge_map[left].add(right)
            edge_map[right].add(left)

        nodes_needed = set(range(n))

        roots = []

        heights = defaultdict(list)

        for node in edge_map:
            height = self.find_height(n, node, edge_map)
            heights[height].append(node)

        return heights[min(heights)]

    def find_height(self, n, node, edge_map):
        nodes_needed = set(range(n))

        height = 0
        to_visit = {node}

        while nodes_needed:
            height += 1
            nodes_needed.difference_update(to_visit)

            next_visit = set()
            for v in to_visit:
                next_visit.update(edge_map[v])

            to_visit = next_visit & nodes_needed

        return height


@pytest.mark.parametrize("n, edges, expected", [
    (7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]], [1,2]),
    (4, [[1,0],[1,2],[1,3]], [1]),  # ex 1
    (6, [[3,0],[3,1],[3,2],[3,4],[5,4]], [3, 4]),  # ex 2
    (1, [], [0]),  # ex 3
    (2, [[0,1]], [0,1])
])
def test_solution(n, edges, expected):
    assert Solution().findMinHeightTrees(n, edges) == expected
