# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, parent):
            if not node:
                return

            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)
        q = deque([target])
        seen = {target}
        distance = 0

        while q and distance < k:
            curr_len = len(q)
            for i in range(curr_len):
                node = q.popleft()
                for n in [node.left, node.right, node.parent]:
                    if n and n not in seen:
                        seen.add(n)
                        q.append(n)
            distance += 1
        
        return [node.val for node in q]

        