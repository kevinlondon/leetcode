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

        leaves = [node for node, pairs in edge_map.items() if len(pairs) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                pair = edge_map[leaf].pop()
                edge_map[pair].remove(leaf)
                if len(edge_map[pair]) == 1:
                    new_leaves.append(pair)

            leaves = new_leaves
        return leaves


@pytest.mark.parametrize("n, edges, expected", [
    (7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]], [1,2]),
    (4, [[1,0],[1,2],[1,3]], [1]),  # ex 1
    (6, [[3,0],[3,1],[3,2],[3,4],[5,4]], [3, 4]),  # ex 2
    (1, [], [0]),  # ex 3
    (2, [[0,1]], [0,1])
])
def test_solution(n, edges, expected):
    assert Solution().findMinHeightTrees(n, edges) == expected
