"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        dict = defaultdict(list)
        def dfs(node, level):
            if not node:
                return
            dict[level].append(node.val)
            for c in node.children:
                dfs(c, level + 1)

        dfs(root, 0)
        return dict.values()